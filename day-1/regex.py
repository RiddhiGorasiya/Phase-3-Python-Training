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
# import re

# a = "harry potter and the1 chamber2@34 of secrets"

# match = re.search(r"\Aharry",a)
# print(match)

# match = re.search(r"ha\B",a)
# print(match)

# match = re.search(r"\ber",a)
# print(match)

# match = re.findall(r"\d",a)
# print(match)

# match = re.findall(r"\D",a)
# print(match)

# match = re.findall(r"\s",a)
# print(match)

# match = re.findall(r"\S",a)
# print(match)

# match = re.findall(r"\w",a)
# print(match)

# match = re.findall(r"\W",a)
# print(match)

# match = re.findall(r"\Z",a)
# print(match)

# re.findall()
# import re
# a = """ John has scored 89 marks
# lisa has scored 58 marks
# david has scored 78 marks """
# print(re.findall(r"\d+",a))
# print(re.findall(r"[A-Z][a-z]*",a))

# re.compile()
# import re
# a = """ John has scored 89 marks
# lisa has scored 58 marks
# david has scored 78 marks """
# p = re.compile("[a-d]")
# p = re.compile("[0-9]")
# print(re.findall(p,a))

# re.split()
# import re
# a = """ John has scored 89 marks
# lisa has scored 58 marks
# david has scored 78 marks """
# b = "fantastic 5 turtles"
# print(re.split(r"\d+" ,a))
# print(re.split(r"\d+" ,b))

# re.sub()
# import re
# a = """ John has scored 89 marks
# lisa has scored 58 marks
# # david has scored 78 marks """
# b = "fantastic 5 turtles"
# print(re.sub(r"\s+", "", a))
# print(re.sub(r"\s+", "", b))

# re.subn()
# import re
# a = """ John has scored 89 marks
# lisa has scored 58 marks
# # david has scored 78 marks """
# print(re.subn(r"\s+", "", a))

# re.escape()
# import re
# a = """ John has scored 89 marks
# lisa has scored 58 marks
# # david has scored 78 marks """
# print(re.escape(a))

# re.search()
import re
a = """ John has scored 89 marks
lisa has scored 58 marks
# david has scored 78 marks """
print(re.search(r"\d+", a))