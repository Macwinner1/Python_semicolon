import re

numbers = "123-456-7890"

pattern = re.findall(r"\d\d\d-\d\d\d-\d\d\d", numbers)

print(pattern)

email = "sammy566@gmail.com"
pattern = re.findall(r'([\da-zA-Z]*@gmail\.com|yahoo\.com+)', email)

print(pattern)

text = "Alice and Bob are Good Friends."
pattern = re.findall(r"\b[A-Z][a-z]+", text)
count = 0
for item in pattern:
    count += 1
print(pattern, count)

sentence = "Hello! How are you doing?"
pattern = re.findall(r"\b\w+", sentence)
print(pattern)