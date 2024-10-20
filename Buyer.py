from Property import Property

prop = Property()
loan_amount = prop.calculate_loan_amount()

def input_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

class Buyer:
    
    # Initialize the Buyer class with necessary financial details
    def __init__(self):
        self.initial_savings = input_float("Enter your initial savings: ")
        #self.initial_savings = float(10000)

        self.monthly_salary = input_float("Enter your monthly salary: ")
        #self.monthly_salary = float(15000)

        self.monthly_saving_percentage = input_float("Enter your monthly saving percentage: ") / 100  # Convert percentage to decimal
        #self.monthly_saving_percentage = float(20) / 100

        self.annual_return_rate = input_float("Enter the annual return rate of your saving: ") / 100  # Convert percentage to decimal
        #self.annual_return_rate = float(5) / 100

        # Initialize a Property object to use its methods
        self.loan_amounts = Property()

    # Method to call and return the loan amount calculated by the Property object
    def call_loan_amount(self):
        loan_amounts = self.loan_amounts.calculate_loan_amount()

        return loan_amounts

    # Calculate the time required to accumulate a specified total expense based on savings and returns
    def calculate_time_to_accumulate(self, total_expense):
        # Convert annual return rate to monthly for calculations
        monthly_return_rate = self.annual_return_rate / 12
        # Start with initial savings
        cumulative_savings = self.initial_savings
        # Initialize months required to 0
        months_required = 0
        # Loop until cumulative savings meet or exceed the total expense
        while cumulative_savings < total_expense:
            # Calculate monthly savings from salary
            monthly_savings = self.monthly_salary * self.monthly_saving_percentage

            return_on_investment = cumulative_savings * monthly_return_rate
            # Update cumulative savings
            cumulative_savings += monthly_savings + return_on_investment
            # Increment months required
            months_required += 1

        return months_required
    
    # Calculate the monthly payment for a loan given the loan amount, interest rate, and duration
    def calculate_monthly_payment(self, loan_amount, interest_rate, months_required):
        # Calculate monthly payment using the formula for an amortizing loan
        monthly_payment = (loan_amount * (interest_rate / 100) / (1 - (1 + (interest_rate/100))**(-months_required)))

        return monthly_payment

