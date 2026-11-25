# ==========================================================
# PROJECT: BANK LOAN CALCULATOR
# Language: Python 3
#
# Python concepts used:
# Unit 1: Variables, data types, input(), print(), operators,
#         if-elif-else conditions
# Unit 2: User-defined functions, parameters, return values,
#         and try-except exception handling
# ==========================================================


# FUNCTION 1: calculate_emi()
# Purpose: Calculates the monthly EMI using the EMI formula.
# Concepts: Function definition, parameters, if-else, operators,
#           arithmetic calculation, and return value.
def calculate_emi(principal, annual_rate, tenure_months):
    monthly_rate = annual_rate / (12 * 100)

    # If the interest rate is zero, use the simple division formula.
    if monthly_rate == 0:
        emi = principal / tenure_months
    else:
        emi = (
            principal
            * monthly_rate
            * (1 + monthly_rate) ** tenure_months
            / ((1 + monthly_rate) ** tenure_months - 1)
        )

    return round(emi, 2)


# FUNCTION 2: calculate_total_payable()
# Purpose: Calculates the total amount paid during the complete loan tenure.
# Concepts: Function, parameters, multiplication operator, and return value.
def calculate_total_payable(emi, tenure_months):
    return round(emi * tenure_months, 2)


# FUNCTION 3: calculate_total_interest()
# Purpose: Calculates the total interest by subtracting the principal
#          amount from the total payable amount.
# Concepts: Function, parameters, subtraction operator, and return value.
def calculate_total_interest(total_payable, principal):
    return round(total_payable - principal, 2)


# FUNCTION 4: check_eligibility()
# Purpose: Checks whether the EMI is within 40% of monthly income.
# Concepts: Function, parameters, comparison operator, if-else,
#           and returning two values.
def check_eligibility(emi, monthly_income):
    maximum_emi = monthly_income * 0.40

    if emi <= maximum_emi:
        return True, maximum_emi
    else:
        return False, maximum_emi


# FUNCTION 5: main()
# Purpose: Controls the complete program: accepts input, validates values,
#          calls the other functions, and displays the final result.
# Concepts: Function calls, input/output, variables, conditions,
#           f-strings, and try-except exception handling.
def main():
    print("========== BANK LOAN CALCULATOR ==========")

    try:
        # Taking input from the user.
        principal = float(input("Enter loan amount (Principal): "))
        annual_rate = float(input("Enter annual interest rate (%): "))
        tenure_months = int(input("Enter loan tenure (months): "))
        monthly_income = float(input("Enter monthly income: "))

        # Checking whether the entered values are valid.
        if principal <= 0:
            print("Invalid loan amount. Enter a positive amount.")
        elif annual_rate < 0 or annual_rate > 30:
            print("Invalid annual interest rate. Enter a rate from 0 to 30.")
        elif tenure_months < 1 or tenure_months > 360:
            print("Invalid tenure. Enter tenure from 1 to 360 months.")
        elif monthly_income <= 0:
            print("Invalid monthly income. Enter a positive amount.")
        else:
            # Calling FUNCTION 1 to calculate monthly EMI.
            emi = calculate_emi(principal, annual_rate, tenure_months)

            # Calling FUNCTION 2 to calculate total payable amount.
            total_payable = calculate_total_payable(emi, tenure_months)

            # Calling FUNCTION 3 to calculate total interest.
            total_interest = calculate_total_interest(total_payable, principal)

            # Calling FUNCTION 4 to check loan eligibility.
            eligible, maximum_emi = check_eligibility(emi, monthly_income)

            # Displaying the final result.
            print("\n========== LOAN CALCULATION RESULT ==========")
            print(f"EMI: Rs. {emi:.2f}")
            print(f"Total Payable: Rs. {total_payable:.2f}")
            print(f"Total Interest: Rs. {total_interest:.2f}")

            if eligible:
                print("Eligible: Yes")
            else:
                print(f"Maximum allowed EMI (40% of income): Rs. {maximum_emi:.2f}")
                print("Loan not eligible: EMI exceeds the allowed limit.")

    # Handles incorrect input, such as entering letters instead of numbers.
    except ValueError:
        print("Invalid input. Please enter numbers in the correct format.")


# Calling FUNCTION 5 to start the program.
main()
