number_of_student = int(input("Enter number of students: "))

highest_score = 0
highest_score2 = 0
first_name = " "
second_name = " "
count = 0

while count < number_of_student:
	score = int(input("Enter student score: ")) 
	student_name = input("Enter student name: ")

	if score > highest_score2 & score < highest_score:
		highest_score2 = score
		second_name = student_name
		
	if score >= highest_score:
		highest_score2 = highest_score
		second_name = first_name
		first_name = student_name
		highest_score = score

	count = count + 1

print("\nthis is the highest student name: ", first_name)
print("\nthis is the highest score: ", highest_score)

print("\nthis is the second highest student name: ", second_name)
print("\nthis is the second highest score: ", highest_score2)