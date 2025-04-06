# Write a function that returns the next to last word in the string argument.

# function name: penultimate
# input: string
# output: string

# requirements:
    # words are any sequence of non-blank characters
    # input string will contain 2 or more words

#%%
def penultimate(string):
    return string.split(' ')[-2]

# These examples should print True
print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")
# %%
