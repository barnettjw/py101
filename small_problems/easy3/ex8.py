# Write a function that determines the mean (average) of the three scores
# passed to it, and returns the letter associated with that grade.

# requirements:
# scores are integers between 0 up to 100
# grades
# 90 <= score <= 100: 'A'
# 80 <= score < 90: 'B'
# 70 <= score < 80: 'C'
# 60 <= score < 70: 'D'
# 0 <= score < 60: 'F'

# function name: get_grade
# input: list
# output: string


# %%
def get_grade(score1, score2, score3):
    avg = (score1 + score2 + score3) / 3

    if avg >= 90:
        grade = "A"
    elif avg >= 80:
        grade = "B"
    elif avg >= 70:
        grade = "C"
    elif avg >= 60:
        grade = "D"
    else:
        grade = "F"

    return grade


# %%
print(get_grade(95, 90, 93) == "A")  # True
print(get_grade(50, 50, 95) == "D")  # True
# %%
