class Account:
    def __init__(self, account_number, balance):
        self.account_number = int(account_number)
        self.balance = balance

    def increase_balance(self, amount):
        self.amount = amount
        self.balance += self.amount
        return self.balance

    def withdraw(self, amount):
        self.amount = amount
        self.balance -= self.amount
        return self.balance

    def show_balance(self):
        print(self.balance)


class Credit(Account):
    def __init__(self, account_number, balance, amount):
        self.amount = amount
        self.remaining_amount = amount
        super().__init__(account_number, balance)

    def give_credit(self):
        self.balance += self.amount
        return self.balance

    def pay_credit(self, number_of_months):
        monthly_payment = self.amount / number_of_months
        for _ in range(number_of_months):
            self.balance -= monthly_payment
            self.remaining_amount -= monthly_payment
        return self.balance

    def credit_fully_paid(self):
        if self.remaining_amount <= 0:
            return True
        else:
            return False


credit = Credit(500, 1000, 2500)
credit.give_credit()
number_of_months = 5
credit.pay_credit(number_of_months)
print(f"Credit amount: {credit.amount}, duration in months: {number_of_months}")
print(f"Remaining amount: {credit.remaining_amount}")
print(f"Credit fully paid: {credit.credit_fully_paid()}")
