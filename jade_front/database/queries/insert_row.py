import json
import re
from typing import Dict

from jade_front.database.queries.abstract import AbstractQuery


class InsertQuery(AbstractQuery):
    _query_template = 'INSERT INTO {} ({}) VALUES ({}) ON DUPLICATE KEY UPDATE {};'  # noqa

    def run_query(self, connection, table_name, key_dictionary,
                  value_dictionary):
        key_column_names, key_values =\
            self._get_key_names_values(key_dictionary)
        value_column_names, value_values, value_assignments =\
            self._get_value_names_values(value_dictionary)
        column_names = ', '.join(key_column_names + value_column_names)
        values = ', '.join(key_values + value_values)
        value_assignments = ', '.join(value_assignments)
        self._query = self._query_template.format(
            table_name,
            column_names,
            values,
            value_assignments,
        )
        response = super().run_query(connection)
        return response

    def _get_key_names_values(self, key_dictionary):
        key_column_names = []
        key_values = []
        for k, v in key_dictionary.items():
            key_column_names.append(k)
            key_values.append("'{}'".format(str(v)))
        return key_column_names, key_values

    def _get_value_names_values(self, value_dictionary):
        value_column_names = []
        value_values = []
        value_assignments = []
        for k, v in value_dictionary.items():
            value_column_names.append(k)
            if isinstance(v, Dict):
                v = json.dumps(v)
                v = re.sub('\'', '\\\'', v)
            value_values.append("'{}'".format(str(v)))
            value_assignments.append("{}='{}'".format(k, str(v)))
        return value_column_names, value_values, value_assignments
