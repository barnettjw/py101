# Create a function that takes 2 arguments, a list and a dictionary.

# The list will contain 2 or more elements that, 
    # when joined with spaces, will produce a person's name. 
# The dictionary will contain two keys, "title" and "occupation", and the appropriate values. 
# Your function should return a greeting that uses the person's full name, 
    # and mentions the person's title.

# input: list and dictionary
# output: string

# function name: greeting

### algo ###
# concatentate name and assign it to name
# use an f-string to create the greeting

# %%
def greetings(full_name_list, job):
    name = ' '.join(full_name_list)
    greeting = f"Hello, {name}! Nice to have a {job['title']} {job['occupation']} around."
    return greeting


greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.
# %%
