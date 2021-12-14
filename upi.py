import random
import math
import sys



contacts={"dhanushaupi":9837423572,"paulupi":8875374234,"niteshupi":6538429534,
          "srimanupi":7126432857,"vidhyaupi":8756423657,"thakurupi":8877945681,
          "vijayupi":6549871590}  #Contact Databases

class Gpay:    # Main App

    def __init__(self):
        self.pay=input("Enter Number Or ID To Whom You Want To Pay:")

    def payment(self): # Payment Process
        if self.pay.isnumeric():
            valuecheck=contacts.values()
            if int(self.pay) in valuecheck:
                paymentconfirmation()
            else:
                contd=input("Do You Want To Add New Contact y/n?")
                if contd=='y':
                    addcontacts()
                else:
                    sys.exit()
        elif self.pay.isalpha():
            keychecker=contacts.keys()
            if self.pay in keychecker :
                paymentconfirmation()
            else:
                conts=input("Do You Want To Add New Contact y/n?")
                if conts=='y':
                    addcontacts()
                else:
                    sys.exit()

def paymentconfirmation(): # Payment Confirmation Process
    amount=int(input("Enter the Amount to be sent:"))
    key=otpgen()
    print("\n")
    value=int(input("Enter The Received OTP:"))
    print("\n")
    if key==value:
        print("                       Transaction Successful Paid %d RS"%amount)
        print("\n")
        cont=input("Do You Want To Continue y/n?")
        print("\n")
        if cont=='y':
            menu()
        else:
            print("""Thank You For Using Google Pay""")
            sys.exit()
    else:
        print("                       Transaction Failed")
        print("\n")
        j=input("Do You Want To Continue y/n?")
        print("\n")
        if j=='y':
            menu()
        else:
            print("""Thank You For Using Google Pay""")
            sys.exit()

kdef otpgen():  # OTP Generation Process
    otp=""
    digits="0123456789"

    for i in range(6):
        otp=otp+digits[math.floor(random.random()*10)]

    print("The OTP is:",otp)

    return (int(otp))


def addcontacts(): # Add New Contacts Process
    upiid=input("Enter UPI ID:")
    phonenumber=input("Enter Your Phone Number:")
    if len(phonenumber)==10:
        contacts[upiid]=int(phonenumber)
    else:
        raise ValueError("Number Should Be Of 10 Digits Try Again")
    print("\n")
    menu()

def viewcontacts(): # Viewing Contact List"
    for i,j in contacts.items():
        print("         ",i," : ",j)

    print("\n")
    menu()


def menu():  # Menu Enables Us To Use The App
    print("""
    1.Pay
    2.Add Contacts
    3.View Contacts
    4.Exit App
    """)
    pref=int(input("Enter The Number Of Your Preference:"))
    print("\n")
    if pref==1:
        pay=Gpay()
        pay.payment()
    elif pref==2:
        addcontacts()
    elif pref==3:
        viewcontacts()
    elif pref==4:
        print("""                 Thank You For Using Google Pay                             """)
        sys.exit()


menu()
