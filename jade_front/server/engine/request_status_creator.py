import numpy as np

from jade_front.server.engine.abstract_processor import AbstractProcessor
from jade_front.datamodel.jade_request_status.jade_request_status import JadeRequestStatus


class RequestStatusCreator(AbstractProcessor):
    _instance = None
    _name = 'Requests Status Creator'

    def create(self, logs) -> JadeRequestStatus:
        convert_fns = [
            self.assign_epochs,
            self.assign_losses,
            self.assign_question_answering_metrics,
        ]
        request_status = JadeRequestStatus()
        for fn in convert_fns:
            request_status = fn(logs, request_status)
        return request_status

    def assign_epochs(self, logs, request_status: JadeRequestStatus) -> JadeRequestStatus:
        experiment = logs.experiments()[0]
        current_epoch_i = len(experiment.epochs())
        total_epochs = experiment.total_epochs()
        request_status.set_current_epoch_i(current_epoch_i)
        request_status.set_total_epochs(total_epochs)
        return request_status

    def assign_losses(self, logs, request_status: JadeRequestStatus) -> JadeRequestStatus:
        experiment = logs.experiments()[0]
        epoch = experiment.epochs()[-2]
        train_batches = epoch.train_batches()
        losses = []
        mean_losses = []
        for train_batch in train_batches:
            datapoints = train_batch.datapoints()
            for datapoint in datapoints:
                losses.append(datapoint.loss())
                mean_losses.append(np.mean(losses))
        request_status.set_losses(mean_losses[50:])
        return request_status

    def assign_question_answering_metrics(self, logs, request_status: JadeRequestStatus) -> JadeRequestStatus:
        experiment = logs.experiments()[0]
        epoch = experiment.epochs()[-2]
        train_batches = epoch.train_batches()
        evaluate_batches = epoch.evaluate_batches()

        train_scores = self._batches2scores(train_batches)
        request_status.set_train_precision(train_scores['precision'])
        request_status.set_train_recall(train_scores['recall'])
        request_status.set_train_f1(train_scores['f1'])
        request_status.set_train_exact_match(train_scores['exact_match'])

        if len(evaluate_batches) > 0:
            evaluate_scores = self._batches2scores(evaluate_batches)
            request_status.set_evaluate_precision(evaluate_scores['precision'])
            request_status.set_evaluate_recall(evaluate_scores['recall'])
            request_status.set_evaluate_f1(evaluate_scores['f1'])
            request_status.set_evaluate_exact_match(evaluate_scores['exact_match'])

        return request_status

    def _batches2scores(self, batches):
        precisions = []
        recalls = []
        f1s = []
        exact_matches = []
        for batch in batches:
            datapoints = batch.datapoints()
            for datapoint in datapoints:
                expected_label = set(datapoint.expected_label())
                predicted_label = set(datapoint.predicted_label())
                precision_list = []
                recall_list = []
                for pred in predicted_label:
                    if pred in expected_label:
                        precision_list += [1]
                    else:
                        precision_list += [0]
                for expected in expected_label:
                    if expected in predicted_label:
                        recall_list += [1]
                    else:
                        recall_list += [0]
                precision = 0
                if len(precision_list) > 0:
                    precision = np.mean(precision_list)
                recall = 0
                if len(recall_list) > 0:
                    recall = np.mean(recall_list)
                f1 = 0
                if len(precision_list) == len(recall_list) == 0:
                    f1 = 1
                elif (precision + recall) != 0:
                    f1 = (2 * precision * recall) / (precision + recall)
                precisions += [precision]
                recalls += [recall]
                f1s += [f1]
                exact_matches += [1 if expected_label == predicted_label else 0]
        return {
            'precision': self._fix_decimal(np.mean(precisions)),
            'recall': self._fix_decimal(np.mean(recalls)),
            'f1': self._fix_decimal(np.mean(f1s)),
            'exact_match': self._fix_decimal(np.mean(exact_matches)),
        }
    
    def _fix_decimal(self, number):
        n_decimal = 3
        number = int(number * 10 ** n_decimal)
        number = number / (10.0 ** n_decimal) 
        return number
