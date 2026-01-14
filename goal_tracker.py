target = 1000
current_money = 0
months = 0

print("--- Career Goal Tracker ---")

# ციკლი, რომელიც გაგრძელდება მანამ, სანამ 2000-ს არ მივაღწევთ
while current_money < target:
    months = months + 1
    earn = int(input(f"Month {months}: How much did you earn? "))
    current_money = current_money + earn
    
    if current_money >= target:
        print(f"Goal Reached in {months} months!")
    else:
        print(f"Total so far: ${current_money}. Still working...")

print("Success! Now let's upload this to GitHub.")