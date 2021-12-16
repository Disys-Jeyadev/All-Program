import time

data = {"Sriram": {"Instagram": 30, "Twitter": 30, "Spotify": 20, "Facebook": 20, "Youtube": 60},
        "Jeyadev": {"Instagram": 60, "Twitter": 10, "Spotify": 70, "Facebook": 5, "Youtube": 150},
        "Thirupathi": {"Instagram": 37, "Twitter": 15, "Spotify": 15, "Facebook": 5, "Youtube": 20},
        "Puspanathan": {"Instagram": 45, "Twitter": 5, "Spotify": 90, "Facebook": 0, "Youtube": 120}}
User = list(data.keys())


class Track:

    def __init__(self, name):
        self.name = name

    def warning(self):
        for j in data[self.name].keys():
            print(j)
        time.sleep(2)

        print("Displaying All The Apps That are Overused\n")
        for k, v in data[self.name].items():
            if v > 45:
                print(k, end=" ")
            else:
                print("No App Is Over Used \n")
                print("WELL DONE!!!1")
                break
        print("\n")
        time.sleep(3)
        menu()


def add_data(na, noa):
    temp = {}
    '''na = input("Enter Your Name:")
    print("\n")
    noa = int(input("Enter The Number Of App Data You Want To Add?"))'''
    for i in range(noa):
        appname = input("Enter The App Name:")
        usage = int(input("Enter The Usage In Minutes:"))
        print("\n")
        temp[appname] = usage
    data[na] = temp

    time.sleep(2)
    menu()


def view_data():
    for k, v in data.items():
        print(k, v)

    print("\n")
    time.sleep(2)
    menu()


def menu():
    temp = {}
    print("""                           Menu
          1.Check For App Tracking Of a Person
          2.Add Your Data For Tracking
          3.View The Data
          4.Exit The App
          """)
    choice = int(input("Please Enter Your Choice:"))
    if choice == 1:
        print("These Are User", User)
        name = input("Enter The Name Of The Person Whom You Want To Track?")
        obj = Track(name)
        obj.warning()
    elif choice == 2:
        na = input("Enter Your Name:")
        print("\n")
        noa = int(input("Enter The Number Of App Data You Want To Add?"))
        add_data(na, noa)
        menu()
    elif choice == 3:
        view_data()
    elif choice == 4:
        print("                         Thank You For Using Digital Wellbeing")
        exit()


menu()
