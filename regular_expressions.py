# regular expressions are available as standard library can be imported using re module
import re 

to_match = r"hello" # raw string

# match function checks if the given string matches the beginning of the string
if re.match(to_match, "hello"):
  print ("match")
else:
  print("No match")

# other regular expression functions re.search, re.findall
if re.search(to_match, "hello"):
  print ("match")
else:
  print("No match")

if re.findall(to_match, "hello"):
  print ("match")
else:
  print("No match")

