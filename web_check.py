import requests

# The URL we want to check
target_url = "https://api.github.com"

print(f"--- Testing Connection to: {target_url} ---")

try:
    # Sending a GET request to the website
    response = requests.get(target_url)
    
    # 200 is the HTTP standard for 'Everything is OK'
    if response.status_code == 200:
        print("Success! The website is reachable.")
        print(f"Server info: {response.headers['Server']}")
    else:
        print(f"Warning: Website returned status code {response.status_code}")

except requests.exceptions.ConnectionError:
    print("Error: Could not connect to the internet. Please check your connection.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")