def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome aboard")


greet("Elmedin", "Hodzic")
greet("John", "Smith")

# Two types of functions
# 1 - Perform a task
# 2 - Return a value


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Elmedin")

print(message)


def increment(number, by):
    return number + by


print(increment(2, 1))

# Using default parameters


def increment2(number, by=1):
    return number + by


print(increment2(2))


def multiply(*numbers):
    print(numbers)


multiply(2, 3, 4, 5)
