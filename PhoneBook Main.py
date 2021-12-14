import os

class Phonebook:
    def __init__(self):
        self.phonebook = {}
        self.phonebook_file = 'Phonebook.txt'

    def loadAll(self):
        #Clear the phonebook dictionary
        self.phonebook.clear()
        
        #Load all of the items from the text file into the dictionary
        file = open(self.phonebook_file, 'r')
        for line in file.readlines():
            name, number = line.strip().split()
            self.phonebook[name] = number
        file.close()
        
    def addEntry(self):
        self.loadAll()

        #Prompt the user for the details of the new entry
        name = input("ENTER NAME: ")
        number = input("ENTER NUMBER: ")

        #Create a string to be written to the file
        new_entry = name + '\t' + number + '\n'

        #Write the string to the file
        file = open(self.phonebook_file, 'a')
        file.write(new_entry)
        file.close()
        Book_1.menu()
        
    def readAll(self):
        self.loadAll()

        #Print out the entire phonebook dictionary
        for name, number in self.phonebook.items():
            print(name, " : ", number)
        if len(self.phonebook) == 0:
            print("PHONEBOOK IS EMPTY")
        Book_1.menu()
            
    def searchEntry(self):
        self.loadAll()

        #Prompt the user for the name to search for, and search the phonebook dictionary 
        search = input("ENTER NAME TO SEARCH FOR: ")
        if search in self.phonebook.keys():
            print(search, " : ", self.phonebook[search])
        else:
            print("ENTRY NOT FOUND")
        Book_1.menu()
    def deleteEntry(self):
        self.loadAll()

        entry_to_delete = input("ENTER NAME OF ENTRY TO DELETE: ")
        if entry_to_delete in self.phonebook.keys():
            del self.phonebook[entry_to_delete]
            file = open(self.phonebook_file, 'w')
            for name, number in self.phonebook.items():
                string = name + '\t' + number + '\n'
                file.write(string)
            file.close()
            print("ENTRY DELETED SUCCESSFULLY")

        else:
            print("ENTRY NOT FOUND")
        Book_1.menu()  
        #exit()

    def exitProgram(self):
        os._exit

    def menu(self):
        print("""\
       -MENU-
1) READ ALL ENTRIES
2) ADD AN ENTRY
3) DELETE AN ENTRY
4) LOOK UP AN ENTRY
5) Exit\n""")
        choice = input("ENTER CHOICE: ")
        choice_menu = {'1' : self.readAll,
                       '2' : self.addEntry,
                       '3' : self.deleteEntry,
                       '4' : self.searchEntry,
                       '5' : self.exitProgram}
        if choice not in choice_menu.keys():
            print("PLEASE ENTER A VALID CHOICE")
        else:
            choice_menu[choice]()
            
Book_1 = Phonebook()
Book_1.menu()
