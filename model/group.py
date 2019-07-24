class Group:

    def __init__(self, name=None):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

    def __repr__(self):
        return self.name
