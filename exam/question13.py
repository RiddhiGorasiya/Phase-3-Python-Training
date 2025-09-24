import re

def extract_phone_numbers(text):
    pattern = r"\b\d{3}[-.\s]??\d{3}[-.\s]??\d{4}\b"
    return re.findall(pattern, text)

text = "Call me at 123-456-7890 or 987.654.3210 or 555 666 7777."
print(extract_phone_numbers(text))


