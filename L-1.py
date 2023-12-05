Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
2*2
4
>>> print('hi')
hi
>>> print("Bhavya's laptop)
...       
SyntaxError: incomplete input
>>> print("Bhavya's laptop")
...       
Bhavya's laptop
>>> print('Bhavya\'s "laptop"')
...       
Bhavya's "laptop"
>>> print("Bhavya's \"Laptop")
...       
Bhavya's "Laptop
>>> print("Bhavya's \"Laptop\"")
...       
Bhavya's "Laptop"
>>> Bhavya*8
...       
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    Bhavya*8
NameError: name 'Bhavya' is not defined
>>> print("Bhavya*8")
...       
Bhavya*8
>>> 'Bhavya'*8
...       
'BhavyaBhavyaBhavyaBhavyaBhavyaBhavyaBhavyaBhavya'
>>> print('c:\docs\navin')
...       
c:\docs
avin
>>>  print(r'c:\docs\navin')
...       
SyntaxError: unexpected indent
>>> print(r'c:\docs\navin')
...       
c:\docs\navin
