print("===== ONLINE FOOD ORDERING SYSTEM =====")

# Menu prices
pizza = 200
burger = 120
sandwich = 80
juice = 50

# Predefined orders (instead of user input)
item1 = "Pizza"
item2 = "Juice"

total = 0

print("\nMENU")
print("Pizza      = ₹200")
print("Burger     = ₹120")
print("Sandwich   = ₹80")
print("Juice      = ₹50")

print("\nSelected Items:")
print(item1)
print(item2)

# Calculate total
if item1 == "Pizza":
    total += pizza
elif item1 == "Burger":
    total += burger
elif item1 == "Sandwich":
    total += sandwich
elif item1 == "Juice":
    total += juice

if item2 == "Pizza":
    total += pizza
elif item2 == "Burger":
    total += burger
elif item2 == "Sandwich":
    total += sandwich
elif item2 == "Juice":
    total += juice

print("\nTotal Amount = ₹", total)

print("Order placed successfully")
print("CI Pipeline Executed Successfully")