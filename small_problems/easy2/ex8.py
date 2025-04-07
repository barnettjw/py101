# Write a function that returns a list that contains 
    # every other element of a list that is passed in as an argument.

# function title: oddities
# input: list
# output: list

# requirements:
    # support an empty list

### algo ###
# iterate through the list using a range
# if num is not even then add num to list

#%%
def oddities(lst):
    return [lst[num] for num in range(len(lst)) 
            if num % 2 == 0]

#%%
print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True
        

# Bonus question: Try to solve the problem using list slicing.

# %%
def oddities(lst):
    return lst[::2]

#%%
print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True
# %%

# Further Exploration: Write a companion function that returns 
    # the 2nd, 4th, 6th, and so on elements of a list.

# %%
def evens(lst):
    return lst[1::2]

#%%
print(evens([2, 3, 4, 5, 6]))
print(evens([1, 2, 3, 4]))
print(evens(["abc", "def"]))
print(evens([123]))
print(evens([]) ) 
