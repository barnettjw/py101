# In this exercise, you will write an xor function that takes two arguments,
# and returns True if exactly one of its arguments is truthy, False otherwise.

# requirements:
    # xor means ONLY 1 operand must be evaluate to True

# function name: xor

# input: 2 values
# output: boolean

#%%
def xor(a, b):
    if bool(a) == True and bool(b) == False: return True
    if bool(a) == False and bool(b) == True: return True
    return False

print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)
# %%
