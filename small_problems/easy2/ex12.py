# Write a function that takes a number as an argument.
# If the argument is a positive number,
    # return the negative of that number.
# If the argument is a negative number, return it as-is.

# function name: negative

# input: integer
# output: integer

### algo ###
# get the absolute value of num
# mutliply it by -1

#%%
def negative(num):
    return abs(num) * -1

print(negative(5) == -5)      # True
print(negative(-3) == -3)     # True
print(negative(0) == 0)       # True
# %%
