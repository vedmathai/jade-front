from jade_front.database.queries.abstract import AbstractQuery


class CreateTablesQuery(AbstractQuery):
    _query_template = 'CREATE TABLE {} ({});'

    def run_query(self, connection, table_name, columns):
        self._query = self._query_template.format(table_name, columns)
        response = super().run_query(connection)
        return response
