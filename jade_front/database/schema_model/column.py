class Column:
    def __init__(self):
        self._name = None
        self._type = None

    def name(self) -> str:
        return self._name

    def type(self) -> str:
        return self._type

    def set_name(self, name: str):
        self._name = name

    def set_type(self, type: str):
        self._type = type

    @staticmethod
    def from_dict(val):
        column = Column()
        column.set_name(val['name'])
        column.set_type(val['type'])
        return column

    def to_dict(self):
        return {
            'name': self.name(),
            'type': self.type(),
        }
