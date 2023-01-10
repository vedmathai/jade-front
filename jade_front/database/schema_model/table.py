from typing import List, Dict

from jade_front.database.schema_model.column import Column
from jade_front.database.schema_model.foreign_key import ForeignKey


class Table:
    def __init__(self):
        self._name = None
        self._columns = []
        self._primary_keys = []
        self._foreign_keys = []

    def name(self) -> str:
        return self._name

    def columns(self) -> List[Column]:
        return self._columns

    def primary_keys(self) -> List[str]:
        return self._primary_keys

    def foreign_keys(self) -> List[ForeignKey]:
        return self._foreign_keys

    def set_name(self, name: str):
        self._name = name

    def set_columns(self, columns: List[Column]):
        self._columns = columns

    def set_primary_keys(self, primary_keys: List[ForeignKey]):
        self._primary_keys = primary_keys

    def set_foreign_keys(self, foreign_keys: List[Dict]):
        self._foreign_keys = foreign_keys

    @staticmethod
    def from_dict(val):
        table = Table()
        columns = [Column.from_dict(i) for i in val['columns']]
        table.set_name(val['name'])
        table.set_columns(columns)
        table.set_primary_keys(val['primary_keys'])
        table.set_foreign_keys(
            [ForeignKey.from_dict(i) for i in val.get('foreign_keys', [])]
        )
        return table

    def to_dict(self):
        return {
            'name': self.name(),
            'columns': [i.to_dict() for i in self.columns()],
            'primary_keys': self.primary_keys(),
            'foreign_keys': [i.to_dict() for i in self.foreign_keys()],
        }
