# Write a function that takes two strings as arguments,
# determines the length of the two strings,
# and then returns the result of concatenating the shorter string,
# the longer string, and the shorter string once again.
# You may assume that the strings are of different lengths.

# input: 2 strings
# output: concatenated string

# function name: short_long_short
# reqirements:
    # must support empty strings
    # assume strings of different lengths

### algo ###

# compare the 2 strings using len()
# if the length of first > the length of second
    # set first to longest and second to shortest
# else second to longest and first to shortest
# concatanate the strings

#%%
def short_long_short(first, second):
    if len(first) > len(second):
        longest = first
        shortest = second
    else:
        longest = second
        shortest = first

    return shortest + longest + shortest

# These examples should all print True
print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")
# %%
