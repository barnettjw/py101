# Given a string that consists of some words and an assortment of
# non-alphabetic characters, write a function that returns that string with all
# of the non-alphabetic characters replaced by spaces.
#
# If one or more non-alphabetic characters occur in a row,
# you should only have one space in the result
# (i.e., the result string should never have consecutive spaces).

### algo
# init results to an empty string
# for index in length of string
# current_char is string[index]
# if current_char is alpha add it to results
# else
# if last character in results is not a space,
# add a space to results


# %%
def clean_up(string):
    results = ""

    for char in string:
        if char.isalpha():
            results += char
        else:
            if results == "" or results[-1] != " ":
                results += " "
    return results


print(clean_up("---what's my +*& line?"))
print(clean_up("---what's my +*& line?") == " what s my line ")

# %%
