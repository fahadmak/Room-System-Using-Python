"""
Usage:
    dojo create_room (Living|Office) <room_name>...
    dojo add_person <first_name> <last_name> (Fellow|Staff) [<wants_space>]

Options:
    -h --help     Show this screen.
    -i --interactive  Interactive Mode
    -v --version
"""
import random
from rooms import Office, Living
from person import Person
from staff import Staff
from fellow import Fellow
from Docopt import docopt

spacer = " "



class Dojo(object):
    def __init__(self):
        self.rooms = []
        self.vacant_rooms = []
        self.offices = []
        self.vacant_offices = []
        self.livingspaces = []
        self.vacant_livingspaces = []
        self.people = []
        self.allocated_people = []
        self.unallocated_people = []
        self.fellows = []
        self.allocated_fellows = []
        self.staff = []
        self.allocated_staff = []

   

if __name__ == '__main__':
   arguments = docopt(__doc__)
