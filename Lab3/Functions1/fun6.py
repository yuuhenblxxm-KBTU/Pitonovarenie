import json
import re

def calculate_average_gpa(data):
    total_gpa = sum(student["GPA"] for student in data["students"])
    average_gpa = total_gpa / len(data["students"])
    return average_gpa

def is_valid_email(email):
    # Basic email format validation using regular expression
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

# Load JSON data
with open('students_data.json', 'r') as file:
    data = json.load(file)

# Calculate average GPA
average_gpa = calculate_average_gpa(data)
print("Average GPA of all students:", average_gpa)

# Check if emails are valid
for student in data["students"]:
    if is_valid_email(student["email"]):
        print(f"{student['name']}'s email ({student['email']}) is valid.")
    else:
        print(f"{student['name']}'s email ({student['email']}) is not valid.")
