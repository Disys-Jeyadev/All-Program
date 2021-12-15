
print("\t\t\tRigester to get started\n")


class login:
    def __init__(self):
        self.__username = str(input("Enter name with initial : "))
        if type(self.__username) == str:
            print("Name verified sucessfully \n")
        else:
            raise TypeError("Invalid name or check your name once again and try again")

    def unum(self):
        self.__usernumber = input("Enter Mobile Number : ")

        if type(self.__usernumber) == str:
            if len(self.__usernumber) == 10:
                print(self.__usernumber, )
                print("Mobile number verified sucessfully \n")
            else:
                raise TypeError("Check your mobile number : ")
        else:
            raise ValueError("Invalid Type check your Mobile name and Try Again")

    def mailid_verify(self):
        self.__user_emailid = input("Enter Mail ID :")
        if type(self.__user_emailid) == str:
            if len(self.__user_emailid) < 20:
                print(self.__user_emailid)
                print("Email id verified sucessfully \n")
            else:
                raise TypeError("check your Emailid")
        else:
            raise ValueError("Invalid Email Address")


class hotels:
    def selct_area(self, *args):
        self.areadb = args
        print(self.areadb)
        self.__area = input("Currently delevering to the abovelocations \n Choose a location")
        for i in args:
            if i == self.__area:
                print("Showing hotels in ", i)

    def selct_hotels(self):
        if self.__area == "Mylapore":
            print("KFC \n  Ratings - ⭐⭐⭐⭐⭐")
            print("Above Sea Level \n Ratings - **⭐⭐⭐")
            print("ALMAXA \n Ratings - ⭐⭐⭐⭐")
            print("A2B \n Ratings - ⭐⭐⭐⭐")

        else:
            raise ValueError("NO HOTELS FOUND NEAR YOU")
            if self.__area == "T Nagar":
                print("Rosewater Fine Dining \n  Ratings - *⭐⭐⭐⭐")
                print("BBQ NATION T-Nagar \n Ratings - ⭐⭐⭐⭐")
                print("Paprika \n Ratings - ⭐⭐⭐⭐")
                print("Basil With a Twist \n Ratings - ⭐⭐⭐⭐⭐")

            else:
                raise ValueError("NO HOTELS FOUND NEAR YOU")

                if self.__area == "Porur":
                    print("Copper Kitchen \n  Ratings - ⭐⭐⭐⭐")
                    print("  \n Ratings - ⭐⭐⭐⭐")
                    print("Kelfi \n Ratings - ⭐⭐⭐⭐")
                    print("Zaitoon \n Ratings - ⭐⭐⭐⭐⭐")

                else:
                    raise ValueError("NO HOTELS FOUND NEAR YOU")

                    if self.__area == "Ramapuram":
                        print("Salsa\n  Ratings - ⭐⭐⭐⭐")
                        print("Shawarma Spot \n Ratings - ⭐⭐⭐⭐")
                        print("KFC \n Ratings - ⭐⭐⭐⭐")
                        print("Paradise Briyani\n Ratings - ⭐⭐⭐⭐⭐")

                    else:
                        raise ValueError(" NO HOTELS FOUND NEAR YOU")
                        if self.__area == "Thiruvanmiyur":
                            print("Writes's cafe \n  Ratings - ⭐⭐⭐⭐")
                            print("Madurai Kumar Mess \n Ratings - ⭐⭐⭐⭐")
                            print("SS hydrabad \n Ratings - ⭐⭐⭐⭐")
                            print("NALAN'S GRAVY \n Ratings - ⭐⭐⭐⭐⭐")

                        else:
                            raise ValueError("-NO-HOTELS-FOUND-NEAR-YOU")


class dishes(hotels):
    def __init__(self):
        self.choose_hotel = input("Choose an hotel")
        self.hotel_list = ["KFC", "Above Sea Level", "ALMAXA", "A2B", "Rosewater Fine Dining", "BBQ NATION T-Nagar",
                      "Paprika","Basil With a Twist","Copper Kitchen","Kelfi","Zaitoon","Salsa","Shawarma Spot","KFC ",
                      "Paradise Briyani","Writes's cafe","Madurai Kumar Mess","SS hydrabad", "NALAN'S GRAVY"]
        self.alldishes = {"pannergobi": "Rs250", "aloomatar": "Rs199", "frenchfries": "Rs99", "manchurian": "249",
                          "sizzler": "Rs99", "wintersquash": "Rs79", "mac&cheese": "Rs249", "upma": "Rs499"}

    def menu(self):
        print(self.alldishes)
        for i in self.hotel_list:
            if i == self.choose_hotel:
                print(self.alldishes)

    def orderstatus(self):
        self.__orderdetails = input("Please Enter Your Order")
        for i in self.alldishes:
            if k in i.items():
                if k == self.__orderdetails:
                    print(k)

    def recipt(self):
        print("order placed succesfully for", self.__username)
        print("payment mode : COD")


user = login()
user.unum()
user.mailid_verify()
user1 = hotels()
user1.selct_area("Mylapore","T Nagar","Ramapuram","Porur","Thiruvanmiyur")
user1.selct_hotels()
rest = dishes()
rest.menu()
rest.orderstatus()
rest.recipt()