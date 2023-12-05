Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x=9
x+10
19
y=3
_+y
22
'''  "-" is used to use last result '''
'  "-" is used to use last result '
name='Bhavya'
surname='Jain'
name+surname
'BhavyaJain'
name+ surname
'BhavyaJain'
name='Bhavya '
surname='Jain'
SyntaxError: multiple statements found while compiling a single statement
>>> a='Bhavya '
... b='Jain'
SyntaxError: multiple statements found while compiling a single statement
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined
>>> print('j')
j
>>> name='AMIRI'
>>> name[0]
'A'
>>> name[0:6]
'AMIRI'
>>> name[0:7]
'AMIRI'
>>> name[0:1:6]
'A'
>>> name[0::1::6]
SyntaxError: invalid syntax
>>> len(njdfndfnadf)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    len(njdfndfnadf)
NameError: name 'njdfndfnadf' is not defined
>>> len(AMIRI)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    len(AMIRI)
NameError: name 'AMIRI' is not defined
>>> lem(name)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    lem(name)
NameError: name 'lem' is not defined. Did you mean: 'len'?
>>> len(name)
5
