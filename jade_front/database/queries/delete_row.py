from jade_front.database.queries.abstract import AbstractQuery


class DeleteQuery(AbstractQuery):
    _query_template = 'DELETE FROM {}'
    _query_condition_template = 'WHERE {};'

    def run_query(self, connection, table_name, value_dictionary):
        equivalence_checks = self._equivalence_checks(value_dictionary)
        self._query = self._query_template.format(
            table_name,
        )
        if len(equivalence_checks) > 0:
            self._query_condition = self._query_condition_template.format(
                equivalence_checks
            )
            self._query = self._query + ' ' + self._query_condition
        response = super().run_query(connection)
        return response

    def _equivalence_checks(self, value_dictionary):
        equivalences = []
        for k, v in value_dictionary.items():
            equivalences.append("{}='{}'".format(k, v))
        equivalence_checks = ' AND '.join(equivalences)
        return equivalence_checks
