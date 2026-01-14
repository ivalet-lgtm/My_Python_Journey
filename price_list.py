# Product Pricing Database
product_prices = {
    "Laptop": 1200,
    "Mouse": 25,
    "Keyboard": 50,
    "Monitor": 200
}

search_query = input("Enter product name to check price: ")

if search_query in product_prices:
    price = product_prices[search_query]
    print(f"The price of {search_query} is ${price}.")
else:
    print(f"Sorry, '{search_query}' is not in our price list.")