import random
class Password:
    def __init__(self):
        self.bogstaver = "abcdefghijklmnopqrstuvwxyzæøå"
        self.tal = "0123456789"
        self.tegn = "!%?=&"
        self.password_længde = 10

    def generate_password(self):
        print("password generator.exe")
        tal_set = ""
        tegn_set = ""
        while True:

            choice = input("Skal passworden indholde 'store', 'små' eller 'blandet' bogstaver?: ")
            if choice == "store":
                print("Du har valgt store bogstaver.")
                bogstaver_set = self.bogstaver.upper()
            elif choice == "små":
                print("Du har valgt små bogstaver.")
                bogstaver_set = self.bogstaver.lower()
            elif choice == "blandet":
                print("Du har valgt blandet bogstaver.")
                bogstaver_set = self.bogstaver.lower() + self.bogstaver.upper()
            else:
                print("fejl")
                continue
            break
        while True:

            choice = input("Skal passworden indholde tal? 'ja' eller 'nej': ")
            if choice == "ja":
                print("Du har valgt at passworden skal indholde tal")
                tal_set = self.tal
            elif choice == "nej":
                print("Du har valgt at den ikke skal indholde tal")
            else:
                print("fejl")
                continue
            break
        while True:
            choice = input("Skal passworden indholde speciale tegn? 'ja' eller 'nej': ")
            if choice == "ja":
                print("Du har valgt at passworden skal indholde speciale tegn")
                tegn_set = self.tegn
            elif choice == "nej":
                print("Du har valgt at passworden ikke skal indholde speciale tegn")
            else:
                print("fejl")
                continue
            break



        password = "".join(random.choice(bogstaver_set + tal_set + tegn_set) for i in range(self.password_længde))
        print(f"Dit genererede password er: {password}")

# Create an instance of the Password class

password_generator = Password()

# Call the generate_password method
password_generator.generate_password()