# Write a function that takes a positive integer, n,
    # as an argument and prints a right triangle whose sides each have n stars.

#%%
def triangle(n):
    for i in range(1,n+1):
        string = '*' * i
        print(string.rjust(n,' '))


triangle(5)
triangle(9)
# %%
