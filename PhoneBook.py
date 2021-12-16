
import sys
import time


class Phonebook:
    def __init__(self):
        self.__phonebook = {}
        self.phonebook_file = 'Phonebook.txt'

    def loadAll(self):
        # Clear the phonebook dictionary
        self.__phonebook.clear()

        # Load all of the items from the text file into the dictionary
        file = open(self.phonebook_file, 'r')
        for line in file.readlines():
            name, number = line.strip().split()
            self.__phonebook[name] = number
            self.__phonebook[name] = number

        file.close()

    def addEntry(self):
        self.loadAll()

        # Prompt the user for the details of the new entry
        name = str(input("ENTER NAME: "))
        number = input("ENTER NUMBER: ")
        if name is None or len(name) >= 15:
            sys.exit("Please Enter A Valid Name")
        if len(number) == 10:

            # Create a string to be written to the file
            new_entry = name + '\t' + number + '\n'

            # Write the string to the file
            file = open(self.phonebook_file, 'a')
            file.write(new_entry)
            file.close()
            print('\n')
            Book_1.menu()
        else:
            sys.exit("Please Enter A Valid Number!!!!!")
        time.sleep(2)

    def readAll(self):
        self.loadAll()

        # Print out the entire phonebook dictionary
        for name, number in self.__phonebook.items():
            print(name, " : ", number)
        if len(self.__phonebook) == 0:
            print("PHONEBOOK IS EMPTY \n")
        time.sleep(2)
        Book_1.menu()

    def searchEntry(self):
        self.loadAll()

        # Prompt the user for the name to search for, and search the phonebook dictionary
        search = input("ENTER NAME TO SEARCH FOR: ")
        if search in self.__phonebook.keys():
            print(search, " : ", self.__phonebook[search])
        else:
            print("ENTRY NOT FOUND \n")
        time.sleep(3)
        Book_1.menu()

    def deleteEntry(self):
        self.loadAll()

        entry_to_delete = input("ENTER NAME OF ENTRY TO DELETE: ")
        if entry_to_delete in self.__phonebook.keys():
            del self.__phonebook[entry_to_delete]
            file = open(self.phonebook_file, 'w')
            for name, number in self.__phonebook.items():
                string = name + '\t' + number + '\n'
                file.write(string)
            file.close()
            print("ENTRY DELETED SUCCESSFULLY")

        else:
            print("ENTRY NOT FOUND \n")
        time.sleep(2)
        Book_1.menu()
        # exit()

    def exitProgram(self):
        exit()

    def menu(self):
        print("""\
       -MENU-
1) READ ALL ENTRIES
2) ADD AN ENTRY
3) DELETE AN ENTRY
4) LOOK UP AN ENTRY
5) Exit\n""")
        choice = input("ENTER CHOICE: ")
        choice_menu = {'1': self.readAll,
                       '2': self.addEntry,
                       '3': self.deleteEntry,
                       '4': self.searchEntry,
                       '5': self.exitProgram}
        if choice not in choice_menu.keys():
            print("PLEASE ENTER A VALID CHOICE")
        else:
            choice_menu[choice]()


Book_1 = Phonebook()
Book_1.menu()
