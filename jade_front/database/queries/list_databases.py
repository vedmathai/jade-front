from jade_front.database.queries.abstract import AbstractQuery


class ListDatabasesQuery(AbstractQuery):
    _query_template = 'SHOW DATABASES;'

    def run_query(self, connection):
        self._query = self._query_template
        response = super().run_query(connection)
        response = [i[0] for i in response]
        return response
