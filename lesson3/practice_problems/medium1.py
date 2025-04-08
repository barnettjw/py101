# %%

# 1.

for i in range(1, 11):
    print(f"{'-' * i}The Flintstones Rock!")

# -The Flintstones Rock!
# --The Flintstones Rock!
# ---The Flintstones Rock!
# %%

# 2.


def factors(number):
    divisor = number
    result = []
    while divisor > 0:
        if number % divisor == 0:
            result.append(number // divisor)
        divisor -= 1
    return result


print(factors(-15))
# %%

# 2. bonus question
# number % divisor == 0 Checks if a number is divisible by a divisor with no remainder
# %%
# 3.


def add_to_rolling_buffer1(buffer, max_buffer_size, new_element):
    buffer.append(new_element)
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer


# we are mutating the object 'buffer' that is passed in as an argument


# %%
def add_to_rolling_buffer2(buffer, max_buffer_size, new_element):
    buffer = buffer + [new_element]
    if len(buffer) > max_buffer_size:
        buffer.pop(0)
    return buffer


# we are taking object buffer passed in and adding another list and
# and assigning that to a new local variable named buffer

# %%

# 4.

print(0.3 + 0.6)  # prints 0.89 repeating
print(0.3 + 0.6 == 0.9)  # prints False
# %%

# 5.

nan_value = float("nan")
print(nan_value == float("nan"))  # prints False
# %%
import math

print(math.isnan(nan_value))
# %%

# 6.

answer = 42


def mess_with_it(some_number):
    return some_number + 8


new_answer = mess_with_it(answer)

print(answer - 8)  # prints 34
# %%

# 7.

munsters = {
    "Herman": {"age": 32, "gender": "male"},
    "Lily": {"age": 30, "gender": "female"},
    "Grandpa": {"age": 402, "gender": "male"},
    "Eddie": {"age": 10, "gender": "male"},
    "Marilyn": {"age": 23, "gender": "female"},
}


def mess_with_demographics(demo_dict):
    for key, value in demo_dict.items():
        value["age"] += 42
        value["gender"] = "other"


mess_with_demographics(munsters)
print(munsters)
# This will modify the dictionary because when a mutable object is passed into
# A function any updates to the object mutate the original object
# %%

# 8.


def rps(fist1, fist2):
    if fist1 == "rock":
        return "paper" if fist2 == "paper" else "rock"
    elif fist1 == "paper":
        return "scissors" if fist2 == "scissors" else "paper"
    else:
        return "rock" if fist2 == "rock" else "scissors"


print(rps(rps(rps("rock", "paper"), rps("rock", "scissors")), "rock"))

# %%

# 9.


def foo(param="no"):
    return "yes"


def bar(param="no"):
    return (param == "no") and (foo() or "no")


bar(foo())  # returns False

# 10.

a = 42
b = 42
c = a

print(id(a) == id(b) == id(c))  # Prints True, due to interning
