from typing import List

from jade_front.database.schema_model.table import Table


class Database:
    def __init__(self):
        self._name = None
        self._tables = []

    def name(self) -> str:
        return self._name

    def tables(self) -> List[Table]:
        return self._tables

    def set_name(self, name: str):
        self._name = name

    def set_tables(self, tables: List[Table]):
        self._tables = tables

    @staticmethod
    def from_dict(val):
        database = Database()
        tables = [Table.from_dict(i) for i in val['tables']]
        database.set_name(val['name'])
        database.set_tables(tables)
        return database

    def to_dict(self):
        return {
            'name': self.name(),
            'tables': [i.to_dict() for i in self.tables()],
        }
