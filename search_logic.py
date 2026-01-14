# Inventory Search System
stock = ["Laptop", "Mouse", "Keyboard", "Monitor", "Webcam"]

print("--- Inventory Search Tool ---")

# We use .strip() to remove extra spaces and .capitalize() to match our list
query = input("Enter the item name you are looking for: ").strip().capitalize()

if query in stock:
    print(f"Result: Yes, we have '{query}' in our warehouse.")
else:
    print(f"Result: Sorry, '{query}' is currently out of stock.")