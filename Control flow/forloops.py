# for number in range(1, 10, 2):
#     print("Attempt", number, number * ".")


# FOR ELSE LOOPS
# successful = False
# for number in range(3):
#     print("Attempt")
#     if successful:
#         print("Successful")
#         break
# else:
#     print("Attempted 3 times and failed")


# # Nested loops

# for x in range(5):
#     for y in range(3):
#         print(f"({x}, {y})")

# Iterables

for x in [1, 2, 3, 4]:
    print(x)

# Practice challenges given by AI
shopping_cart = [
    {"product": "Laptop", "price": 1200.00, "quantity": 1, "in_stock": True},
    {"product": "Wireless Mouse", "price": 25.50, "quantity": 2, "in_stock": True},
    {"product": "Desk Monitor", "price": 300.00, "quantity": 1, "in_stock": False},
    {"product": "HDMI Cable", "price": 15.00, "quantity": 3, "in_stock": True}
]

for item in shopping_cart:
    if item["in_stock"]:
        print(f"Ordering {item["product"]}")
    else:
        print(f"Exception {item["product"]} not in shopping cart")

total_cost = 0
for item in shopping_cart:
    total_cost += item['price'] * item['quantity']

print(f"To Pay: {total_cost}")
