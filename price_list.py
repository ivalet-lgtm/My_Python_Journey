# ლექსიკონი: გასაღები (ნივთი) და მნიშვნელობა (ფასი)
products = {
    "Laptop": 1200,
    "Mouse": 25,
    "Keyboard": 50,
    "Monitor": 200
}

# გამოვიტანოთ ფასი კონკრეტული ნივთისთვის
item = input("Enter product name to see price: ")

if item in products:
    # products[item] ამოიღებს შესაბამის ფასს
    print(f"The price of {item} is ${products[item]}")
else:
    print("Product not found.")