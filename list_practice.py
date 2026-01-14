# Inventory Management System
inventory = ["Laptop", "Mouse", "Keyboard", "Monitor"]

print("--- Current Inventory Status ---")
for product in inventory:
    print(f"Product: {product}")

# Adding new data to the list
new_item = "Webcam"
inventory.append(new_item)

print(f"\nUpdate: Added {new_item} to the system.")
print(f"Full Inventory: {inventory}")