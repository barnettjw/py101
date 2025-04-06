# Write a program that asks the user to enter an integer greater than 0,
# then asks whether the user wants to determine the sum or
# the product of all numbers between 1 and the entered integer, inclusive.

### Algo ###
# prompt the user to enter an integer greater than 0 using input() and assign it to num
# prompt the user to enter "s" to comuter the sum or "p" to compute the product and assign it to choice
# get a range of 1 to num + 1 and assign it to numbers

# if s: sum the range and assign it to result
# if p:
    # initalize result to 1
    # for num in numbers result *= num

#%%
num = int(input("Enter an integer greater than 0: "))
choice = input("Ener 's' to compute the sum, or 'p' to compute the product. ")

numbers = range(1, num + 1)
if choice == 's': result = sum(numbers)
if choice == 'p':
    result = 1
    for num in numbers:
        result *= num

print(result)
