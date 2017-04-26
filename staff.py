from person import Person

class Staff(Person):

    job_type = "Staff"

    def __init__(self, name):
        super(Staff, self).__init__(name)
        self.emp_id = id(self)

    def __repr__(self):
        return "<Staff %s>" % self.name
