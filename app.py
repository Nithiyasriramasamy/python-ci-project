print("===== ONLINE FOOD ORDERING SYSTEM =====")

# Food Menu
pizza = 200
burger = 120
sandwich = 80
juice = 50

total = 0

print("\nMENU")
print("1. Pizza      = ₹200")
print("2. Burger     = ₹120")
print("3. Sandwich   = ₹80")
print("4. Juice      = ₹50")

# User Order
item1 = input("\nEnter food item name: ")

if item1 == "Pizza":
    total += pizza
elif item1 == "Burger":
    total += burger
elif item1 == "Sandwich":
    total += sandwich
elif item1 == "Juice":
    total += juice
else:
    print("Item not available")

another_order = input("Do you want another item? (yes/no): ")

if another_order == "yes":
    item2 = input("Enter second item name: ")

    if item2 == "Pizza":
        total += pizza
    elif item2 == "Burger":
        total += burger
    elif item2 == "Sandwich":
        total += sandwich
    elif item2 == "Juice":
        total += juice
    else:
        print("Item not available")

print("\nTotal amount to pay = ₹", total)

print("Order placed successfully")
print("Thank you for using Online Food Ordering System")