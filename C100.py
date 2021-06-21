class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin
        self.amount = 50000

    def check_balance(self):
        print("Your balance is : ",self.amount )

    def withdrawl(self,withdrawAmount):
        self.amount = self.amount - withdrawAmount
        print("you have withdrawn amount "+str(withdrawAmount) +". Your remaining balance is "+ str(self.amount))


def main():
    
    Card_number = input("insert your card number:- ")
    pin_number  = input("enter your pin number:- ")

    new_user =  Atm(Card_number ,pin_number)
    count = 0
    while count<3:
        print("Choose your activity ")
        print("1.Balance Enquriy   2.withdrawl")
        activity = int(input("enter activity number :- "))

        if (activity == 1):
            new_user.check_balance()
        elif (activity == 2):
            amount = int(input("enter the amount:- "))
            new_user.withdrawl(amount)
        else:
            print("enter a valid number")

        count = count + 1

if __name__ == "__main__":
    main()