# Print all odd numbers from 1 to 99, inclusive, with each number on a separate line.

# algo
# for each num in the range 1 to 100
# if num mod 2 is not equal to 0
# print num

#%%
for num in range(1,100):
    if num % 2 != 0: print(num)
# %%

# Bonus Question: Can you solve the problem by iterating over just the odd numbers?

# algo
# for each num in the range 1 to 100, step 2
# print num

#%%
for num in range(1,100, 2):
    print(num)
# %%
