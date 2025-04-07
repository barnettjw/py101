# Build a program that displays when the user will retire and
    # how many years she has to work till retirement.

### algo ###
# prompt user "What is your age?" and assign to age
# prompt user "At what age would you like to retire?" and assign to retirement_age

# get current year by using the today() from the datetime module
    # and getting the year property and assign it to current_year
# calculate years til retirement using formula retirment_age - age and assign in years_til_retirement
# calculate retirement year using formula current_year + years_til_retirement

#%%
import datetime
current_year = datetime.date.today().year

age = int(input("What is your age? "))
retirement_age = int(input("At what age would you like to retire?"))

years_til_retirment = retirement_age - age
retirement_year = current_year + years_til_retirment

print(f"It's {current_year}. You will retire in {retirement_year}.")
print(f"You have only {years_til_retirment} years of work to go!")
# %%
