# Write a function that takes a non-empty string argument
    # and returns the middle character(s) of the string.

# requirements:
    # if odd length: return 1 character
    # if even length: return 2 characters

# input: string
# output: string

# function name: center_off

### algo ###
# get length of string and assign it to length
# calculate middle using the formula length // 2 and assign it to middle_index
# if length % 2 is not 0 then assign string[middle_index] to middle
# else calculate middle by string[middle_index:(middle_index + 1)]
    # then join middle into a string

#%%
def center_of(string):
    length = len(string)
    middle_index = length // 2
    
    if length % 2 != 0: return string[middle_index]
    else:
        even_middle = string[(middle_index - 1):(middle_index +1 )]
        return ''.join(even_middle)
#%%
print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True


# %%
