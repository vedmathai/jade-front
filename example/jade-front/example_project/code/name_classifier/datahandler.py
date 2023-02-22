import os
import random
import string
import torch
import unicodedata

from jadelogs import JadeLogger

from name_classifier.constants import FOLDERPATH


class Datahandler:
    def __init__(self):
        self._category_lines = {}
        self._all_categories = []
        self._all_letters = string.ascii_letters + " .,;'"
        self._n_letters = len(self._all_letters)
        self._jade_logger = JadeLogger()

    def load(self):
        self.read_files()

    # Turn a Unicode string to plain ASCII, thanks to https://stackoverflow.com/a/518232/2809427
    def unicodeToAscii(self, s):
        self._all_letters = string.ascii_letters + " .,;'"
        return ''.join(
            c for c in unicodedata.normalize('NFD', s)
            if unicodedata.category(c) != 'Mn'
            and c in self._all_letters
        )

    def read_files(self):
        filepaths = self._jade_logger.file_manager.list_data_dir(FOLDERPATH)
        for filepath in filepaths:
            category = os.path.splitext(os.path.basename(filepath))[0]
            lines = open(filepath, encoding='utf-8').read().strip().split('\n')
            lines = [self.unicodeToAscii(line) for line in lines]
            self._all_categories.append(category)
            self._category_lines[category] = lines

    def n_categories(self):
        return len(self._all_categories)

    def n_letters(self):
        return self._n_letters

    def category_lines(self):
        return self._category_lines

    def all_categories(self):
        return self._all_categories

    # Find letter index from all_letters, e.g. "a" = 0
    def letterToIndex(self, letter):
        return self._all_letters.find(letter)

    # Just for demonstration, turn a letter into a <1 x n_letters> Tensor
    def letterToTensor(self, letter):
        tensor = torch.zeros(1, self._n_letters)
        tensor[0][self.letterToIndex(letter)] = 1
        return tensor

    # Turn a line into a <line_length x 1 x n_letters>,
    # or an array of one-hot letter vectors
    def lineToTensor(self, line):
        tensor = torch.zeros(len(line), 1, self._n_letters)
        for li, letter in enumerate(line):
            tensor[li][0][self.letterToIndex(letter)] = 1
        return tensor

    def categoryFromOutput(self, output):
        top_n, top_i = output.topk(1)
        category_i = top_i[0].item()
        return self._all_categories[category_i]

    def split_data(self):
        data = []
        for categories, values in self.category_lines().items():
            for value in values:
                data.append((categories, value))
        train_end = int(0.8 * len(data))
        test_start = int(0.9 * len(data))
        train_data = data[:train_end]
        evaluate_data = data[train_end: test_start]
        test_data = data[test_start: ]
        random.shuffle(train_data)
        random.shuffle(test_data)
        random.shuffle(evaluate_data)
        return train_data, evaluate_data, test_data

    def datapoint2tensor(self, datapoint):
        category, line = datapoint
        category_tensor = torch.tensor([self._all_categories.index(category)], dtype=torch.long)
        line_tensor = self.lineToTensor(line)
        return category, line, category_tensor, line_tensor
