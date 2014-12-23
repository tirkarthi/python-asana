# This file is automatically generated by generate.py using api.json

class _Projects:
    def __init__(self, session=None):
        self.session = session

    def create(self, params={}):
        return self.session.post('/projects', params)

    def update(self, project_id, params={}):
        path = '/projects/%d' % (project_id)
        return self.session.put(path, params)

    def find_by_id(self, project_id, params={}):
        path = '/projects/%d' % (project_id)
        return self.session.get(path, params)

    def find_by_workspace(self, workspace_id, params={}):
        path = '/workspaces/%d/projects' % (workspace_id)
        return self.session.get(path, params)

    def find_all(self, params={}):
        return self.session.get('/projects', params)

    def create_in_workspace(self, workspace_id, params={}):
        path = '/workspaces/%d/projects' % (workspace_id)
        return self.session.post(path, params)

    def delete(self, project_id, params={}):
        path = '/projects/%d' % (project_id)
        return self.session.delete(path, params)
