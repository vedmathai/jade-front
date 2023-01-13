from jade_front.database.queries.abstract import AbstractQuery


class ListTablesQuery(AbstractQuery):
    _query_template = "SELECT name FROM sqlite_schema WHERE type ='table' AND name NOT LIKE 'sqlite_%';"

    def run_query(self, connection, database_name):
        self._query = self._query_template.format(database_name)
        response = super().run_query(connection)
        response = [i[0] for i in response]
        return response
