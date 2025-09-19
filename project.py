
class IndianBank:
    def __init__(self,name,mainbalance,pin=123):
                self.name=name
                self.mainbalance=mainbalance
                self.pin=pin
        
    def __verifypin(self,pin):
            return self.pin==pin
    def __updatedmainbalbywithdraw(self,amount):
            self.mainbalance-=amount
            print("withdrawamount:",amount)
    def __updatedmainbalancebydeposit(self,amount):
            self.mainbalance+=amount
    def __show_mainbalance(self):
            print("mainbalance:",self.mainbalance)
    def __raise_checkbook(self):
            self.__is_checkbook_holder=True
            return "checkbook approved"
    def __raise_atmcard(self):
            self.__is_atmcard_holder=True
            return "ATM card approved"

    def __atmcard_freezing(self):
            self.__is_atmcard_frreezing=True
            return "ATM card freezed"
    def  withdraw(self,amount,pin):
            if self.__verifypin(pin):
                    if amount>self.mainbalance:
                            print("insufficient balance")
                    else:
                            print("you entered wrong pin")
            else:
                    print("invallid pin")
    def __deposite(self,amount):
            if self.__verifypin(pin):
                    self.__updatedmainbalancebydeposit(amount,pin)
            else:
                    print("invallid pin")
    def check_balance(self,pin):                
            if self.__verifypin(pin):
                    self.__show_mainbalance()
            else:
                    print("invallid pin")
    def request_for_atmcard(self):
            status_of_atmcard_approval=self.__raise_atmcard()
            print(status_of_atmcard_approval)
    def request_for_checkbook(self):
            status_of_checkbook_approval=self.__raise_checkbook()
            print(status_of_checkbook_approval)
    def request_for_freeze_atmcard(self):
            status_of_atmcard_freezing=self.__atmcard_freezing()
            print(status_of_atmcard_freezing)
    def request_for_atmcard_freezing(self):     
            print(self.__atmcard_freezing())
class SavingAccount(IndianBank):
    def __init__(self, name, bal, pin=123):
        super().__init__(name, bal, pin)
        self.loanlimit = 300000

    def personal_loan_raise(self, amount):
        if amount > self.loanlimit:
            print("Loan amount exceeds limit")
        else:
            print("Loan approved")
class BusinessAccount(IndianBank):
    def __init__(self, name, bal, pin=123):
        super().__init__(name, bal, pin)
        self.loanlimit = 200000

    def business_loan_raise(self, amount):
        if amount > self.loanlimit:
            print("Loan amount exceeds limit")
        else:
            print("Loan approved")
saccount = SavingAccount("Sridevi", 50000, 123)

amount = int(input("Enter the amount to withdraw: "))
pin = int(input("Enter the pin: "))
saccount.withdraw(amount, pin)
saccount.check_balance(pin)
baccount = BusinessAccount("Sridevi Biz", 150000, 123)
baccount.business_loan_raise(150000)
baccount.check_balance(pin)
baccount.request_for_atmcard()
baccount.request_for_checkbook()
baccount.request_for_freeze_atmcard()
baccount.request_for_atmcard_freezing()
