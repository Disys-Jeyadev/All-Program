
db={"Sriram":{"Nikunj","Karan","Nitesh","Sriman"},
    "Jeyadev":{"Nitesh","Sriman","Vishal","Tara",},
    "Akash": {"Jeyadev", "Praveen", "Ahamad", "Thirupathi"},
    "Ahamad": {"Thirupathi", "Akash", "Praven", "Venkat"},
    "Thirupathi": {"Arun", "Crack", "Ahamad", "Akash"}}


class Facebook:

    def __init__(self):
        self.username = input("Enter Your Name:")
        if self.username in db:
            self.friends = db[self.username]
            number = int(input("Enter The Number Of Friends You Want To Add:"))
            for i in range(number):
                self.name = input("Enter Your Name:")
                self.friends.add(self.name)
            menu()
        else:
            self.friend = set()
            number = int(input("Enter The Number Of Friends You Want To Add:"))
            for i in range(number):
                self.name = input("Enter Your Name:")
                self.friend.add(self.name)
            db[self.username] = self.friend
            menu()


def check_mutual_friend(name1, name2):
    if (name1 in db) and (name2 in db):
        friends1 = db[name1]
        friends2 = db[name2]
        mutual = friends2.difference(friends1)
    else:
        raise AttributeError("One Of the Mentioned Name is not Present")
    return mutual


def display_friends(name):
    if name in db:
        friends = db[name]
        print("My Name is", name, "And My Friends are:\n")
        for i in friends:
            print(i, end=" ")
    print("\n")
    menu()


def menu():
    print("""
          1.Add New Friends
          2.Check Out Mutual Friends
          3.Show My Friend
          4.Exit
    """)
    preference = int(input("Enter Your Preference:"))
    if preference == 1:
        obj = Facebook()
    elif preference == 2:
        name1 = input("Enter Your Name:")
        name2 = input("Enter The Name Of Your Friend:")
        mutual_friends = check_mutual_friend(name1, name2)
        print("The Recommended Friends Are: ")
        for i in mutual_friends:
            print(i, end=" ")

    elif preference == 3:
        name = input("Enter Your Name To Display Your Friend list:")
        display_friends(name)

    else:
        print("                     Thank You For Using Facebook")
        exit()


menu()
