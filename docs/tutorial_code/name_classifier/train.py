import random
import torch.nn as nn
from torch import optim
from jadelogs import Jadelogger

from name_classifier.constants import LEARNING_RATE, N_ITERS, N_EPOCHS
from name_classifier.model import RNN
from name_classifier.datahandler import Datahandler



criterion = nn.NLLLoss()


class Trainer:
    def __init__(self):
        self._datahandler = Datahandler()
        self._rnn = RNN()
        self._optimizer = optim.SGD(self._rnn.parameters(), lr=LEARNING_RATE)
        self._jade_logger = Jadelogger()

    def train(self):
        self._train_data, self._evaluate_data, self._test_data = self._datahandler.split_data()
        self._jade_logger.new_experiment()
        for epoch_i in range(N_EPOCHS):
            self._jade_logger.new_epoch()
            self.train_epoch(epoch_i)
            self.evaluate_epoch(epoch_i)

    def train_epoch(self, epoch_i):
        current_loss = 0
        all_losses = []
        for iter_i in range(N_ITERS):
            datapoint = self._train_data[iter_i]
            category, line, category_tensor, line_tensor = self._datahandler.datapoint2tensor(datapoint)
            hidden = self._rnn.initHidden()
            self._optimizer.zero_grad()
            for i in range(line_tensor.size()[0]):
                output, hidden = self._rnn(line_tensor[i], hidden)
            loss = criterion(output, category_tensor)
            loss.backward()
            self._optimizer.step()
            output, loss.item()
            current_loss += loss


    # Just return an output given a line
    def evaluate_epoch(self, line_tensor):
        hidden = self._rnn.initHidden()
        category, line, category_tensor, line_tensor = self._datahandler.datapoint2tensor(datapoint)
        for i in range(line_tensor.size()[0]):
            output, hidden = self._rnn(line_tensor[i], hidden)

        return output
