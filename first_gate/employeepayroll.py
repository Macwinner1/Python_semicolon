
employee_details = {}
list_of_employees = {}
deductions = {}
def employee_tax_calculate(hours, rate, federal, state):
	if hours > 168:
		return "hours above weekly hours"
	elif hours <= 168:
		gross_pay = hours * rate
		federal_due = gross_pay * (federal / 100)
		state_due = gross_pay * (state / 100)
		total_tax = federal_due + state_due
		net_pay = gross_pay - total_tax
		deductions.setdefault('Gross pay', gross_pay)
		deductions.setdefault('Federal withholding Tax', federal_due)
		deductions.setdefault('State withholding tax', state_due)
		deductions.setdefault('Total tax', total_tax)
		deductions.setdefault('Net pay', net_pay)
		list_of_employees.setdefault('Deductions ', []).append(deductions)
		employee_name = {'Employees name': name, 'Hours worked': hours, 'Pay rate': rate, 'Federal withholding Tax': federal, 'State withholding tax': state}
		employee_details.update(employee_name)

		return "deductions successful"
	
	return list_of_employees


	
	
def employee_details(name):
	employee_name = {'Employees name': name, 'Hours worked': hours, 'Pay rate': rate, 'Federal withholding Tax': federal, 'State withholding tax': state}
	employee_details.update(employee_name)
	employee_details.update(employee_tax_calculate(hours, rate, federal, state))
	
	return employee_details
	
	
menu = '''

	Welcome to semicolon Employees Payroll:
	
	1. Add Employees Payroll
	2. View Employees Payroll
	3. Update Employee Payroll
		4. Exit
		
	'''

list_of_employees = {}
employee_details = {}
exit = True
while exit:
	print(menu)
	option = input()
	match option:
		case '1':
			name = input("Enter Employees Name: ")
			hours = int(input("Enter number of hours worked in a week: "))
			rate = float(input("Enter hourly pay rate: "))
			federal = float(input("Enter federal tax withholding rate: "))
			state = float(input("Enter state tax withholding rate: "))
			employee_name = {'Employees name': name, 'Hours worked': hours, 'Pay rate': rate, 'Federal withholding Tax': federal, 'State withholding tax': state}
			employee_details.update(employee_name)
			gross_pay = hours * rate
			federal_due = gross_pay * (federal / 100)
			state_due = gross_pay * (state / 100)
			total_tax = federal_due + state_due
			net_pay = gross_pay - total_tax
			employee_details.update(employee_name)
			employee_details.setdefault('Gross pay', gross_pay)
			employee_details.setdefault('Federal withholding Tax', federal_due)
			employee_details.setdefault('State withholding tax', state_due)
			employee_details.setdefault('Total tax', total_tax)
			employee_details.setdefault('Net pay', net_pay)
			list_of_employees.setdefault('Employees List ', []).append(employee_details)
			print(list_of_employees)
		case '2':
			print(list_of_employees)
			option2 = input("Press((1) Exit): ")
			exit2 = True
			while exit2:
				match option2:
					case '1':
						exit2 = False

			
		case '3':
			#if list_of_employees == list_of_employees
				#return "name exist" 
				
			#else:
				pop(employee_name)
				exit = False
				
		case '4':
			exit = False
