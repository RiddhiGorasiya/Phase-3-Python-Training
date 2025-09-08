# import re

# a = "charlie chaplin coa and the chocolate factory"
# b = "riddhi.gorasiya@gmail.com" 
# c = "hello world"
# d = "XYZ, YZ, Z, XYYZ, XXYYZ, XX, YZZ, Y, YZ, ZYX"

# match = re.search(r"\.",b) # \ Signals a special sequence (can also be used to escape special characters)
# print(match)

# match = re.search(r"[@]",b) # [] A set of characters
# print(match)

# match = re.search(r"[^u]",c) # ^ Starts with
# print(match)

# match = re.search(r"[com$]",b) # $ Ends with
# print(match)

# match = re.findall(r"[c.a]",a) # . Any character except newline
# print(match)

# match = re.findall(r"cha|tor",a) # | Either or
# print(match)

# match = re.findall(r"ch?a",a) # ? Zero or one occurrence
# print(match)

# match = re.findall(r"ch*a",a) # * Zero or more occurrences
# print(match)

# match = re.findall(r"XY+Z",d) # + One or more occurrences
# print(match)

# match = re.findall(r"X{2,4}",d) # {} Exactly the specified number of occurrences
# print(match)

# match = re.findall(r"(X|Y)YZ",d) # () Capture and group
# print(match)


# special sequences
import re

a = "harry potter and the1 chamber2@34 of secrets"

match = re.search(r"\Aharry",a)
print(match)

match = re.search(r"ha\B",a)
print(match)

match = re.search(r"\ber",a)
print(match)

match = re.findall(r"\d",a)
print(match)

match = re.findall(r"\D",a)
print(match)

match = re.findall(r"\s",a)
print(match)

match = re.findall(r"\S",a)
print(match)

match = re.findall(r"\w",a)
print(match)

match = re.findall(r"\W",a)
print(match)

match = re.findall(r"\Z",a)
print(match)