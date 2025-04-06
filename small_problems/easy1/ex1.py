# Write a function that takes one integer argument and
# returns True when the number's absolute value is odd, False otherwise.

# input: int
# output: boolean

# algo
# define function named odd, it should accept 1 parameter, named num
# assign num the absolute value of num
# if num mod 2 is not equal to 0 return True, else return False

#%%
def odd(num):
    num = abs(num)
    return True if num % 2 != 0 else False

print(odd(-3))
print(odd(5))
print(odd(0))
print(odd(2))
print(odd(-4))
# %%
