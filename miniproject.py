def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def main():
    print("===== Student Grade Calculator =====")

    name = input("Enter student name: ")

    subjects = ["Python", "Mathematics", "Science", "English", "Computer"]

    marks = []

    for subject in subjects:
        while True:
            try:
                mark = float(input(f"Enter marks for {subject} (0-100): "))

                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Please enter marks between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

    total = sum(marks)
    percentage = total / len(subjects)
    grade = calculate_grade(percentage)

    if percentage >= 40:
        result = "Pass"
    else:
        result = "Fail"

    print("\n===== Result =====")
    print("Student Name:", name)
    print("Total Marks:", total, "/", len(subjects) * 100)
    print("Percentage:", round(percentage, 2), "%")
    print("Grade:", grade)
    print("Result:", result)


if __name__ == "__main__":
    main()
