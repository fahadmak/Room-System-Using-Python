class Person(object):
    """
    Creates a Person object. Classes Fellow and Staff inherit from it.
    """
    def __init__(self, name):
        self.name = name
        self.emp_id = id(self)

    def __repr__(self):
        return "<Room %s>" % self.name




