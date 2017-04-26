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


    def create_room(self, args):
        """Create new room(s)"""

        print(spacer)

        new_rooms = []
        for room in args["<room_name>"]:
            if room.lower() in [r.name.lower() for r in self.rooms]:
                print("One or more rooms you tried to create already exist! " \
                      "Please try again.")
                print(spacer)
                return
            if args["Office"]:
                new_room = Office(room)
                self.offices.append(new_room)
            elif args["Living"]:
                new_room = Living(room)
                self.livingspaces.append(new_room)
            self.check_vacant_rooms()
            self.rooms.append(new_room)
            new_rooms.append(new_room)
        print("You have successfully added the following rooom(s):")
        for new_room_ in new_rooms:
            print("Name: " + ''.join(new_room_.name) + " | Type: " \
                  + new_room_.room_type)
        print(spacer)

    def check_vacant_rooms(self):
        """Add vacant rooms to lists; remove full ones from lists"""
        for office in self.offices:
            if len(office.occupants) < office.capacity:
                if office not in self.vacant_offices:
                    self.vacant_offices.append(office)
                    self.vacant_rooms.append(office)
            elif len(office.occupants) >= office.capacity:
                if office in self.vacant_offices:
                    self.vacant_offices.remove(office)
                    self.vacant_rooms.remove(office)
        for livingspace in self.livingspaces:
            if len(livingspace.occupants) < livingspace.capacity:
                if livingspace not in self.vacant_livingspaces:
                    self.vacant_livingspaces.append(livingspace)
                    self.vacant_rooms.append(livingspace)
            elif len(livingspace.occupants) >= livingspace.capacity:
                if livingspace in self.vacant_livingspaces:
                    self.vacant_livingspaces.remove(livingspace)
                    self.vacant_rooms.remove(livingspace)


if __name__ == '__main__':
   arguments = docopt(__doc__)
