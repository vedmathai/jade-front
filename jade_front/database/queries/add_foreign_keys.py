from jade_front.database.queries.abstract import AbstractQuery


class AddForeignKeyQuery(AbstractQuery):
    _query_template = "ALTER TABLE {} ADD FOREIGN KEY ({}) REFERENCES {}({});"

    def run_query(self, connection, table_name, foreign_keys):
        for fk in foreign_keys:
            self._query = self._query_template.format(
                table_name,
                fk.column(),
                fk.reference_table(),
                fk.reference_column(),
            )
            super().run_query(connection)
