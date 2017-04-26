import unittest
import os
from dojo import Dojo



class TestDojo(unittest.TestCase):

    def setUp(self):
        self.test_dojo = Dojo()

        """Create living space"""
        self.test_dojo.create_room({
            "<room_name>": ["LivingA"],
            "Living": True,
            "Office": False
        })

        """Create office"""
        self.test_dojo.create_room({
            "<room_name>": ["OfficeA"],
            "Living": False,
            "Office": True
        })

        # Assign rooms to variables
        self.livinga = self.test_dojo.livingspaces[0]
        self.officea = self.test_dojo.offices[0]

        """Add fellow that wants space"""
        self.test_dojo.add_person({
            "<first_name>": "Test",
            "<last_name>": "Fellow",
            "<wants_space>": "Y",
            "Fellow": True,
            "Staff": False
        })

        """Add staff member that wants space"""
        self.test_dojo.add_person({
            "<first_name>": "Test",
            "<last_name>": "Staff",
            "<wants_space>": "Y",
            "Fellow": False,
            "Staff": True
        })
        # Assign people to variables
        self.testfellow = self.test_dojo.people[0]
        self.teststaff = self.test_dojo.people[1]

    def test_create_room(self):
        """Test creation of rooms"""
        # LivingA and OfficeA from setup() added to relevant lists
        self.assertEqual(2, len(self.test_dojo.rooms))
        self.assertEqual(1, len(self.test_dojo.livingspaces))
        self.assertEqual(1, len(self.test_dojo.offices))

        """Test creation of multiple living spaces"""
        self.test_dojo.create_room({
            "<room_name>": ["LivingB", "LivingC"],
            "Living": True,
            "Office": False
        })
        # Two living spaces added to list of rooms and list of living spaces
        self.assertEqual(4, len(self.test_dojo.rooms))
        self.assertEqual(3, len(self.test_dojo.livingspaces))

        """Test creation of multiple offices"""
        self.test_dojo.create_room({
            "<room_name>": ["OfficeB", "OfficeC"],
            "Living": False,
            "Office": True
        })
        # Two offices added to list of rooms and list of offices
        self.assertEqual(6, len(self.test_dojo.rooms))
        self.assertEqual(3, len(self.test_dojo.offices))

        """Test that duplicate rooms are not added"""
        self.test_dojo.create_room({
            "<room_name>": ["OfficeA", "OfficeB"],
            "Living": False,
            "Office": True
        })
        # Duplicate rooms not added to any list
        self.assertEqual(6, len(self.test_dojo.rooms))
        self.assertEqual(3, len(self.test_dojo.offices))

    def test_add_person(self):
        """Test addition of people"""
        #  Test Fellow and Test Staff from setup() added to relevant lists
        self.assertEqual(2, len(self.test_dojo.people))
        self.assertEqual(1, len(self.test_dojo.fellows))
        self.assertEqual(1, len(self.test_dojo.staff))

        """Test allocation of those who want space"""
        # Check that people have been appended to rooms' lists of occupants
        self.assertEqual(2, len(self.officea.occupants))

    def test_vacant_offices(self):
        """Test that vacant rooms are added to relevant list"""
        # Add office
        self.test_dojo.create_room({
            "<room_name>": ["OfficeB"],
            "Living": False,
            "Office": True
        })

        self.test_dojo.check_vacant_rooms()

        # Check if OfficeB has been appended to relevant lists
        self.assertEqual(2, len(self.test_dojo.vacant_offices))
        self.assertEqual(3, len(self.test_dojo.vacant_rooms))

if __name__ == '__main__':
    unittest.main()

    
