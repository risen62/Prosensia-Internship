def grading(score):
    if score < 0 or score > 100:
        return "Invalid Score"
    if score >= 90:
        return "A"
    elif score >= 85:
        return "A-"
    elif score >= 80:
        return "B+"
    elif score >= 75:
        return "B"
    elif score >= 70:
        return "B-"
    elif score >= 65:
        return "C+"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"

def print_grade_summary(student_name, score, grade):
    print(f"Student {student_name} scored {score:.1f} → Grade: {grade}")

def main():
    student_name = input("Enter your name: ")
    try:
        score_input = float(input("How many marks did you get? "))
        if 0 <= score_input <= 100:
            grade_result = grading(score_input)
            print_grade_summary(student_name, score_input, grade_result)
        else:
            print("Invalid input: Score must be between 0 and 100.")
    except ValueError:
        print("Invalid input: Please enter a valid number.")

main()
