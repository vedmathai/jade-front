

class AbstractQuery:
    def run_query(self, connection):
        response = []
        cursor = connection.cursor()
        cursor.execute(self._query)
        for i in cursor:
            response.append(i)
        cursor.close()
        return response

    def run_queries(self, connection):
        response = []
        cursor = connection.cursor()
        for query in self._queries:
            cursor.execute(query)
            for i in cursor:
                response.append(i)
        cursor.close()
        return response
