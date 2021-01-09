def grade_book():
    print("This is a grade book analyzer.")

    students = int(input("How many students are in the class?"))
    student_grades = dict()
    for x in range(0, students):
        add_student(student_grades)

    for x in student_grades:
        print(len(student_grades))
        while input("Would you like to enter a grade for student " + str(x) + "? (Y/N)").lower() == "y":
            grade_input(x, student_grades)

    answer = input("What would you like to do next?: ")
    if answer == "individual average":
        student = int(input("Which student?: "))
        print(get_average(student, student_grades))
    elif answer == 'overall average':
        print(get_overall_average(student_grades))


def get_average(student, student_grades):
    return sum(student_grades[student]) / len(student_grades[student])


def get_overall_average(student_grades):
    average = 0
    for x in student_grades:
        average += get_average(x, student_grades)
    return average / len(student_grades)


def add_student(student_grades):
    student_grades[len(student_grades) + 1] = []


def grade_input(index, student_grades):
    assignment = 0
    score = int(input("Enter student " + str(index) + "'s assignment score: "))
    if score < 1 or score > 100:
        print("Invalid score. Score range is form 0 to 100.")
    else:
        student_grades[index].append(score)


grade_book()
