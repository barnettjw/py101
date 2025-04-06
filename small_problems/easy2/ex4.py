# Using the multiply function from the "Multiplying Two Numbers" exercise,
    # write a function that computes the square of its argument
    # (the square is the result of multiplying a number by itself).

# function name: square
# input: integer
# output: integer

#%%
def multiply(a, b):
    return a * b

def square(num):
    return multiply(num, num)

print(square(5) == 25)   # True
print(square(-8) == 64)  # True
# %%
