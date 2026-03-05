high_income = False
good_credit = True
student = True

if high_income and good_credit:
    print("Eligible")
else:
    print("Not eligible")
# Eligible if both variables satisfy the condition


if high_income or good_credit:
    print("Eligible")
else:
    print("Not eligible")
# Eligible if one of two variables satisfy the condition

if not student:
    print("Eligible")
else:
    print("Not eligible")
# If the variable is true, the "not" operator inverts it to false


if (high_income or good_credit) and not student:
    print("Eligible")
else:
    print("Not eligible")
# Student is eligible if he has HI or GC and is not a student.


# Chaining comparison operators
# Rule: Age should be between 18 and 65
age = 22
if 18 <= age < 65:
    print("Eligible")

if 10 == "10":
    print("a")
elif "bag" > "apple" and "bag" > "cat":
    print("b")
else:
    print("c")
