# Day 14: File handling
# writing and reading text files using python

# writing log file
with open("practice_log.txt", "w") as file:
    file.write("Day 14 Log:\n")
    file.write("Learned file handling operations.\n")
    file.write("Using python is getting more interesting.\n")

print("File written successfully.")

# reading the log file
print("Reading file content:")
with open("practice_log.txt", "r") as file:
    content = file.read()
    print(content)

# appending a new line
with open("practice_log.txt", "a") as file:
    file.write("Append line: Added this line later!\n")

# read log lines into a list
with open("practice_log.txt", "r") as file:
    lines = file.readlines()
    print("Lines read:", lines)

# exercise 1: count lines in the log file
line_count = len(lines)
print(f"Total lines: {line_count}")

# challenge: copy file content and save it in UPPERCASE
def copy_uppercase(src, dest):
    try:
        with open(src, "r") as s_file:
            content = s_file.read()
        with open(dest, "w") as d_file:
            d_file.write(content.upper())
        print(f"Copied from {src} to {dest} in UPPERCASE.")
    except FileNotFoundError:
        print("Source file not found!")

copy_uppercase("practice_log.txt", "practice_log_upper.txt")
