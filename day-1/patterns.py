# email
import re
a = """Hello from riddhi34556@gmail.com
to disha@yahoo.com about the meeting @2pm"""
lst = re.findall(r'\S+@\S+', a)
print(lst)

# phone number
import re
a = """Call me at 9876543210 or at +919876543210.
My office number is 09123456789."""
lst = re.findall(r'(\+91[\-\s]?\d{10}|0\d{10}|[6-9]\d{9})', a)
print(lst)

# file name
import re
a = """Here are some files: report.txt, data123.csv, 
invalid|name.doc, my-file.pdf, photo.jpeg"""
lst = re.findall(r'[\w,\s-]+\.[A-Za-z]{2,4}', a)
print(lst)
