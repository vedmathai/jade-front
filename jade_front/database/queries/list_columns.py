from jade_front.database.queries.abstract import AbstractQuery


class ListColumnsQuery(AbstractQuery):
    _query_template = 'SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = "{}";'  # noqa

    def run_query(self, connection, table_name):
        self._query = self._query_template.format(table_name)
        response = super().run_query(connection)
        response = [i[3] for i in response]
        return response
