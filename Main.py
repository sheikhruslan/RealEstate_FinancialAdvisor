from Property import Property
from Buyer import Buyer
from Mortgage import Mortgage

def input_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# User input for property prices
t = input_float("Enter the transaction price of the property (purchase price): ")
a = input_float("Enter the valuation price of the property: ")

# Create instances of the classes
prop = Property()
buyer = Buyer()
mortgage = Mortgage()

# Calculate total expenses related to the property transaction
total_expense = prop.calculate_total_expense()
print(f"The total expense is: {total_expense:.2f}")

# Calculate the loan amount based on property and mortgage details
loan_amount = prop.calculate_loan_amount()
loan_amountB = buyer.call_loan_amount()
interest_rate = prop.interest_rate
total_expense = prop.calculate_total_expense()
months_required = buyer.calculate_time_to_accumulate(total_expense)

# Decision-making based on monthly salary
if buyer.monthly_salary > 36000:
    downpayment = prop.calculate_downpayment()
    print(f"The downpayment is: {downpayment[1]:.2f}")
    tenor_options = [10, 15, 20, 25, 30]
    for tenor in tenor_options:
        prop.tenor = tenor  # Update the tenor attribute of the prop object
        insurance = prop.calculate_mortgage_insurance(prop.ltv, prop.valuation_price, prop.tenor)
        print(f'Mortgage insurance for a {tenor}-year loan: {insurance[1]:.2f}')
        insurance_plus_loan = prop.calculate_mortgage_insurance(prop.ltv, prop.valuation_price, prop.tenor)
        print(f'Loan Amount, including mortgage insurance, for a {tenor}-year loan: {(insurance_plus_loan[1] + loan_amount[1]):.2f}')
    print(f"The monthly payment is: {buyer.calculate_monthly_payment(loan_amountB[1], interest_rate, months_required):.2f}")
    print(f"The loan amount is: {prop.calculate_loan_amount()[1]:.2f}")
else:
    # Lower salary adjustments and calculations
    downpayment = prop.calculate_downpayment()
    print(f"The downpayment is: {downpayment[0]:.2f}")
    tenor_options = [10, 15, 20, 25, 30]
    for tenor in tenor_options:
        prop.tenor = tenor  # Update the tenor attribute of the prop object
        insurance = prop.calculate_mortgage_insurance(prop.ltv, prop.valuation_price, prop.tenor)
        print(f'Mortgage insurance for a {tenor}-year loan: {insurance[0]:.2f}')
        insurance_plus_loan = prop.calculate_mortgage_insurance(prop.ltv, prop.valuation_price, prop.tenor)
        print(f'Loan Amount, including mortgage insurance, for a {tenor}-year loan: {(insurance_plus_loan[0] + loan_amount[0]):.2f}')
    print(f"The monthly payment is: {buyer.calculate_monthly_payment(loan_amountB[0], interest_rate, months_required):.2f}")
    print(f"The loan amount is: {prop.calculate_loan_amount()[0]:.2f}")


# Calculate bank rebate and display
bank_rebate = prop.calculate_bank_rebate()
print(f"The bank rebate is: {bank_rebate:.2f}")

# Calculate time to save enough for total expenses and display
print(f"The number of years and months required to accumulate the total expense is: {months_required // 12} years and {months_required % 12} months.")

# Calculate DTI and Stress Test outcomes and display results
DTI = round((loan_amount[0] * (interest_rate / 100) / (1 - (1 + (interest_rate/100))**(-months_required))) / buyer.monthly_salary, 6)
if DTI > 0.5:
    print(f"The DTI is {(DTI*100):.2f}%, thus it is not feasible as the DTI is above 50%")
else:
    print(f"The DTI is {(DTI*100):.2f}%, thus it is feasible as the DTI is less than 50%")

stress = round((loan_amount[0] * ((interest_rate + 2) / 100) / (1 - (1 + ((interest_rate+2)/100))**(-months_required))) / buyer.monthly_salary, 6)
if stress > 0.6:
    print(f"The Stress-Test figure is {(stress*100):.2f}%, thus it is not feasible as the Stress-Test figure is above than 60%")
else:
    print(f"The Stress-Test figure is {(stress*100):.2f}%, thus it is feasible as the Stress-Test figure is less than 60%")


