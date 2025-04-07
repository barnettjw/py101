"""calculate monthly interest rate"""


# %%
def valid_number(number_str, data_type):
    """Check if a string is a valid float or integer and is greater than 0"""

    value = 0
    try:
        if data_type == "float":
            value = float(number_str)
        if data_type == "int":
            value = int(number_str)
    except ValueError:
        return False

    return value if value > 0 else False


# %%
def calc_monthly_payment(loan_amount, apr, duration_in_months):
    """Returns amount of monthly payment for a loan with monthly compound interest"""

    loan_amount = valid_number(loan_amount, "float")
    apr = valid_number(apr, "int")
    duration_in_months = valid_number(duration_in_months, "int")

    # return error message not a valid number
    if not loan_amount:
        return "Error: Loan amount must be a whole number or decimal"
    if not apr:
        return "Error: APR must be a whole number"
    if not duration_in_months:
        return "Error: Duration must be a whole number"
    monthly_interest_rate = (apr * 0.01) / 12
    compound_interest = 1 - (1 + monthly_interest_rate) ** (-duration_in_months)
    monthly_payment = loan_amount * (monthly_interest_rate / compound_interest)

    print(f"Monthly Payment: ${monthly_payment:.2f}")
    print(f"For a loan of ${loan_amount:.2f} at a {apr}% APR for {duration_in_months} months")


# %%
calc_monthly_payment(50000, 5, 30)

# %%
