dollar_amount = int(input("Enter price in dollar : "))
cent_amount = int(input("Enter price in cents : "))

quarters = 25
dimes = 10
pennies = 1

dollar_amount = dollar_amount * 100
change_amount = dollar_amount - cent_amount
quarter = change_amount // quarters
dime =  change_amount % quarters // dimes
pennie = change_amount % quarters % dimes // pennies

print(f"your amount {dollar_amount} consists of")
print(f" {cent_amount} cents")
print(f" {quarter} quarters")
print(f" {dime} dimes")
	
print(f" {pennie} pennies")

	