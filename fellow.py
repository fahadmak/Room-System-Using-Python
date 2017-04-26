from person import Person

class Fellow(Person):

    job_type = "Fellow"

    def __init__(self, name):
        super(Fellow, self).__init__(name)
        self.emp_id = id(self)

    def __repr__(self):
        return "Fellow %s>" % self.name
