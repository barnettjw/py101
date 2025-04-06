# Build a program that asks the user to enter the length and width of a room,
# in meters, then prints the room's area in both square meters and square feet.

# Note: 1 square meter == 10.7639 square feet

# input: length and width via keyboard
# output: prints area as square meters and square feet

# algo
# initalize constant SQ_METER_IN_SQ_FT to 10.7639
# Request input from user for room's length and assign the value to the variable length
# Request input from user for room's width and assign the value to the variable width
# convert both length and width from strings to integers using int()
# calculate area in square meters using formula length * width and assign the value to the variable area_sq_m
# calculate area in square feet using the formula area_sq_m * SQ_METER_IN_SQ_FT and store the value in the variable area_sq_ft

#%%
SQ_METER_IN_SQ_FT = 10.7639
length = int(input("Room's length (in meters)"))
width = int(input("Room's width (in meters)"))
area_sq_m = length * width
area_sq_ft = area_sq_m * SQ_METER_IN_SQ_FT
print(f"Area in {area_sq_m} sq meters")
print(f"Area in {round(area_sq_ft,2)} sq ft")
# %%
