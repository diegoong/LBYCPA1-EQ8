def tax_calculator(income):
    tax = 0.0
    if income <= 250000:                        #income below PHP 250,000
        tax = income * 0
    elif income <= 400000:                      #income between PHP 250,000 to PHP 400,000
        tax = .15 * (income - 250000)
    elif income <= 800000:                      #income between PHP 400,000 to PHP 800,000
        tax = 22500 + .20 * (income - 400000)
    elif income <= 2000000:                     # income between PHP 800,000 to PHP 2,000,000
        tax = 102500 + .25 * (income - 800000)
    elif income <= 8000000:                     # income between PHP 2,000,000 to PHP 8,000,000
        tax = 402500 + .30 * (income - 2000000)
    else:                                       # income above PHP 8,000,000
        tax = 2202500 + .35 * (income - 8000000)
    return tax

def annual_tax(income):
    return tax_calculator(income)

def monthly_tax(income):
    return (annual_tax (income) / 12)

income = float(input("Enter your annual income: "))
annual_tax_owed = annual_tax(income)
monthly_tax_owed = monthly_tax(income)

print("Annual Tax owed: PHP %.2f" % annual_tax_owed)
print("Monthly Tax owed: PHP %.2f" % monthly_tax_owed)