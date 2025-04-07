# Write a function that takes one argument, a positive integer,
    # and returns a string of alternating '1's and '0's,
    # always starting with a '1'. 

# function name: stringy

# input: integer
# output: string

# requirements:
    # integer must be greater than 0
    # string's length must equal integer
    # must always start with 1

#%%
def stringy(num):
    result = ''
    for i in range(num):
        result += "1" if i % 2 == 0 else "0"
    return result

print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True
# %%
