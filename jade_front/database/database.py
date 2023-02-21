import json

from jade_front.common.keyring import Keyring
from jade_front.common.config import Config

from jade_front.database.connector import SQLiteConnector
from jade_front.database.queries.insert_row import InsertQuery
from jade_front.database.queries.insert_row import InsertQuery
from jade_front.database.queries.delete_row import DeleteQuery
from jade_front.database.queries.read_row import ReadQuery
from jade_front.database.queries.use_database import UseDatabaseQuery
from jade_front.database.setup import SetupDatabase
from jade_front.datamodel.jade_request.jade_request import JadeRequest
from jade_front.datamodel.jade_project.jade_project import JadeProject
from jade_front.datamodel.jade_project.jade_project_list import JadeProjectList
from jade_front.database.schema_model.database import\
     Database as DatabaseSchemaModel


class Database:

    _instance = None
    _name = 'database'

    @classmethod
    def instantiate(cls):
        if cls._instance is None:
            cls._instance = Database()
            cls._instance.setup()

    @classmethod
    def instance(cls):
        if cls._instance is None:
            raise Exception('{} not instantiated.'.format(cls._name))
        return cls._instance

    def setup(self):
        config = Config.instance()
        keyring = Keyring.instance()
        SQLiteConnector.instantiate(config, keyring)
        self.database_schema = self.get_schema()
        setup_database = SetupDatabase()
        setup_database.setup(config, keyring)
        self.use_database_query = UseDatabaseQuery()

    def connect(self):
        connector = SQLiteConnector.instance()
        connection = connector.connect()
        return connection

    def close(self, connection):
        connection.commit()
        connection.close()

    def get_schema(self):
        config = Config.instance()
        with open(config.database_schema_file()) as f:
            schema_dict = json.load(f)
            database_schema = DatabaseSchemaModel.from_dict(schema_dict)
            return database_schema

    def write_jade_request(self, jade_request):
        connection = self.connect()
        table = "jade_requests"
        query = InsertQuery()
        key_dictionary = {
            "jade_request_id": jade_request.id(),
        }
        value_dictionary = {
            "jade_request": jade_request.to_dict(),
        }
        query.run_query(connection, table, key_dictionary, value_dictionary)
        self.close(connection)

    def read_jade_request(self, jade_request_id):
        connection = self.connect()
        request = None
        query = ReadQuery()
        table = "jade_requests"
        key_dictionary = {
            "jade_request_id": jade_request_id,
        }
        response = query.run_query(connection, table, key_dictionary)
        if len(response) == 1:
            request_json = response[0][1]
            request = JadeRequest.from_dict(
                json.loads(request_json)
            )
        self.close(connection)
        return request

    def read_jade_requests(self):
        connection = self.connect()
        query = ReadQuery()
        table = "jade_requests"
        key_dictionary = {}
        response = query.run_query(connection, table, key_dictionary)
        requests = []
        for i in response:
            request_json = i[1]
            requests.append(JadeRequest.from_dict(
                json.loads(request_json)
            ))
        self.close(connection)
        return requests

    def delete_jade_request(self, jade_request_id):
        connection = self.connect()
        query = DeleteQuery()
        table = "jade_requests"
        key_dictionary = {
            "jade_request_id": jade_request_id,
        }
        query.run_query(connection, table, key_dictionary)
        self.close(connection)
        return

    def write_jade_project(self, jade_project):
        connection = self.connect()
        table = "jade_projects"
        query = InsertQuery()
        key_dictionary = {
            "jade_project_id": jade_project.id(),
        }
        value_dictionary = {
            "jade_project": jade_project.to_dict(),
        }
        query.run_query(connection, table, key_dictionary, value_dictionary)
        self.close(connection)

    def read_jade_project(self, jade_project_id):
        connection = self.connect()
        request = None
        query = ReadQuery()
        table = "jade_projects"
        key_dictionary = {
            "jade_project_id": jade_project_id,
        }
        response = query.run_query(connection, table, key_dictionary)
        print(jade_project_id)
        if len(response) == 1:
            project_json = response[0][1]
            request = JadeProject.from_dict(
                json.loads(project_json)
            )
        self.close(connection)
        return request

    def read_jade_projects(self):
        connection = self.connect()
        query = ReadQuery()
        table = "jade_projects"
        key_dictionary = {}
        response = query.run_query(connection, table, key_dictionary)
        jade_project_list = JadeProjectList()
        for i in response:
            project_json = i[1]
            jade_project = JadeProject.from_dict(
                json.loads(project_json)
            )
            jade_project_list.append_jade_project(jade_project)
        self.close(connection)
        return jade_project_list

    def delete_jade_project(self, jade_project_id):
        connection = self.connect()
        query = DeleteQuery()
        table = "jade_projects"
        key_dictionary = {
            "jade_project_id": jade_project_id,
        }
        query.run_query(connection, table, key_dictionary)
        self.close(connection)
        return