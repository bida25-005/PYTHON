# SECTION C: Introduction of Dictionaries

# Create an empty dictionary
students = {}


# ----------------------------------
# 1. ADD A NEW STUDENT
# ----------------------------------

def add_student():

    name = input("Enter student name: ")

    if name in students:
        print("Student already exists.")
        return

    # Create a dictionary for this student
    students[name] = {}

    number_of_subjects = int(
        input("How many subjects? ")
    )

    for i in range(number_of_subjects):

        subject = input("Enter subject name: ")

        grade = float(
            input("Enter grade: ")
        )

        # Store the grade in a list
        students[name][subject] = [grade]

    print("Student added successfully.")


# ----------------------------------
# 2. UPDATE A STUDENT'S GRADES
# ----------------------------------

def update_student():

    name = input("Enter student name: ")

    if name not in students:
        print("Student not found.")
        return

    subject = input("Enter subject to update: ")

    if subject not in students[name]:
        print("Subject not found.")
        return

    grade = float(
        input("Enter new grade: ")
    )

    # Add the new grade to the list
    students[name][subject].append(grade)

    print("Grade updated successfully.")


# ----------------------------------
# 3. REMOVE A STUDENT
# ----------------------------------

def remove_student():

    name = input(
        "Enter student name to remove: "
    )

    if name in students:

        del students[name]

        print("Student removed successfully.")

    else:

        print("Student not found.")


# ----------------------------------
# 4. VIEW GRADES FOR A SUBJECT
# ----------------------------------

def view_subject():

    subject = input(
        "Enter subject name: "
    )

    print("\nGrades for", subject)

    found = False

    for name in students:

        if subject in students[name]:

            print(
                name,
                ":",
                students[name][subject]
            )

            found = True

    if found == False:

        print(
            "No grades found for this subject."
        )


# ----------------------------------
# 5. SEARCH FOR A STUDENT
# ----------------------------------

def search_student():

    name = input(
        "Enter student name to search: "
    )

    if name not in students:

        print("Student not found.")
        return

    print("\nStudent:", name)

    total = 0
    number_of_grades = 0

    # Display subjects and grades
    for subject in students[name]:

        grades = students[name][subject]

        print(
            subject,
            ":",
            grades
        )

        # Add all grades
        for grade in grades:

            total = total + grade

            number_of_grades = (
                number_of_grades + 1
            )

    # Calculate average
    if number_of_grades > 0:

        average = (
            total / number_of_grades
        )

        print(
            "Average:",
            round(average, 2)
        )


# ----------------------------------
# MAIN MENU
# ----------------------------------

while True:

    print("\n===== STUDENT MANAGEMENT =====")

    print("1. Add a new student")
    print("2. Update student's grades")
    print("3. Remove a student")
    print("4. View grades for a subject")
    print("5. Search for a student")
    print("6. Exit")

    choice = input(
        "Enter your choice: "
    )

    if choice == "1":

        add_student()

    elif choice == "2":

        update_student()

    elif choice == "3":

        remove_student()

    elif choice == "4":

        view_subject()

    elif choice == "5":

        search_student()

    elif choice == "6":

        print("Program ended.")
        break

    else:

        print(
            "Invalid choice. Please choose 1-6."
        )