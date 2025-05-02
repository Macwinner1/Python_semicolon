amount = float(input("Enter the Principal amount: "))

annualRate = float(input("Enter the annual interest rate: "))

year = float(input("Enter the duration in years: "))

duration = int(year * 12)

monthlyRate = float(annualRate / 1200)

monthlyPow = float((1 + monthlyRate) ** duration)

upperSide = float(amount * (monthlyRate * monthlyPow))

monthly =  upperSide / (monthlyPow - 1)

print(f"Your monthly payment is ${monthly:.2f}")