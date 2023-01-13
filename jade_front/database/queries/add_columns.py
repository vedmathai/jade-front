from jade_front.database.queries.abstract import AbstractQuery


class AddColumnsQuery(AbstractQuery):
    _query_template = 'ALTER TABLE {} ADD COLUMN {} {};'

    def run_query(self, connection, table_name, column_name, data_type):
        self._query = self._query_template.format(
            table_name,
            column_name, data_type
        )
        response = super().run_query(connection)
        return response
