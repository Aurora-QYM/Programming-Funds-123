def print_report(students):
    header = f"{'Name':<12} {'Score':<6} {'Grade':>6} {'Status':>8}"
    separator = "-" * len(header)

    print(header)
    print(separator)

    for name, score in students:
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"

        status = "Pass" if score >= 60 else "Fail"
        print(f"{name:<12} {score:<6.1f} {grade:<6} {status:>8}")

students = [("Alice", 92.5), ("Bob", 74.0), ("Carol", 58.5), ("Dave", 85.0)]
print_report(students)
