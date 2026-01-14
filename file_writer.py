# Interactive File Writing System
file_path = "d:/Python_Project/data.txt"

print("--- Data Entry System ---")

user_input = input("Enter the text you want to save to the file: ")

try:
    with open(file_path, "a") as file:
        # We add \n to ensure the new text starts on a new line
        file.write(f"\n{user_input}")
        print("Success: Data has been securely saved.")

except Exception as e:
    print(f"Error: Unable to write to file. Details: {e}")