investment_amount = float(input("Enter your investment amount: "))
years = int(input("Enter years: "))
interest_rate = float(input("Enter your interest rate: ")) / 100
result = 0
for index in range(1, years + 1):
	
	for index2 in range(1):
		result = investment_amount * interest_rate
		investment_amount = result + investment_amount
		print(f"year {index} => {investment_amount:,.2f}")

