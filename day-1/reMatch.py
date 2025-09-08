import re

a = "The rain in Spain"
b = "riddhi.gorasiya@gmail.com" 
c = "hello world"
d = "XYZ, YZ, Z, XYYZ, XXYYZ, YZZ, Y, ZYX"

match = re.search(r"\.",b)
print(match)

match = re.search(r"[@]",b)
print(match)