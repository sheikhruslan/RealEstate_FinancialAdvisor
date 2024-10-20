class Property:

    # Initialize the property with predefined values for transaction and valuation prices, and other financial metrics
    def __init__(self):

        #self.transaction_price = float(input("Enter the transaction price of the property (purchase price): "))
        self.transaction_price = float(320000)  # The purchase price of the property
        #self.valuation_price = float(input("Enter the valuation price of the property: "))
        self.valuation_price = float(300000)  # The appraised value of the property
        self.ltv = 90  # Loan-to-value ratio, indicating the percentage of the property's value that can be financed

        # Fixed rates for various fees associated with purchasing a property
        self.agency_fee_rate = 0.01  # Agency fee as a percentage of the transaction price
        self.legal_fee_rate = 0  # Placeholder for legal fees, to be updated
        self.stamp_duty_rate = 0  # Placeholder for stamp duty, to be updated
        self.mortgage_insurance = 0  # Placeholder for mortgage insurance amount, to be updated
        self.mortgage_insurance_rate = 0  # Placeholder for mortgage insurance rate, to be updated
        self.interest_rate = 1.2  # Interest rate for mortgage loans

    def calculate_downpayment(self):
        # Calculate the minimum downpayment required, based on the lower of transaction or valuation price
        downpayment70 = 0.3 * min(self.transaction_price, self.valuation_price) + max(self.transaction_price - self.valuation_price, 0)
        downpayment90 = 0.1 * min(self.transaction_price, self.valuation_price) + max(self.transaction_price - self.valuation_price, 0)

        # Return both downpayment options
        downpayments = [downpayment70, downpayment90]
        return downpayments

    def calculate_loan_amount(self):
        # Calculate the loan amount based on the downpayment options
        loan_amounts = []

        downpayments = self.calculate_downpayment()

        for i in downpayments:
            loan_amount = self.transaction_price - i
            loan_amounts.append(loan_amount)

        return loan_amounts

    def calculate_bank_rebate(self):
        # Calculate the bank rebate based on the valuation price of the property
        bank_rebate = self.valuation_price * 0.03
        return bank_rebate

    def calculate_mortgage_insurance(self, ltv, valuation_price, loan_tenor):
        if valuation_price <= 6000000:
            if ltv <= 75:
                mortgage_insurance_rate = 0
            elif ltv <= 80:
                mortgage_insurance_rate = {10: 0.5, 15: 0.6, 20: 0.76, 25: 0.83, 30: 0.92}[loan_tenor]
            elif ltv <= 85:
                mortgage_insurance_rate = {10: 0.86, 15: 1.02, 20: 1.25, 25: 1.35, 30: 1.41}[loan_tenor]
            else:  # ltv up to 90
                mortgage_insurance_rate = {10: 1.25, 15: 1.48, 20: 1.79, 25: 2.03, 30: 2.16}[loan_tenor]
        else:  # property value up to $15 million
            if ltv <= 75:
                mortgage_insurance_rate = 0
            elif ltv <= 80:
                mortgage_insurance_rate = {10: 0.6, 15: 0.71, 20: 0.9, 25: 0.97, 30: 1.09}[loan_tenor]
            elif ltv <= 85:
                mortgage_insurance_rate = {10: 1.01, 15: 1.2, 20: 1.46, 25: 1.57, 30: 1.64}[loan_tenor]
            else:  # ltv up to 90
                mortgage_insurance_rate = {10: 1.46, 15: 1.72, 20: 2.08, 25: 2.35, 30: 2.5}[loan_tenor]

        mortgage_insurance70 = min(self.transaction_price, self.valuation_price) * 70 / 100 * mortgage_insurance_rate
        mortgage_insurance90 = min(self.transaction_price, self.valuation_price) * 90 / 100 * mortgage_insurance_rate

        mortgage_insurances = [mortgage_insurance70, mortgage_insurance90]
        return mortgage_insurances

    def calculate_total_expense(self):
        # Calculate the total expense involved in purchasing the property, including downpayment, fees, and mortgage insurance
        downpayment = self.calculate_downpayment()
        # Calculate agency fee based on transaction price
        agency_fee = self.agency_fee_rate * self.transaction_price

        if self.transaction_price < 3000000:  # Below 3M
            legal_fee = 7000
        elif 3000000 <= self.transaction_price < 5000000:  # 3M – 5M
            legal_fee = 8000
        elif 5000000 <= self.transaction_price < 10000000:  # Above 5M and Below 10M
            legal_fee = 9000
        else:  # 10M and above
            legal_fee = 0.001 * self.transaction_price

        disbursement_fee = 3000  # Disbursement fee in all situations
        # Determine stamp duty fee based on transaction price brackets
        if self.transaction_price <= 3000000:  # Does not exceed 3M
            stamp_duty_fee = 100
        elif 3000000 < self.transaction_price <= 3528240:  # Exceeds 3M, does not exceed 3,528,240
            stamp_duty_fee = 100 + 0.10 * (self.transaction_price - 3000000)
        elif 3528240 < self.transaction_price <= 4500000:  # Exceeds 3,528,240, does not exceed 4.5M
            stamp_duty_fee = 0.015 * self.transaction_price
        elif 4500000 < self.transaction_price <= 4935480:  # Exceeds 4.5M, does not exceed 4,935,480
            stamp_duty_fee = 67500 + 0.10 * (self.transaction_price - 4500000)
        elif 4935480 < self.transaction_price <= 6000000:  # Exceeds 4,935,480, does not exceed 6M
            stamp_duty_fee = 0.0225 * self.transaction_price
        elif 6000000 < self.transaction_price <= 6642860:  # Exceeds 6M, does not exceed 6,642,860
            stamp_duty_fee = 135000 + 0.10 * (self.transaction_price - 6000000)
        elif 6642860 < self.transaction_price <= 9000000:  # Exceeds 6,642,860, does not exceed 9M
            stamp_duty_fee = 0.03 * self.transaction_price
        elif 9000000 < self.transaction_price <= 10080000:  # Exceeds 9M, does not exceed 10,080,000
            stamp_duty_fee = 270000 + 0.10 * (self.transaction_price - 9000000)
        elif 10080000 < self.transaction_price <= 20000000:  # Exceeds 10,080,000, does not exceed 20M
            stamp_duty_fee = 0.0375 * self.transaction_price
        elif 20000000 < self.transaction_price <= 21739120:  # Exceeds 20M, does not exceed 21,739,120
            stamp_duty_fee = 750000 + 0.10 * (self.transaction_price - 20000000)
        else:  # Exceeds 21,739,120
            stamp_duty_fee = 0.0425 * self.transaction_price

        # Calculate mortgage insurance here

        ltv = 90  # replace with actual LTV

        property_value = self.valuation_price  # replace with actual property value

        loan_tenor = 30  # replace with actual loan tenor

        mortgage_insurance = self.calculate_mortgage_insurance(ltv, property_value, loan_tenor)

        total_expense = downpayment[0] + agency_fee + legal_fee + disbursement_fee + stamp_duty_fee + float(mortgage_insurance[0])

        return total_expense
    
    