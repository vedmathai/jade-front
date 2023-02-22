import random
import torch.nn as nn
from torch import optim
from jadelogs import JadeLogger

from name_classifier.constants import (
    LEARNING_RATE, N_EPOCHS, BATCH_SIZE,
    HIDDEN_SIZE, OUTPUT_SIZE,
)

from name_classifier.model import RNN
from name_classifier.datahandler import Datahandler


criterion = nn.NLLLoss()


class Trainer:
    def __init__(self):
        self._datahandler = Datahandler()
        self._jade_logger = JadeLogger()

    def load(self):
        self._datahandler.load()
        self._rnn = RNN(
            self._datahandler.n_letters(),
            HIDDEN_SIZE,
            self._datahandler.n_categories()
        )
        self._optimizer = optim.SGD(self._rnn.parameters(), lr=LEARNING_RATE)

    def train(self):
        self._train_data, self._evaluate_data, self._test_data = self._datahandler.split_data()
        self._jade_logger.new_experiment()
        for epoch_i in range(N_EPOCHS):
            self._jade_logger.new_epoch()
            self.train_epoch(epoch_i)
            self.evaluate_epoch(epoch_i)

    def train_epoch(self, epoch_i):
        current_loss = 0
        losses = []
        batch = self._jade_logger.new_train_batch()
        self._jade_logger.current_epoch().set_size(len(self._train_data))
        for iter_i in range(len(self._train_data)):
            datapoint = self._train_data[iter_i]
            category, line, category_tensor, line_tensor = self._datahandler.datapoint2tensor(datapoint)
            hidden = self._rnn.initHidden()
            self._optimizer.zero_grad()
            for i in range(line_tensor.size()[0]):
                output, hidden = self._rnn(line_tensor[i], hidden)
            loss = criterion(output, category_tensor)
            predicted_category = self._datahandler.categoryFromOutput(output)
            self._jade_logger.new_train_datapoint(category, predicted_category, loss.item(), {})
            if len(losses) == 0:
                losses = [loss]
            else:
                losses.append(loss)
            if len(losses) == BATCH_SIZE:
                loss = sum(losses)
                loss.backward()
                self._optimizer.step()
                losses = []
                batch = self._jade_logger.new_train_batch()

    # Just return an output given a line
    def evaluate_epoch(self, epoch_i):
        hidden = self._rnn.initHidden()
        for iter_i in range(len(self._evaluate_data)):
            datapoint = self._train_data[iter_i]
            category, line, category_tensor, line_tensor = self._datahandler.datapoint2tensor(datapoint)
        category, line, category_tensor, line_tensor = self._datahandler.datapoint2tensor(datapoint)
        for i in range(line_tensor.size()[0]):
            output, hidden = self._rnn(line_tensor[i], hidden)
        return output
