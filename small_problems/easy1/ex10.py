# Write a function that computes the sum of all numbers between 1 and 
# some other number, inclusive, that are multiples of 3 or 5.

# For instance, if the supplied number is 20, 
# the result should be 98 (3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 + 20).

# requirements:
    # integer will be greater than 1

# input: integer greather than 1
# output: integer

# function name: multisum

# compute the range between 1 and num and assign it to numbers
# for each num in numbers, if num % 3 == 0 or num % 5 == 0
# sum the list using sum()

#%%

def multisum(num):
    numbers = range(1, num + 1)
    return sum([num for num in numbers 
                if num % 3 == 0 or num % 5 == 0])

# These examples should all print True
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)
# %%
