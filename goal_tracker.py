# Monthly Progress Tracker
target = 1000
current_money = 0
months = 0

print("--- Monthly Income Progress Tracker ---")

while current_money < target:
    months += 1
    try:
        earn = int(input(f"Enter earnings for month {months}: "))
        current_money += earn
        
        if current_money >= target:
            print(f"Goal Reached! Total earned in {months} months: ${current_money}")
        else:
            remaining = target - current_money
            print(f"Total so far: ${current_money}. You need ${remaining} more.")
    except ValueError:
        print("Error: Please enter a valid number.")