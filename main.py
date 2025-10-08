class Bankaccount:
    def __init__(self, name, balance):
        self.name=name
        self.balance=balance
        self.isactive=True
        self.CheckBook_req=False
        self.atm_req=False
    def Balance(self):
        if not self.isactive:
            print("acc is not in active")
        else:
            print("the bal is {self.balance}")
    def freeze_acc(self):
        if not self.isactive:
            print("acc is freezed")
        self.isactive=False
        print("the acc is freezen")
    def unfreeze_acc(self):
        if self.isactive:
            print ("Account already active.")
            self.is_active = True
        return ("account actived.")
    def checkBook_req(self):
        if self.CheckBook_req:
            print("already requested")
        else:
            self.CheckBook_req=True
            print("book req approved")
    def atm_req(self):
        if self.atm_req:
            print("already requested")
        else:
            self.atm_req=True
            print("atm req approved")
class Savings(Bankaccount):
        