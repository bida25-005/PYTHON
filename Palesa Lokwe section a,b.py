# SECTION A: Student Grades

# Ask for the number of students
number_of_students = int(input("Enter the number of students: "))

total = 0
students = []

# Get information for each student
for i in range(number_of_students):

    print("\nStudent", i + 1)

    name = input("Enter student name: ")

    # Check that the grade is between 0 and 100
    while True:
        try:
            grade = float(input("Enter grade (0-100): "))

            if 0 <= grade <= 100:
                break
            else:
                print("Grade must be between 0 and 100.")

        except ValueError:
            print("Please enter a number.")

    # Add grade to total
    total = total + grade

    # Store name and grade
    students.append((name, grade))


# Calculate the class average
average = total / number_of_students


# Display the results
print("\nRESULTS")

print("Class total:", total)
print("Class average:", round(average, 2))

for student in students:

    name = student[0]
    grade = student[1]

    print(
        name,
        "grade:", grade,
        "| Class average:", round(average, 2)
    )

# SECTION B: Multiple Subjects

# Ask for the number of students
number_of_students = int(input("Enter the number of students: "))


# Create a list for subjects
subjects = []

# The assignment requires at least 3 subjects
for i in range(3):

    subject = input("Enter subject " + str(i + 1) + ": ")

    subjects.append(subject)


# Create a list for students
students = []


# Enter student information
for i in range(number_of_students):

    print("\nStudent", i + 1)

    name = input("Enter student name: ")

    # Create a list for this student's grades
    grades = []

    # Get a grade for each subject
    for subject in subjects:

        while True:
            try:
                grade = float(
                    input(
                        "Enter " + subject +
                        " grade (0-100): "
                    )
                )

                if 0 <= grade <= 100:
                    break
                else:
                    print(
                        "Grade must be between 0 and 100."
                    )

            except ValueError:
                print("Please enter a number.")

        grades.append(grade)

    # Store the student as a tuple
    students.append((name, grades))


# ----------------------------------
# Calculate each student's average
# ----------------------------------

print("\nSTUDENT AVERAGES")

for student in students:

    name = student[0]
    grades = student[1]

    average = sum(grades) / len(grades)

    print(
        name,
        "average:",
        round(average, 2)
    )


# ----------------------------------
# Find highest and lowest grades
# ----------------------------------

print("\nHIGHEST AND LOWEST GRADES")

for i in range(len(subjects)):

    subject_grades = []

    # Get all grades for this subject
    for student in students:

        grades = student[1]

        subject_grades.append(grades[i])

    highest = max(subject_grades)
    lowest = min(subject_grades)

    print(
        subjects[i],
        "highest:", highest,
        "lowest:", lowest
    )


# ----------------------------------
# Display summary table
# ----------------------------------

print("\nSUMMARY TABLE")

print("Student", end="")

for subject in subjects:
    print("\t" + subject, end="")

print("\tAverage")


for student in students:

    name = student[0]
    grades = student[1]

    average = sum(grades) / len(grades)

    print(name, end="")

    for grade in grades:
        print("\t" + str(grade), end="")

    print("\t" + str(round(average, 2)))

