from jade_front.datamodel.jade_project.jade_project import JadeProject


class JadeProjectList:
    def __init__(self):
        self._jade_project_list = []

    def jade_project_list(self):
        return self._jade_project_list

    def set_jade_project_list(self, jade_project_list):
        self._jade_project_list = jade_project_list

    def append_jade_project(self, jade_project_list):
        self._jade_project_list.append(jade_project_list)

    def to_dict(self):
        return {
            'jade_project_list': [i.to_dict() for i in self.jade_project_list()],
        }

    @staticmethod
    def from_dict(jade_request_dict):
        jade_project_list = JadeProjectList()
        jade_projects = [JadeProject.from_dict(i) for i in jade_request_dict['jade_project_list']]
        jade_project_list.set_jade_project_list(jade_projects)
        return jade_project_list
