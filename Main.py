import csv
filename = "students data.csv"
students_data = {}
def load_data():
    file = open(filename, "r")

    for line in file:
        if line.startswith("ID"):
            continue

        data = line.strip().split(",")

        students_data[data[1]] = {
            "ID": data[0],
            "Maths": int(data[2]),
            "Science": int(data[3]),
            "English": int(data[4]),
            "Attendance": int(data[5]),
            "Average": float(data[6]),
            "Grade": data[7],
            "Result": data[8]
        }

    file.close()

def save_data():
    with open(filename, "w", newline="") as file:
        fieldnames = ["ID", "Name", "Maths", "Science", "English",
                      "Attendance", "Average", "Grade", "Result"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for name, data in students_data.items():
            writer.writerow({
                "ID": data["ID"],
                "Name": name,
                "Maths": data["Maths"],
                "Science": data["Science"],
                "English": data["English"],
                "Attendance": data["Attendance"],
                "Average": data["Average"],
                "Grade": data["Grade"],
                "Result": data["Result"]
            })
def calculate_grade(avg):
    if avg >= 75:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 40:
        return "C"
    else:
        return "F"
def add_student():
    name = input("Enter Student Name: ")

    if name in students_data:
        print("Student already exists!")
        return

    sid = input("Enter Student ID: ")
    students_data[name] = {
        "ID": sid,
        "Maths": 0,
        "Science": 0,
        "English": 0,
        "Attendance": 0,
        "Average": 0.0,
        "Grade": "-",
        "Result": "-"
    }
    print("Student added successfully!")
def enter_marks():
    name = input("Enter Student Name: ")

    if name not in students_data:
        print("Student not found!")
        return

    m = int(input("Enter Maths Marks: "))
    s = int(input("Enter Science Marks: "))
    e = int(input("Enter English Marks: "))
    att = int(input("Enter Attendance Percentage: "))

    avg = (m + s + e) / 3
    grade = calculate_grade(avg)
    result = "PASS" if avg >= 40 and att >= 75 else "FAIL"

    students_data[name].update({
        "Maths": m,
        "Science": s,
        "English": e,
        "Attendance": att,
        "Average": round(avg, 2),
        "Grade": grade,
        "Result": result
    })

    print("Marks updated successfully!")
def search_student():
    name = input("Enter Student Name to Search: ")

    if name not in students_data:
        print("Student not found!")
        return

    data = students_data[name]
    print("\n----- Student Report -----")
    print("Name:", name)
    print("ID:", data["ID"])
    print("Maths:", data["Maths"])
    print("Science:", data["Science"])
    print("English:", data["English"])
    print("Attendance:", data["Attendance"], "%")
    print("Average:", data["Average"])
    print("Grade:", data["Grade"])
    print("Result:", data["Result"])
    
def delete_student():
    name = input("Enter Student Name to Delete: ").strip()

    if name in students_data:
        del students_data[name]
        print("Student record deleted successfully!")
    else:
        print("Student not found!")
def class_analysis():
    if not students_data:
        print("No student data available!")
        return

    averages = [data["Average"] for data in students_data.values()]
    total_students = len(averages)
    class_avg = sum(averages) / total_students
    highest = max(averages)
    lowest = min(averages)

    passed = sum(1 for data in students_data.values() if data["Result"] == "PASS")
    pass_percent = (passed / total_students) * 100

    print("\n----- Class Performance -----")
    print("Total Students:", total_students)
    print("Class Average:", round(class_avg, 2))
    print("Highest Average:", highest)
    print("Lowest Average:", lowest)
    print("Pass Percentage:", round(pass_percent, 2), "%")
def menu():
    while True:
        print("\n--------------------------------------")
        print("STUDENT PERFORMANCE MANAGEMENT SYSTEM")
        print("--------------------------------------")
        print("1. Add Student")
        print("2. Enter / Update Marks")
        print("3. Search Student by Name")
        print("4. Class Performance Analysis")
        print("5. Delete Student")
        print("6. Save & Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            enter_marks()
        elif choice == "3":
            search_student()
        elif choice == "4":
            class_analysis()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            save_data()
            print("Data saved. Exiting program...")
            break
        else:
            print("Invalid choice!")
load_data()
menu()