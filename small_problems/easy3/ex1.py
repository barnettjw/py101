# Write a function that takes two arguments, a string and a positive integer,
    # then prints the string as many times as the integer indicates.

# function name: repeat

# input: string and integer
# output: prints string

#%%
def repeat(string, num):
    for _ in range(num):
        print(string)

repeat('Hello', 3)
# %%
