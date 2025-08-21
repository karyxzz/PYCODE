import json
from datetime import datetime

FILE_NAME = "employee_data.json"


def save_record():
    emp_id = input("Enter Employee ID: ")
    check_in = input("Enter Check-in time (HH:MM): ")
    check_out = input("Enter Check-out time (HH:MM): ")

    # Load existing records if file exists
    try:
        with open(FILE_NAME, "r") as f:
            records = json.load(f)
    except FileNotFoundError:
        records = {}

    # Save new record
    records[emp_id] = [check_in, check_out]

    with open(FILE_NAME, "w") as f:
        json.dump(records, f, indent=4)

    print("Data saved successfully!")


def calculate_hours():
    try:
        with open(FILE_NAME, "r") as f:
            records = json.load(f)
    except FileNotFoundError:
        print("No data found!")
        return

    for emp_id, times in records.items():
        check_in, check_out = times
        t1 = datetime.strptime(check_in, "%H:%M")
        t2 = datetime.strptime(check_out, "%H:%M")
        worked = t2 - t1
        hours = worked.total_seconds() / 3600
        print(f"Employee {emp_id} worked {hours:.2f} hours.")


if __name__ == "__main__":
    while True:
        print("\n1. Save record")
        print("2. Calculate hours worked")
        print("3. Exit")
        choice = input("Choose option: ")

        if choice == "1":
            save_record()
        elif choice == "2":
            calculate_hours()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Try again.")
