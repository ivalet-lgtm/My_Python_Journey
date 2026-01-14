# Professional File Reading System
file_path = "d:/Python_Project/data.txt"

print("--- Reading External Data ---")

try:
    with open(file_path, "r") as file:
        content = file.read().strip()
        
        if not content:
            print("Notice: The file is empty.")
        else:
            print("Content found:")
            print("-" * 20)
            print(content)
            print("-" * 20)

except FileNotFoundError:
    print(f"Error: Could not find the file at {file_path}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")