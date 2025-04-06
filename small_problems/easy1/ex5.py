# Create a simple tip calculator. The program should prompt for a bill amount and a tip rate.
# The program must compute the tip, then print both the tip and the total amount of the bill.
# You can ignore input validation and assume that the user will enter valid numbers.

### algo ###

# Request user input via keyboard for bill amount using input()
# convert the string to an integer
# and assign the value to the variable bill

# Reques user input via keyboard for tip rate using input()
# convert the string to an integer
# multiply it by .01 to convert it to a percentage
# and assign the value to the variable tip_rate

# Calculate tip using the formula bill * tip_rate
# format it as dollars and assign the value to the variable tip

# Calculate total using the formula bill + tip
# format it as dollars and assign the value to the variable total

#%%
bill = float(input("What is the bill? "))
tip_rate = float(input("What is the tip percentage? ")) *.01
tip = bill * tip_rate

formatted_tip = '${:,.2f}'.format(tip)
total = '${:,.2f}'.format(bill + tip)
print(f"The tip is {formatted_tip}")
print(f"The total is {total}")

# %%
