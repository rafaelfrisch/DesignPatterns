from abc import ABC

class Account:
    def __init__(self):
        self.balance = 0

class Command(ABC):
      
    def __init__(self, receiver, account):
        self.receiver = receiver
        self.account = account

    def process(self):
        pass
  
class Invoker:
    
    def __init__(self):
        self.commands = []

    def store_command(self, command):
        self.commands.append(command)
  
    def execute(self):
        for command in self.commands:
            command.process()

class Receiver:

    def __init__(self, account):
        self.account = account

    def check_balance(self):
        print("Balance is: ", account.balance)
    
    def withdraw_money(self, quantity):
        message = "Not enought money in account"
        if account.balance >= quantity:
            account.balance -= quantity
            message = "Withdraw of " + str(quantity)
        print(message)

    def add_money(self, quantity):
        account.balance += quantity
        print("Added " + str(quantity) + " to the account")

class CommandCheckBalance(Command):

    def __init__(self, receiver):
        self.receiver = receiver

    def process(self):
        receiver.check_balance()

class CommandAddMoney(Command):

    def __init__(self, receiver, quantity=None):
        self.receiver = receiver
        self.quantity = 0
        if not quantity is None:
            self.quantity = quantity

    def process(self):
        receiver.add_money(self.quantity)

class CommandWithdrawMoney(Command):

    def __init__(self, receiver, quantity=None):
        self.receiver = receiver
        self.quantity = 0
        if not quantity is None:
            self.quantity = quantity

    def process(self):
        receiver.withdraw_money(self.quantity)

if __name__ == "__main__":
    
    account = Account()
    receiver = Receiver(account)
    quantity_withdraw = 50
    quantity_add = 100

    check = CommandCheckBalance(Command)
    add = CommandAddMoney(Command, quantity_add)
    withdraw = CommandWithdrawMoney(Command, quantity_withdraw)

    invoker = Invoker()
    invoker.store_command(check)
    invoker.store_command(add)
    invoker.store_command(check)
    invoker.store_command(withdraw)
    invoker.store_command(check)
    invoker.store_command(withdraw)
    invoker.store_command(check)
    invoker.store_command(withdraw)
    invoker.store_command(check)

    invoker.execute()
