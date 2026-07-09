###================================###
 # QUESTION 1
###=================================###


student = {
    "name": "Maryam",
    "age": 16,
    "city": "Karachi",
    "hobbies": ["skeching", "Reading", "Gaming"],
    "skills": ["Python", "Ms office", "javascipt"]
marks = {
    "math": 85,
    "english": 75,
    "science": 90,
    "computer": 95
}

}

# Print student name
print("Student Name:", student["name"])

# Print first hobby
print("First Hobby:", student["hobbies"][0])

# Print total skills
print("Total Skills:", len(student["skills"]))

print("Subject Marks")


for subject, mark in marks.items():
    print(subject, ":", mark)

total = sum(marks.values())
average = total / len(marks)

print("Total Marks:", total)
print("Average Marks:", average)



###===================================###
  # QUESTION 3 
###===================================###


average = 86.25

if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
else:
    grade = "Fail"

print("Grade:", grade)

if average >= 60:
    print("Passed")
else:
    print("Failed")



###=================================###
  # QUESTION 4
###=================================###
    
attendance = {
    "total_classes": 100,
    "attended_classes": 80
}

percentage = (attendance["attended_classes"] / attendance["total_classes"]) * 100

print("Attendance Percentage:", percentage)

if percentage < 75:
    print("Short Attendance")
else:
    print("Eligible For Exam")

###=================================###
   #QUESTION 5
###=================================###
    
    student = {
    "fee_paid": True
}

if student["fee_paid"]:
    print("Fee Cleared")
else:
    print("Fee Pending")
    
###=================================###
   #QUESTION 6
###=================================###
    
student = {
    "skills": ["Python", "Ms office", "Javascript"]
}

# Add new skill
student["skills"].append("Html")

# Remove one skill
student["skills"].remove("Javascript")

print("Updated Skills:", student["skills"])

print("Total Skills:", len(student["skills"]))
    
###=================================###
   #QUESTION 7
###=================================###
    
account = {
    "username": "admin",
    "password": "12345"
}

username = input("Enter Username: ")
password = input("Enter Password: ")

if username == account["username"] and password == account["password"]:
    print("Login Successful")
else:
    print("Invalid Credentials")

###=================================###
   #QUESTION 8
###=================================###
    
    student = {
    "address": {
        "area": "Gulistan e johar",
        "street": "Street 5",
        "house_number": 19
    }
}

print("Complete Address")

print(
    student["address"]["house_number"],
    student["address"]["street"],
    student["address"]["area"]
)

# Update area
student["address"]["area"] = "Gulshan iqbal"

# Add zip code
student["address"]["zip_code"] = 74700

print(student["address"])

###================================###
 # QUESTION 9
###=================================###

students = {
    "student1": {
        "name": "maryam",
        "city": "Karachi",
        "marks": 450
    },
    "student2": {
        "name": "Amna",
        "city": "Karachi",
        "marks": 470
    }
}

print("Student1 Name:", students["student1"]["name"])

print("Student2 Marks:", students["student2"]["marks"])

students["student2"]["city"] = "Islamabad"

print(students)

###================================###
 # QUESTION 10
###=================================###

student = {
    "profile": {
        "name": input("Enter Name: "),
        "age": int(input("Enter Age: ")),
        "city": input("Enter City: ")
    },

    "marks": {
        "math": int(input("Math Marks: ")),
        "english": int(input("English Marks: ")),
        "science": int(input("Science Marks: ")),
        "computer": int(input("Computer Marks: "))
    },

    "attendance": {
        "total_classes": int(input("Total Classes: ")),
        "attended_classes": int(input("Attended Classes: "))
    },

    "fee_paid": input("Fee Paid? (yes/no): ").lower() == "yes",

    "skills": ["Python", "Ms office"],

    "address": {
        "area": "Gulistan e johar",
        "street": "Street 5",
        "house_number": 19
    }
}

# Calculations
total = sum(student["marks"].values())
average = total / len(student["marks"])

# Grade
if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
else:
    grade = "Fail"

# Attendance
attendance_percentage = (
    student["attendance"]["attended_classes"]
    / student["attendance"]["total_classes"]
) * 100

attendance_status = (
    "Eligible For Exam"
    if attendance_percentage >= 75
    else "Short Attendance"
)

fee_status = "Fee Cleared" if student["fee_paid"] else "Fee Pending"

# Report Card
print("\n========== STUDENT REPORT CARD ==========")

print("\nPROFILE")
print("Name :", student["profile"]["name"])
print("Age  :", student["profile"]["age"])
print("City :", student["profile"]["city"])

print("\nMARKS")
for subject, mark in student["marks"].items():
    print(subject.capitalize(), ":", mark)

print("\nTotal Marks :", total)
print("Average     :", average)
print("Grade       :", grade)

print("\nATTENDANCE")
print("Percentage :", attendance_percentage)
print("Status     :", attendance_status)

print("\nFEE STATUS")
print(fee_status)

print("\nSKILLS")
for skill in student["skills"]:
    print("-", skill)

print("\nADDRESS")
print("Area :", student["address"]["area"])
print("Street :", student["address"]["street"])
print("House No :", student["address"]["house_number"])

print("\n=========================================")
