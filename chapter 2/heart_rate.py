age = int(input("Enter your age: "))
heart_rate = 220 - age

low_end = heart_rate * 0.5
high_end = heart_rate * 0.85

print(f"{age} years old Target Heart Rate would be {low_end} - {high_end}")