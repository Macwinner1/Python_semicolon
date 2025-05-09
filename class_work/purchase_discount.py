purchase_amount = float(input("Enter the amount you purchase for discount: "))

five_percent = float(0.05)
ten_percent = float(0.10)
twenty_percent = float(0.20)
discount = 0

if purchase_amount < 1000:
	print("Your don't get any discount on this purchase!!")
else:

	if purchase_amount >= 1000 or purchase_amount <= 10000:
		value = float(purchase_amount * five_percent)
		discount = float(purchase_amount - value)
		print(f"Wow you have a discount of {discount:,.2f} on your purchase")


	elif purchase_amount > 10000 or purchase_amount <= 50000:
		value = float(purchase_amount * ten_percent)
		discount = float(purchase_amount - value)
		print(f"Wow you have a discount of {discount:,.2f} on your purchase")


	elif purchase_amount > 50001:
		value = float(purchase_amount * twenty_percent)
		discount = float(purchase_amount - value)
		print(f"Wow you have a discount of {discount:,.2f} on your purchase")


