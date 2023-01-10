import json

from jade_front.common.config import Config
from jade_front.database.connector import MySQLConnector
from jade_front.database.queries.add_columns import AddColumnsQuery
from jade_front.database.queries.create_databases import \
    CreateDatabasesQuery
from jade_front.database.queries.create_tables import \
    CreateTablesQuery
from jade_front.database.queries.add_foreign_keys import AddForeignKeyQuery
from jade_front.database.queries.list_columns import ListColumnsQuery
from jade_front.database.queries.list_databases import \
    ListDatabasesQuery
from jade_front.database.queries.list_tables import ListTablesQuery
from jade_front.database.queries.use_database import UseDatabaseQuery
from jade_front.database.schema_model.database import Database


class SetupDatabase():
    def setup(self, config, keyring):
        self.database_schema = self.get_schema(config, keyring)
        connector = MySQLConnector.instance()
        connection = connector.connect()
        self.create_database(connection)
        self.use_database(connection)
        self.create_tables(connection)
        self.create_columns(connection)
        self.create_foreign_keys(connection)
        connection.close()

    def get_schema(self, config, keyring):
        with open(config.database_schema_file()) as f:
            schema_dict = json.load(f)
            database_schema = Database.from_dict(schema_dict)
            return database_schema

    def create_database(self, connection):
        list_databases_query = ListDatabasesQuery()
        create_databases_query = CreateDatabasesQuery()
        databases = list_databases_query.run_query(connection)
        if self.database_schema.name() not in databases:
            create_databases_query.run_query(
                connection, self.database_schema.name()
            )

    def use_database(self, connection):
        use_databases_query = UseDatabaseQuery()
        use_databases_query.run_query(connection, self.database_schema.name())

    def create_tables(self, connection):
        list_tables_query = ListTablesQuery()
        create_tables_query = CreateTablesQuery()
        tables = list_tables_query.run_query(
            connection, self.database_schema.name()
        )
        for table in self.database_schema.tables():
            if table.name() not in tables:
                columns = table.columns()
                primary_keys = table.primary_keys()
                primary_keys = ', '.join(primary_keys)
                primary_keys = "PRIMARY KEY ({})".format(primary_keys)
                columns = ['{} {}'.format(c.name(), c.type()) for c in columns]
                columns = ', '.join(columns + [primary_keys])
                create_tables_query.run_query(
                    connection, table.name(), columns
                )

    def create_foreign_keys(self, connection):
        add_foreign_key_query = AddForeignKeyQuery()
        for table in self.database_schema.tables():
            add_foreign_key_query.run_query(
                connection, table.name(), table.foreign_keys()
            )

    def create_columns(self, connection):
        list_columns_query = ListColumnsQuery()
        add_columns_query = AddColumnsQuery()
        for table in self.database_schema.tables():
            columns = list_columns_query.run_query(connection, table.name())
            for column in table.columns():
                if column.name() not in columns:
                    add_columns_query.run_query(
                        connection,
                        table.name(),
                        column.name(),
                        column.type(),
                    )


if __name__ == '__main__':
    setupdb = SetupDatabase()
    setupdb.setup()
