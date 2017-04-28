class Office(Room):
    capacity = 6

    def __init__(self, name):
        super(Office, self).__init__(name)

    def __repr__(self):
        return "<Office %s>" % self.name