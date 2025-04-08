#%%
# 1.
numbers = [1, 2, 3, 4]
numbers.clear()
print(numbers)
# %%

# 2.

print([1, 2, 3] + [4, 5])
# [1,2,3,4,5]
# %%

# 3.

str1 = "hello there"
str2 = str1
str2 = "goodbye!"
print(str1) # prints hello there
# %%

# 4.

my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2 = my_list1.copy()
my_list2[0]['first'] = 42
print(my_list1) # prints [{"first": 42}, {"second": "value2"}, 3, 4, 5]
# %%

# 5.

def is_color_valid(color):
    return color == "blue" or color == "green"

def is_color_valid(color):
    return color in ["blue", "green"]