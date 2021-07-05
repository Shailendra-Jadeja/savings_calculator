# print("This is a calculator to see how much you save if you are doing uber weekly, deducting weekly expenses\n"
#       "like rent, mobile bill, petrol, insurance, food expenses, groceries, miscellaneous expenses and tax!")

tax_bracket_1 = 10.5
tax_bracket_2 = 17.5
tax_bracket_3 = 30
tax_bracket_4 = 33

full_amount_of_tax_bracket_1 = 14000 * tax_bracket_1 / 100  # 1470
full_amount_of_tax_bracket_2 = (48000 - 14000) * tax_bracket_2 / 100  # 5950
full_amount_of_tax_bracket_3 = (70000 - 48000) * tax_bracket_3 / 100  # 6600
full_amount_of_tax_bracket_4 = (180000 - 70000) * tax_bracket_4 / 100  # 36300


rent = 165
mobile_bill = 10
insurance = 29.33
groceries = 20
food = 105
miscellaneous_expenses = 30
petrol = 65


def tax_in_dollars_annually(expected_income_annually):
    if expected_income_annually <= 14000:
        return expected_income_annually * tax_bracket_1 / 100
    elif 14000 < expected_income_annually <= 48000:
        return full_amount_of_tax_bracket_1 + (expected_income_annually - 14000) * tax_bracket_2 / 100
    elif 48000 < expected_income_annually <= 70000:
        return full_amount_of_tax_bracket_1 + full_amount_of_tax_bracket_2 + (expected_income_annually - 48000) \
               * tax_bracket_3 / 100


def tax_in_percentage_weekly(expected_income_annually):
    if expected_income_annually <= 14000:
        return tax_bracket_1
    else:
        return (tax_in_dollars_annually(expected_income_annually) * 100) / expected_income_annually


def budget_calculation(expected_income_annually):
    tax_in_dollars_weekly = (tax_in_percentage_weekly(expected_income_annually) / 100) * weekly_income
    expenses = rent + mobile_bill + insurance + groceries + food + miscellaneous_expenses + tax_in_dollars_weekly \
               + petrol
    savings = weekly_income - expenses
    print("Your budget:\nSavings: " + str(savings) + "\nRent: " + str(rent) + "\nMobile Bill: " + str(mobile_bill) +
          "\nInsurance: " + str(insurance) + "\nGroceries: " + str(groceries) + "\nFood: " + str(food) +
          "\nMiscellaneous Expenses: " + str(miscellaneous_expenses) + "\nPetrol: " + str(petrol) +
          "\nTax in Dollars Weekly: " + str(tax_in_dollars_weekly))


predicted_annual_income = int(input("Please input your prediction for income annually: "))
weekly_income = int(input("Please input your weekly income: "))

print("For income " + str(predicted_annual_income) + " your tax will be: " + str(
    tax_in_dollars_annually(predicted_annual_income)))

print("Your tax rate for " + str(weekly_income) + " annual income will be: "
      + str(tax_in_percentage_weekly(predicted_annual_income)) + "%")

budget_calculation(predicted_annual_income)
