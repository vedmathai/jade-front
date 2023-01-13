<<<<<<< HEAD
import uuid


=======
>>>>>>> ca8ba0c2 (CRUD for projects)
class JadeProject:
    def __init__(self):
        self._id = None
        self._name = None
        self._jade_requests = []

    def id(self):
        return self._id

    def name(self):
        return self._name

    def jade_requests(self):
        return self._jade_requests

    def set_id(self, id):
        self._id = id

    def set_name(self, name):
        self._name = name

    def set_jade_requests(self, jade_requests):
        self._jade_requests = jade_requests

    def to_dict(self):
        return {
            'id': self.id(),
            'name': self.name(),
            'jade_requests': self.jade_requests(),
        }

    @staticmethod
    def from_dict(jade_project_dict):
        jade_project = JadeProject()
        jade_project.set_id(jade_project_dict['id'])
        jade_project.set_name(jade_project_dict['name'])
        jade_project.set_jade_requests(jade_project_dict['jade_requests'])
        return jade_project
<<<<<<< HEAD

    @staticmethod
    def create():
        jade_project = JadeProject()
        jade_project.set_id(str(uuid.uuid4()))
        return jade_project
=======
>>>>>>> ca8ba0c2 (CRUD for projects)
