
This notebook includes basics to using regular expressions (python)

https://www.sololearn.com/Play/Python/
    


```python
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

```

    No match
    match
    match
    <_sre.SRE_Match object; span=(3, 8), match='hello'>
    

> Other methods that can be called on object returned by re.search are group(), start(), end(), span()


```python
search = re.search(to_match, r"heyhellohihola")
print (search.group())
print (search.start())
print (search.end())
print (search.span())
```

    hello
    3
    8
    (3, 8)
    

> using __sub__ to search and replace a pattern in a given string


```python
# this subs the string with the given string from the string
re.sub("Sai", "Sai Saketh", "hello my name is Sai")
```




    'hello my name is Sai Saketh'



# MetaCharacters

This is what makes a regex more functional than a regular string method.

we need to use a raw string


```python
# . (dot) 

pattern = r"he..o"

if re.match(pattern, "hello"):
    print ("matches")
if re.match(pattern, "heylo"):
    print ("matches")
```

    matches
    matches
    

In the above regex using the dot metacharacter there can be anything in place of dot but the other parts of the string should match 

> Using ^ & $ metacharacters these match the start and end of a string


```python
# ^ & $

pattern = r"^he..o$"

if re.match(pattern, "gewwo"):
    print ("matches 1")
else:
    print ("does not match 1")
    
if re.match(pattern, "heylo"):
    print ("matches 2")
else:
    print ("does not match 2")    
```

    does not match 1
    matches 2
    

# Character Classes

This is used to match only a specific set of characters

we can match set of charaters by placing them in between square brackets


```python
# [hlo]

pattern = r"[hlo]"

if re.match(pattern, "gewwo"):
    print ("matches 1")
else:
    print ("does not match 1")
    
if re.match(pattern, "heylo"):
    print ("matches 2")
else:
    print ("does not match 2") 
    
# using search function
if re.search(pattern, "gewwo"):
    print ("matches 1 (search)")
else:
    print ("does not match 1 (search)")
    
if re.search(pattern, "heylo"):
    print ("matches 2 (search)")
else:
    print ("does not match 2 (search)")     
```

    does not match 1
    matches 2
    does not match 1 (search)
    matches 2 (search)
    

> Using this [hlo][e]

this will match any of the characters in first square bracket followed by the next any of the characters in second


```python
# [hlo][eos]

pattern = r"[hlo][es]"

if re.match(pattern, "hello"):
    print ("matches 1")
else:
    print ("does not match 1")
```

    matches 1
    

## matching using range of characters

[a-z] matches any lowercase alphabetic charater

similarly

[A-Z] any uppercase

[0-9] any number


```python
# [range of characters]

pattern = r"[0-9][a-z][A-Z]"

if re.search(pattern, "6fT"):
   print("Match 1")

if re.search(pattern, "3FT"):
   print("Match 2")
```

    Match 1
    

> we can use ^ to invert the match


```python
# ^

pattern = r"[^0-9][a-z][A-Z]"

if re.search(pattern, "6fT"):
   print("Match 1")

if re.search(pattern, "sfT"):
   print("Match 2")
```

    Match 2
    

i.e., it matches everything other than what is listed

> some more metacharacters are *,+,?,{and}.

* means zero or more repetitions of the specified string


```python
# *

pattern = r"hello(this)*"

if re.search(pattern, "hello"):
   print("Match 1")

if re.search(pattern, "hello this is good"):
   print("Match 2")

if re.search(pattern, "this is good"):
   print("Match 3")


```

    Match 1
    Match 2
    

> the above example matches the string that starts with hello followed by zero or more repetitions

### + is similar to * but instead of zero or more repetitions it is 1 or more repetitions


```python
pattern = r"hello(this)+"

if re.search(pattern, "hello"):
   print("Match 1")

if re.search(pattern, "hellothis is good"):
   print("Match 2")

if re.search(pattern, "this is good"):
   print("Match 3")

```

    Match 2
    

### ? means zero or one repetitions


```python
# ?

pattern = r"mango(!)?juice"

if re.search(pattern, "mangojuice"):
   print("Match 1")

if re.search(pattern, "mango!juice"):
   print("Match 2")

if re.search(pattern, "mango!!juice"):
   print("Match 3")

```

    Match 1
    Match 2
    

### instead of using above metacharacters we can use {} and specify no of repetitions to accept


```python
# {0,2}

pattern = r"mango(!){0,2}juice"

if re.search(pattern, "mangojuice"):
   print("Match 1")

if re.search(pattern, "mango!juice"):
   print("Match 2")

if re.search(pattern, "mango!!juice"):
   print("Match 3")

```

    Match 1
    Match 2
    Match 3
    

# Groups

surrounding part of a regular expression with parentheses creates a group.

we can give this group as an argument to the metacharacters we have seen above.


```python
# (best)*

pattern = r"(best)*mangojuice"

if re.search(pattern, "mangojuice"):
   print("Match 1")

if re.search(pattern, "bestmangojuice"):
   print("Match 2")
```

    Match 1
    Match 2
    

> contents of group fuction can be accesed using group function


```python
pattern = r"1(234)(56)(7(8)9)"

match = re.match(pattern, "1234567890")
if match:
   print(match.group())
   print(match.group(0))
   print(match.group(1))
   print(match.group(3))
   print(match.groups())
```

    123456789
    123456789
    234
    789
    ('234', '56', '789', '8')
    

group(0) or group() returns the whole match. 
group(n), where n is greater than 0, returns the nth group from the left. 
The method groups() returns all groups up from 1.

> some special groups are __named groups__ and __non_capturing groups__

named groups as the name suggests the groups can be named there format is (?P<name>aaa) where name is the name of the group and aaa is content

non_capturing groups as the names suggests cannot be accesed by group method.
format (?:aaa) whee aaa is the content of the group.


```python
# ?P<...> named groups & ?: unidentified groups

pattern = r"1(?P<name>234)(?:56)(7(8)9)"

match = re.match(pattern, "1234567890")
if match:
   print(match.group("name"))
   print(match.groups())
   print(len(match.groups()))
```

    234
    3
    

Here we can see that the no 56 is not being accessed by group method.

### metacharacter | which means or


```python
# | (or)

pattern = r"gr(ea|ee)t"

match = re.match(pattern, "great")
if match:
   print ("Match 1")

match = re.match(pattern, "greet")
if match:
   print ("Match 2")    

match = re.match(pattern, "goes")
if match:
    print ("Match 3")
```

    Match 1
    Match 2
    

# Special Sequences

Various special sequences can be used with regular expreesions.

one common way to do this by using backlash followed by a number which indicates no of sequences of that pattern.


```python
# \1 backlash & number special sequence

pattern = r"(.+) \1"

match = re.match(pattern, "great great")
if match:
   print ("Match 1")

match = re.match(pattern, "good great")
if match:
   print ("Match 2")    

match = re.match(pattern, "abc abc abc")
if match:
    print ("Match 3")  
```

    Match 1
    Match 3
    

> we can see that the above expression matches for one or more sequences


```python
# another example


pattern = r"(123|456) \1"

match = re.match(pattern, "123456")
if match:
   print ("Match 1")

match = re.match(pattern, "123 123")
if match:
   print ("Match 2")    

match = re.match(pattern, "123 456")
if match:
    print ("Match 3")  
```

    Match 2
    

# more special sequences

> \d matches all digits, \s - whitespace, \w - word characters

Another case is

> \D - matches everything except digits, \W - opposite to word characters, \S matches all non whitespace


```python
# D & d

pattern = r"(\D+\d)"

match = re.match(pattern, "hello1")
if match:
    print ("match 1")
```

    match 1
    


```python
# \W & w


pattern = r"(\W+\w)"

match = re.match(pattern, ".,..%sai")
if match:
    print ("match 1")
```

    match 1
    


```python
# \S & \s


pattern = r"(\S+\s)"

match = re.match(pattern, "sai Saketh")
if match:
    print ("match 1")
```

    match 1
    

> Additional Special sequences 

\A, \Z match beginning and end of a string

\b matches empty string between \w and W

\B matches empty string anywhere else


```python
# \A, \Z


pattern = r"\As.......h\Z"

match = re.match(pattern, "saiSaketh")
if match:
    print ("match 1")
```

    match 1
    


```python
# \B

pattern = r"\B(hey)\B"

match = re.search(pattern," helloheythis ")
if match:
    print ("match 1")

# \b    
    
pattern = r"\b(hey)\b"
    
match = re.search(pattern,"hello!hey this")
if match:
    print ("match 2")    
```

    match 1
    match 2
    

# matching email address


```python
import re

pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
str = "Please visit sololearn.com for learning thankyou@gmail.com"

match = re.search(pattern, str)
if match:
   print(match.group())
```

    thankyou@gmail.com
    


```python

```
