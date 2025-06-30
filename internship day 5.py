
def calculate_weighted_gpa(grades: list[tuple[str, float]]) -> float:
    total_weighted_points = 0
    total_credit_hours = 0
    global GPA

    for grade, credit_hour in grades:
        if grade == "A":
            gp = 4.00
        elif grade == "A-":
            gp = 3.67
        elif grade == "B+":
            gp = 3.33
        elif grade == "B":
            gp = 3.00
        elif grade == "B-":
            gp = 2.67
        elif grade == "C+":
            gp = 2.33
        elif grade == "C":
            gp = 2.00
        elif grade == "D":
            gp = 1.00
        else:
            gp = 0.00
            print("You are failed")
       
        total_weighted_points += gp * credit_hour
        total_credit_hours += credit_hour

    GPA = round(total_weighted_points / total_credit_hours, 2)
    return GPA


def print_gpa_summary():
    global GPA
    name = input("Enter your name : ")
    print(f"Student Name : {name} has GPA {GPA}: ")



calculate_weighted_gpa([ ("A-",2),("B+",3),("B+",3),("B-",3),("A-",3),("B",3),("B",1) ])
print_gpa_summary()




