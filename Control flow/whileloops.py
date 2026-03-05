# number = 100
# while number > 0:
#     print(number)
#     number = number // 2
#     # number //= 2

# command = ''
# while command.lower() != "quit":
#     command = input('>')
#     print("ECHO", command)
count = 0
for number in range(1, 15):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"We have {count} even numbers")
