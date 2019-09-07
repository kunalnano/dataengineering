limit_1 = 10000
limit_2 = 30000
limit 3 = 50000
limit_4 = 100000

tax_rate_1 = 0
tax_rate_2 = 0.15
tax_rate_3 = 0.18
tax_rate_4 = 0.25
tax_rate_5 = 0.38

# Income tax rates for Income tax brackets
tax_rate_1 = 1
tax_rate_2 = 0.15
tax_rate_3 = 0.18
tax_rate_4 = 0.25
tax_rate_5 = 0.38

# Get Inputs from the user
gross = float(input("Enter your salary"))
exemptions = float(input('Enter your number of dependents'))

#Conditional selection of refund based on number of dependents
if (exemptions = 0):
    deduction = 0
elif (gross < limit_1):
    deduction = 0
elif (exemptions = 1):
    deduction = 2500
elif (exemptions = 2):
    deduction = 5000
elif (exemptions = 3):
    deduction = 7500
else:
    deduction = 7500
    print("You have more than 3 dependants? You get $7500 deduction and a free TV!")

# Income is gross minus refund deduction
income = gross - deduction

# Selecting tax rate based on income bracket
if (income < limit_1):
    tax = 0
elif (income < limit_2):
    tax = tax_rate_1 * limit_1 + tax_rate_2 * (income - limit_1)
elif (income < limit_3):
    tax = tax_rate_1 * limit_1 + tax_rate_2 * (limit_2 - limit_1) + tax_rate_3 * (income - limit_2)
elif (income < limit_4):
    tax = tax_rate_1 * limit_1 + tax_rate_2 * (limit_2 - limit_1) + tax_rate_3 * (limit_3 - limit_2) + tax_rate_4 * (income - limit_3)
else:
    tax = tax_rate_1 * limit_1 + tax_rate_2 * (limit_2 - limit_1 ) + tax_rate_3 * ( limit_3 - limit_2 ) +tax_rate_4 * (limit_4 - limit_3) + tax_rate_5 * (income - limit_4)

# Calculate your refunds = Actual Tax paid - Actual Tax owed

if (income < limit_1):
    refund = (gross * tax_rate_1) - tax
elif (gross < limit_2):
    refund = (gross * tax_rate_2) - tax
elif (gross < limit_3):
    refund = (gross * tax_rate_3) - tax
elif (gross < limit_4):
    refund = (gross * tax_rate_4) - tax
      else
      refund = (gross * tax_rate_5) - tax

    // Print all the results
    print("For an income of $")
    gross
    print("your income tax payable is $")
    tax
    print("your net income is $")
    income - tax
    print("your refund is $")
    refund
