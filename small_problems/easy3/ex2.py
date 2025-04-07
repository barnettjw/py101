# Write a function that takes a string argument and
    # returns a new string that contains the value of the original string with
    # all consecutive duplicate characters collapsed into a single character.

# function name: crunch

# input: string
# output: string

# requirements:
    # must support empty string

### algo ###
    # calculate the length of the string
    # if length is 0 or 1, return string
    # for i in a range of the length of string
        # if i is 0, initalize result to string[0]
        # else if string[i - 1] != string[i]:
            # result += string[i]

#%%
def crunch(string):
    length = len(string)
    if length == 0 or length == 1: return string

    for i in range(length):
        if i == 0: result = string[0] 
        elif string[i - 1] != string[i]:
            result += string[i]
    
    return result

#%%
# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')
# %%
