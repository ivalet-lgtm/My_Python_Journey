# პროდუქტების სია (List)
products = ["Laptop", "Mouse", "Keyboard", "Monitor"]

print("--- My Shop Inventory ---")

# გამოვიტანოთ თითოეული პროდუქტი სათითაოდ
for item in products:
    print("Product available: " + item)

# დავამატოთ ახალი პროდუქტი სიაში
products.append("Webcam")
print("\nAfter adding one more:")
print(products)