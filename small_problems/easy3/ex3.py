# Write a function that takes a short line of text and prints it within a box.

# function name: print_in_box

# input: string
# output: string

# requirements:
    # minimum width 2 spaces
    # minimu height 3 lines

### algo ###
# get length of string and assign to length
# border: '+-' repeating dashes equal to length '-+'
# spacer: '| ' spaces equal to length ' |'
# string: '| ' string ' |'

#%%
def print_in_box(string):
    border   = f"+-{'-' * len(string)}-+"
    spacer   = f"| {' ' * len(string)} |"

    print(border )
    print(spacer)
    print(f"| {string} |")
    print(spacer)
    print(border )

print_in_box('')
#%%
print_in_box('To boldly go where no one has gone before.')