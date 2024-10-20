from amortization.amount import calculate_amortization_amount

from Property import Property

def input_float(prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Invalid input. Please enter a valid number.")

class Mortgage(Property):

    # Constructor for the Mortgage class, initializing mortgage details
    def __init__(self):
        self.mortgage_annual_interest = input_float("Enter the mortgage annual interest (compounded monthly): ") / 100  # Convert percentage to decimal
        #self.mortgage_annual_interest = float(4) / 100

        self.mortgage_rebates_percentages = input_float("Enter the mortgage rebates percentages: ") / 100  # Convert percentage to decimal
        #self.mortgage_rebates_percentages = float(1) / 100

        # Set the debt-to-income (DTI) ratio to 50%, representing the portion of a borrower's gross monthly income that goes towards paying debts
        self.dti_ratio = 0.5  # 50% of the income

        # Set the stress test rate to 60%, used to determine a borrower's ability to withstand higher interest rates
        self.stress_test = 0.6  # 60% of the income

    # Calculate the monthly payment for the mortgage based on loan amount and tenor
    def calculate_monthly_payment(self, loan_amount, loan_tenor_years):
        # Convert loan tenor from years to months
        loan_tenor_months = loan_tenor_years * 12
        # Calculate the monthly payment using the amortization formula and return it
        monthly_payment = calculate_amortization_amount(loan_amount, self.mortgage_annual_interest, loan_tenor_months)

        return monthly_payment
