# Write a function that returns the number provided as an argument
# multiplied by two, unless the argument is a double number.
# If the argument is a double number, return the double number as-is.

# requirements
# A double number is an even-length number
# whose left-side digits are exactly the same as its right-side digits.

# function name = twice
# input: integer
# output: integer

### algo

# convert num to string as assing it to digits
# check if the length of the number is even (use % 2)
# if not even: return num * 2

# if even:
# calc half way point
# calc left-side 0:half
# calc right-side half+1:

# if left-side is equal to right-side return number
# else retunr num * 2


# %%
def twice(num):
    digits = str(num)
    if len(digits) % 2 != 0:
        return num * 2

    half = len(digits) // 2
    left_half = digits[0:half]
    right_half = digits[half:]

    return num if left_half == right_half else num * 2


# %%

print(twice(37) == 74)  # True
print(twice(44) == 44)  # True
print(twice(334433) == 668866)  # True
print(twice(444) == 888)  # True
print(twice(107) == 214)  # True
print(twice(103103) == 103103)  # True
print(twice(3333) == 3333)  # True
print(twice(7676) == 7676)  # True
