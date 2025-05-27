menu = """
	TO_DO_LIST MANGER

	1. Add a task
	2. View all tasks
	3. Mark a task as complete
	4. Delete a task
	0. Exit
	"""
exit = True
list_of_task = []
while exit:
	print(menu)
	option = input("Enter your choice: ")
	match option:
		case "1":
			back = True
			while back:
				print("Add a task")
				option_input = input("Enter the Task: ")
				list_of_task.append(option_input)
				print("Task added!")
				pin = input("Enter 0 to move back <- and 1 to keep adding Task: ")
				if pin == 0 or pin == "0":
					back = False
				if pin == 1 or pin == "1":
					back = True
		case "2":
			back = True
			while back:
				print("View all tasks")
				for index, value in enumerate(list_of_task):
					print(index, value)
				if list_of_task == []:
					print("Your task list is empty")
				pin = input("Enter 0 to move back <- and 1 to keep adding Task: ")
				if pin == 0 or pin == "0":
					back = False
				if pin == 1 or pin == "1":
					back = True
		case "3":
			print("Mark a task as complete")
			for index, value in enumerate(list_of_task):
				print(index, value)
				mark_input = input("Enter task number: ")
				if mark_input >= 0:
					list_of_task(index).append("mark_input")
			
		case "4":
			back = True
			while back:
				print("Delete a task")
				for index, value in enumerate(list_of_task):
					print(index, value)
				if list_of_task == []:
					print("Your task list is empty")
					pin = input("Enter 0 to move back <-")
					if pin == 0 or pin == "0":
						back = False
				else: 
					delete_input = int(input("Enter number of the Task: "))
					list_of_task.pop(delete_input)
					pin = input("Enter 0 to move back <- and 1 to keep adding Task: ")
					if pin == 0 or pin == "0":
						back = False
					if pin == 1 or pin == "1":
						back = True
			
		case "0":
			exit = False