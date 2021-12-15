import time

data = {"Sriram": {"Instagram": 30, "Twitter": 30, "Spotify": 20, "Tunein": 20, "Youtube": 60},
        "Jeyadev": {"Instagram": 60, "Twitter": 10, "Spotify": 70, "Tunein": 5, "Youtube": 150},
        "Thirupathi": {"Instagram": 37, "Twitter": 15, "Spotify": 15, "Tunein": 5, "Youtube": 20},
        "Puspanathan": {"Instagram": 45, "Twitter": 5, "Spotify": 90, "Tunein": 0, "Youtube": 120}}
User = list(data.keys())


class Track:

    def __init__(self, name):
        self.name = name

    def warning(self):
        print("Displaying All The Apps That are Overused\n")
        for k, v in data[self.name].items():
            if v > 45:
                print(k, end=" ")
        print("\n")
        time.sleep(1)
        menu()


def viewdata():
    for k, v in data.items():
        print(k, v)

    print("\n")
    menu()


def menu():
    temp = {}
    print("""
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
        for i in range(noa):
            appname = input("Enter The App Name:")
            usage = int(input("Enter The Usage In Minutes:"))
            print("\n")
            temp[appname] = usage
        data[na] = temp
        menu()
    elif choice == 3:
        viewdata()
    elif choice == 4:
        print("                         Thank You For Using Digital Wellbeing")
        exit()


menu()
