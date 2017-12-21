# regular expressions are available as standard library can be imported using re module
import re 

to_match = r"hello" #raw string

# match function checks if it matches at the beginning of the string takes two inputs
if re.match(to_match, "hello"):
  print ("match")
else:
  print("No match")
