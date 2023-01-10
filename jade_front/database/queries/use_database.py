from jade_front.database.queries.abstract import AbstractQuery


class UseDatabaseQuery(AbstractQuery):
    _query_template = 'USE {};'

    def run_query(self, connection, database_name):
        self._query = self._query_template.format(database_name)
        response = super().run_query(connection)
        return response
