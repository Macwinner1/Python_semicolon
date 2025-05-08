principal = int(input("Enter amount here: "))
annual_rate = 0.07
years = int(input("Enter years here: "))

amount = principal * (1 + annual_rate) ** years

print(f"${amount:.2f} on the deposit at the end of the {years} years")