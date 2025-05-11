number_of_student = int(input("Enter number of students: "))

highest_score = 0
name = " "
count = 0

while count < number_of_student: 
	student_name = input("Enter student name: ")
	score = int(input("Enter student score: "))
	
	if score > highest_score:
		highest_score = score
		name = student_name
	count = count + 1

print("\nthis is the student name: ", name)
print("\nthis is the highest score: ", highest_score)
