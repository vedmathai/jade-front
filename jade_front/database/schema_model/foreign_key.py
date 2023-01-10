class ForeignKey:
    def __init__(self):
        self._column = None
        self._reference_table = None
        self._reference_column = None

    def column(self) -> str:
        return self._column

    def reference_table(self) -> str:
        return self._reference_table

    def reference_column(self) -> str:
        return self._reference_column

    def set_column(self, column: str):
        self._column = column

    def set_reference_table(self, reference_table: str):
        self._reference_table = reference_table

    def set_reference_column(self, reference_column: str):
        self._reference_column = reference_column

    @staticmethod
    def from_dict(val):
        foreign_key = ForeignKey()
        foreign_key.set_column(val['column'])
        foreign_key.set_reference_table(val['reference_table'])
        foreign_key.set_reference_column(val['reference_column'])
        return foreign_key

    def to_dict(self):
        return {
            'column': self.column(),
            'reference_table': self.reference_table(),
            'reference_column': self.reference_column(),
        }
