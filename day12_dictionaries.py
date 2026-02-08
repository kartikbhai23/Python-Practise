# Day 12: Dictionaries
# storing items in key-value pairs

student = {
    "name": "Kartik",
    "course": "Python Practice",
    "week": 2,
    "skills": ["Git", "Python"]
}
print("Student dict:", student)

# access keys
print("Name:", student["name"])
print("Grade:", student.get("grade", "Not assigned"))

# add new key-value and update week
student["week"] = 3
student["email"] = "kartik@example.com"
print("Updated student:", student)

# looping keys and values
for key, val in student.items():
    print(f"  {key}: {val}")

# exercise 1: pop 'course' out
removed_val = student.pop("course")
print(f"Removed course: '{removed_val}'. Dict is: {student}")

# challenge: count word frequency in a sentence
sentence = "apple banana apple cherry banana apple"
words = sentence.split()
freq_dict = {}
for word in words:
    freq_dict[word] = freq_dict.get(word, 0) + 1

print("Word count frequencies:")
print(freq_dict)
