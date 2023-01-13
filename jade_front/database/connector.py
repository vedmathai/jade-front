import mysql.connector
import sqlite3


class MySQLConnector:
    _instance = None

    @staticmethod
    def instantiate(config, keyring):
        if MySQLConnector._instance is None:
            MySQLConnector._instance = MySQLConnector()
            MySQLConnector._instance.load(config, keyring)

    @staticmethod
    def instance():
        return MySQLConnector._instance

    def load(self, config, keyring):
        self.host = keyring.database_uri()
        self.port = keyring.database_port()
        self.user = keyring.database_username()
        self.password = keyring.database_password()

    def connect(self):
        mydb = mysql.connector.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
        )
        return mydb

class SQLiteConnector:
    _instance = None

    @staticmethod
    def instantiate(config, keyring):
        if SQLiteConnector._instance is None:
            SQLiteConnector._instance = SQLiteConnector()
            SQLiteConnector._instance.load(config, keyring)

    @staticmethod
    def instance():
        return SQLiteConnector._instance

    def load(self, config, keyring):
        self._database = config.database_name()

    def connect(self):
        mydb = sqlite3.connect(self._database)
        return mydb
