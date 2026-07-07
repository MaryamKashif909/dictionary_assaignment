# student = {
#     "name" : "Ummehani",
#     "age"  : 16,
#     "city" :"Karachi",
#     "course": "Python"
# }
# student ["email"] = "abc@gmail.com"
# print(student)
# print("Data Type:",type(student))



# # Create the dictionary
# car = {
#     "brand" : "Ford",
#     "model" : "Mustang",
#     "year"  : 2024,

# }
# # Print the model
# print("Model:",car["model"])

# # Add a color key
# car ["color"] =  "red"
# print("Add a color key:",car)

# car.pop("brand")

# # Print the dictionary
# print(car)

student = {
    "name": "Zoha",
    "age": 20,
    "city": "Karachi"
}

print(list(student.keys()))
print(list(student.values()))
print(len(student))
print(tuple(student.items())[0][0])
