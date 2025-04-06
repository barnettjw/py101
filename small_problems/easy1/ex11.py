# Write a function that determines and 
#   returns the UTF-16 string value of a string passed in as an argument. 
# The UTF-16 string value is the sum of the UTF-16 values of every character in the string.

# function name: utf16_value
# input: string
# output: integer

# requirements
    # use ord() to get the value of a utf-16 char

### algo ###

# char in string get char value using ord
# sum values using sum

#%%
def utf16_value(string):
    return sum([ord(char) for char in string])

#%%
# These examples should all print True
print(utf16_value('Four score') == 984)
print(utf16_value('Launch School') == 1251)
print(utf16_value('a') == 97)
print(utf16_value('') == 0)
# %%
# The next three lines demonstrate that the code
# works with non-ASCII characters from the UTF-16
# character set.
OMEGA = "\u03A9"              # UTF-16 character 'Ω' (omega)
print(utf16_value(OMEGA) == 937)
print(utf16_value(OMEGA + OMEGA + OMEGA) == 2811)
# %%
