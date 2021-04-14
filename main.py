class Budget:
    def __init__(self, category):
        self.category = category
        self.balance = 0

    def deposit_fund(self, amount):
        self.balance += amount
        print(f"You deposited {amount} in {self.category} bank")
        return self.balance

    def withdraw_fund(self, amount):
        self.balance = self.balance - amount
        print(f"You withdrew {amount} from {self.category}")

    def compute_balance(self):
        print(f"balance for {self.category} is {self.balance}")

    def transfer(self, amount, category):
        self.balance -= amount
        print(f"You transferred {amount} to {category}")

    @staticmethod
    def activities():
        print('=' * 20)
        print("select\n 1, To deposit\n 2, To withdraw\n 3, To transfer\n 4, To check balance\n 5, To exit")
        print('=' * 20)

    @staticmethod
    def input_validation():
        try:
            user_input = int(input("Enter amount:.."))
            return user_input
        except ValueError:
            print("Enter an integer value")

    def budgeting(self):
        print("🌟🌟🌟🌟WELCOME👉👉👉👉")
        self.activities()
        while True:
            option = self.input_validation()
            if option == 1:
                amount = self.input_validation()
                self.deposit_fund(amount)
                self.activities()
            if option == 2:
                amount = self.input_validation()
                self.withdraw_fund(amount)
                self.activities()
            if option == 3:
                amount = self.input_validation()
                print(f"Categories available are:\n Food\n Clothing\n Entertainment\n You are currently in {self.category}")
                category = input("Enter the category you wish to transfer to:..")
                self.transfer(amount, category)
                self.activities()
            if option == 4:
                self.compute_balance()
                self.activities()
            if option == 5:
                break
            if option > 5:
                print("Invalid, option must between 1 to 5")


b = Budget('food')
b.budgeting()
