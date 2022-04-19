class User:
    def __init__(self,first_name, last_name, email, acc_bal):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.acc_bal = acc_bal
    def hi(self):
        print('hi')
    def make_withdrawl(self, amount):
        if self.acc_bal >= amount:
            self.acc_bal = self.acc_bal - amount
        else:
            print('not enough cash money')
    def deposit(self, amount):
        self.acc_bal = self.acc_bal + amount
    def display_user_balance(self):
        print(f'User: {self.first_name} {self.last_name}, you have {self.acc_bal}$ wow you are rich')
    def transfer_money(self, target, amount):
        if self.acc_bal >= amount:
            self.acc_bal = self.acc_bal - amount
            target.acc_bal = target.acc_bal + amount
            print(f'{self.first_name} has {self.acc_bal}$')
            print(f'{target.first_name} has {target.acc_bal}$')

adrian = User('adrian', 'M', 'mm@gmail.com', 1000)
alex = User('Alex', 'G', 'Alex@gmail.com', 1000)
george = User('george', 'T', 'gg@gmail.com', 1000)
alex.deposit(20).deposit(20).deposit(20).make_withdrawl(5).display_user_balance()
adrian.deposit(20).deposit(20).make_withdrawl(1).make_withdrawl(1).display_user_balance().transfer_money(george, 100)
george.deposit(20).make_withdrawl(2).make_withdrawl(2).make_withdrawl(2).display_user_balance()
alex.transfer_money(george, 500)