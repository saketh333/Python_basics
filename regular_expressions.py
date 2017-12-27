# regular expressions are available as standard library can be imported using re module
import re 

to_match = r"hello" # raw string

# match function checks if the given string matches the beginning of the string
if re.match(to_match, r"heyhellohihola"):
  print ("match")
else:
  print("No match")

# other regular expression functions re.search, re.findall

# search searches for that string in the given string  
if re.search(to_match, r"heyhellohihola"):
  print ("match")
else:
  print("No match")

# finds and prints all the matched strings  
if re.findall(to_match, r"heyhellohihola"):
  print ("match")
else:
  print("No match")

# function re.finditer does the same thing as findall but returns an iterator
iter =  re.finditer(to_match, r"heyhellohihola")
for i in iter:
    print (i)
