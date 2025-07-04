def read_marks_file() -> dict:

    while True:
        try:
            path = input("Enter the path of the file: ")
            with open(path, 'r') as file:
                lines = file.readlines()
            break  
        except FileNotFoundError:
            print(" File not found. Please try again.")

    marks_dict = {}
    skipped_count = 0

    for line in lines:
        line = line.strip()
        if not line:
            continue 

        parts = line.split(",")
        if len(parts) != 2:
            skipped_count += 1
            continue

        name = parts[0].strip()
        mark_str = parts[1].strip()

        if mark_str == "":
            skipped_count += 1
            continue

        try:
            mark = int(mark_str)
            marks_dict[name] = mark
        except ValueError:
            skipped_count += 1

    return marks_dict, skipped_count


def print_summary(marks_dict: dict, skipped_count: int):
    """
    Prints student marks, calculates and displays average.
    Handles empty data gracefully.
    """
    print("\n Student Marks Summary:")
    
    if not marks_dict:
        print(" No valid entries found in the file.")
    else:
        total = 0
        count = 0
        for student, mark in marks_dict.items():
            print(f"{student} → {mark}")
            total += mark
            count += 1

        try:
            average = total / count
            print(f"\n Average: {average:.2f}")
        except ZeroDivisionError:
            print(" No valid marks to calculate average.")

    print(f"\n Skipped {skipped_count} invalid entries.")



if __name__ == "__main__":
    marks, skipped = read_marks_file()
    print_summary(marks, skipped)
