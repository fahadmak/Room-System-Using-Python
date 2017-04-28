import db
from objects import Person

class Dojo(object):
    
    def display_welcome(self):
        print("The Dojo Room Space Allocation Program")
        print()    
        display_menu()
    
    def display_menu(self):
        print("COMMAND MENU")
        print("cat_view  - View people by category")
        print("cat_view  - View people by category")
        print("year - View people by year of joining")
        print("add  - Add a FELLOW/STAFF to a room")
        print("del  - Delete a person")
        print("exit - Exit program")
        print()
        
    
        
        
        
    
    
    
            
      
    def display_categories(self):
        
        print("CATEGORIES")
        categories = db.get_categories()    
        for category in categories:
            print(str(category.id) + ". " + category.name)
        print()
    
    def display_people_by_category(self):
        category_id = int(input("Category ID: "))
        print()
        category = db.get_category(category_id)
        people = db.get_people_by_category(category_id)
        display_people(people, category.name.upper())
        
    def display_people(self, people, title_term):
        print("MOVIES - " + title_term)
        line_format = "{:3s} {:37s} {:6s} {:5s} {:10s}"
        print(line_format.format("ID", "Name", "Year", "Mins", "Category"))
        print("-" * 64)
        for person in people:
            print(line_format.format(str(person.id), person.name,
                                     str(person.year), str(person.minutes),
                                     person.category.name))
        print()    
    
    def display_people_by_year(self):
        year = int(input("Year: "))
        print()
        people = db.get_people_by_year(year)
        display_people(people, str(year))
    
    def add_person(self):
        name        = input("Name: ")
        year        = int(input("Year: "))
        minutes     = int(input("Minutes: "))
        category_id = int(input("Category ID: "))
        
        category = db.get_category(category_id)
        person = Person(name=name, year=year, minutes=minutes,
                      category=category)
        db.add_person(person)    
        print(name + " was added to database.\n")
    
    def delete_person(self):
        person_id = int(input("Person ID: "))
        db.delete_person(person_id)
        print("Person ID " + str(person_id) + " was deleted from database.\n")
            
    def main():
        db.connect()
        display_welcome()
        display_categories()
        while True:        
            command = input("Command: ")
            if command == "cat":
                display_people_by_category()
            elif command == "year":
                display_people_by_year()
            elif command == "add":
                add_person()
            elif command == "del":
                delete_person()
            elif command == "exit":
                break
            else:
                print("Not a valid command. Please try again.\n")
                display_menu()
        db.close()
        print("Bye!")
    
    if __name__ == "__main__":
        main()
    