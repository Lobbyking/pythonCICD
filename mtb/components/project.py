class Project():
    def __init__(self, name, manager, creationDate):
        self.name = name
        self.manager = manager
        self.creationDate = creationDate

    def toString(self):
        return f'Name: {self.name}, Manager: {self.manager}, Creation date: {self.creationDate}'