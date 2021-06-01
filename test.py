class Salary():
    def __init__(self):
        self.balance = 0
        print("Bank account Created...")

    def gross_salary(self):
        total_days = int(input("Enter Number of Days  :"))
        daily_compensation = float(input("Enter Compensation per day    :"))

        basicsalary=total_days*daily_compensation;
        House_Rent_Allowance = basicsalary*20/100;
        Transport_Allowance = basicsalary*20/100;
        Medical_Expenses = basicsalary*25/100;
        tax = basicsalary*15/100;

        self.grosssalary = basicsalary+House_Rent_Allowance+Transport_Allowance+Medical_Expenses
        self.deductions = tax
        self.netsalary = self.grosssalary-self.deductions
        print("Gross salary is ", self.grosssalary)
        print("Deductions ", self.deductions)
        print("Net salary is ", self.netsalary)

    def deposit(self):
        amount = float(input("Enter the amount to deposit: "))
        self.balance = self.balance + amount + self.netsalary
        print("Deposit is successful and account balance is %f" % self.balance)

    def withdraw(self):
        amount = float(input("Enter the amount to withdraw: "))
        if (self.balance >= amount):
            self.balance = self.balance - amount
            print("The withdrawal is successful and account balance is %f" % self.balance)
        else:
            print("Insufficient Amount")
    
    def enquiry(self):
        print("Your bank account balance is %f" % self.balance)


Salary().gross_salary()
acc = Salary()
acc.deposit()
acc.withdraw()
acc.enquiry()