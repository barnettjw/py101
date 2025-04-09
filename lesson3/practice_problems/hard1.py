# %%

# 1.


# %%
def first():
    return {
        "prop1": "hi there",
    }


# %%
def second():
    return
    {
        "prop1": "hi there",
    }


print(first())  # prints the dictionary
print(second())  # prints None
# %%

# 2.

dictionary = {"first": [1]}
num_list = dictionary["first"]
num_list.append(2)

print(num_list)  # prints [1, 2]
print(dictionary)  # prints {'first': [1, 2]}
# %%

# 3.

# TODO

# %%

# 4.


def is_an_ip_number(str):
    if str.isdigit():
        number = int(str)
        return 0 <= number <= 255
    return False


def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")
    if len(dot_separated_words) != 4:
        return False

    while len(dot_separated_words) > 0:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            return False
    return True


# %%

# 5.

if False:
    greeting = "hello world"

print(greeting)  # raises a NameError
