# Day 13: Strings and slicing
# learning string methods and reverse slicing tricks

text = "Learning Python is fun!"
print("Original string:", text)

# slicing practice
print("First 8 letters:", text[:8])
print("Middle chunk:", text[9:15])
print("Every second letter:", text[::2])
print("Reversed text:", text[::-1])

# some string methods
spaced_text = "   Python practice   "
print("Stripped spaces:", spaced_text.strip())
print("Capitalized:", text.upper())
print("Replaced text:", text.replace("fun", "awesome"))

# checking sub-strings
print("Has 'Python'?", "Python" in text)
print("Starts with 'Learn'?", text.startswith("Learn"))

# exercise 1: join strings together
word_list = ["This", "is", "a", "good", "day"]
joined = " ".join(word_list)
print("Joined:", joined)

# challenge: check if string is palindrome
def is_palindrome(s):
    cleaned = "".join(s.split()).lower()
    return cleaned == cleaned[::-1]

test1 = "Race car"
test2 = "Hello"
print(f"Is '{test1}' palindrome? {is_palindrome(test1)}")
print(f"Is '{test2}' palindrome? {is_palindrome(test2)}")
