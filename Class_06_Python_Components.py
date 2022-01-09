#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Python Programming Components
Literals
Identifiers
Constants
Variable
Expressions
Statements
Blocks 
Indentation
Comments
Escape Sequences
Data Types
Operators


# In[ ]:


# Literals - Any value

age = 28
name = 'Rahul'
company = 'Learnbay'
lst_name = ['Krishna', 'Rahul', 'Sunita']
sal = 50000.90

Integer - 10, -10, 0
Float - 10.20, -10.20, 0.002
complex - 10+20j, 10-20j
String - 'Python'
Boolean - True False


# In[ ]:


# Identifiers - Any name we use in a Python program
# Constant, Variable, class, function, method, objects

# Rules
1. Allowed Characters - A-Z, a-z, 0-9, _
2. Not allowed characters - Special Characters
3. Identifier shild not start with a number.
4. Identifiers are case sensitive.

# Recommendation
1. Reserved words should not be used as an identifier
2. To define the constants we should use only capital case letters.
3. To define class we should use only pascalCaseNotation.
4. Avoid writing any identifier starting and ending with __.


# In[29]:


# # 1marks1 = 260
# (260/300)*100

# marks = 290
# print(Marks)

# Reserved words
# import keyword
# print(keyword.kwlist)

# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 
#  'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
#  'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

# for = 100

# For = 100

# emp_name = 'Rahul'
# emp_id = 101
# emp_sal = 50000.90
# EMP_COMPANY = 'Learnbay'
# print(EMP_COMPANY)
# EMP_COMPANY = 'TCS'
# print(EMP_COMPANY)


# class carParkingLot:
#     pass

# PI = 3.14


print(dir(int))

# print(10+20)

# print(abs(-10))

# __abc__ = 1000

a = 100
# print(a.as_integer_ratio())

print(a.bit_length())


# In[33]:


# print(help(a.as_integer_ratio))


# In[32]:


# print(dir(float))

# a = 10.20
# a.as_integer_ratio()


# In[52]:


# Expressions - Combination of Operators, operand, values and variables which givrs some result after execution

10+20

10

'Python'

'Python' + 'Class'

a = 3
b = 'Python'
b*a






# In[49]:


# Statements - Combination of Operators, operand, values and variables which does not give any result after execution

a = 10
b = 20
c = 'Python'
if a<b:pass
for i in range(5):pass


# In[ ]:


# Indentation - space
# Blocks


# emp_name = 'Rahul'
# emp_id = 101
# emp_sal = 50000.90
# def emp_det(e_name, e_id, e_sal):
#     e_addr = 'Bengaluru'
#     e_is_married = False
#     print(f'Employee Name is {e_name}')
#     print(f'Employee ID is {e_id}')
#     print(f'Employee Salary is {e_sal}')
#     print(f'Employee Address is {e_addr}')
#     print(f'Employee is Married {e_is_married}')
# emp_det(emp_name, emp_id, emp_sal)
# print(emp_name)
# print(emp_id)
# print(emp_sal)
# print(e_addr)
# print(e_is_married)


def f1():
    code1
    code2
    for loop:
        code3
        code4
        code5
        if cond:
            code6
            code7
            code8
        code9
        code10
    code11
    code12
code13
code14


# In[56]:


# Comments - # in the begining
# Also used to write he properly documented code




emp_name = 'Rahul'
emp_id = 101
emp_sal = 50000.90
# This function is going to give some details of the employees
def emp_det(e_name, e_id, e_sal):
    e_addr = 'Bengaluru'
    e_is_married = False
    print(f'Employee Name is {e_name}')
    print(f'Employee ID is {e_id}')
    print(f'Employee Salary is {e_sal}')
    print(f'Employee Address is {e_addr}')
    print(f'Employee is Married {e_is_married}')
# emp_det(emp_name, emp_id, emp_sal)
# print(emp_name)
# print(emp_id)
# print(emp_sal)
# print(e_addr)
# print(e_is_married)





# In[64]:


# Escape Sequences
# \'
# \"
# \\
# \n - new line
# \t
# \v


# my_str = 'This is Python\'s class'
# print(my_str)

# my_str = "This is \"Python\" class"
# print(my_str)

# my_str = 'This is \\nothing'
# print(my_str)\


# my_str = 'This is \npython class'
# print(my_str)

# my_str = 'This is \tpython class'
# print(my_str)

# my_str = 'This is \vpython class'
# print(my_str)


# In[90]:


# Data Types

# Fundamental - int, float, complex, Boolean, Strings
# Derived - List, Tuple, set, frozenset, Dictionary, bytes, bytearray, range

# Integers - Any number without a decimal point
# 10, -10, 0
# Representation of integer values
# Decimal Format - 10, 0-9, no prefix required,
# Binary format - 2, 0-1, 0b - prefix, bin(val) - (val -> int, bin, oct, hex)
# Octal format - 8, 0-7, 0o - Prefix, oct(val) - (val -> int, bin, oct, hex)
# Hexadecimal format - 16, 0-9 a-f, 0x - Prefix, hex(val) - (val -> int, bin, oct, hex)

# a = 10
# b = -10
# c = 0
# print(a, type(a))
# print(b, type(b))
# print(c, type(c))

a = 10101
print(bin(a))


# In[71]:


# a = 97686568754653426789654
# print(hex(a))

# a = 0xfc98
# print(a)
# print(hex(id(a)))



# a = 'Python'

# Python is dynamically typed
import sys
a = 10
print(sys.getsizeof(a))

a = 10999999999999999999999999999999999999
print(sys.getsizeof(a))


# In[ ]:


# Floats - any number with decimal point
# 10.20, -10.20

# Floats can not be represented in binary, octal, hexadecimal format



# In[75]:


# complex - a+bj

# a is real
# b is imaginary

num = 10-20j
print(num.real)
print(num.imag)


# Complex can not be represented in binary, octal, hexadecimal format



# In[77]:


print(dir(int))


# In[78]:


help(int)


# In[80]:


print(dir(float))


# In[81]:


help(float)


# In[83]:


print(dir(complex))


# In[84]:


help(complex)


# In[ ]:


# Operators


# In[89]:


a = 0b111+0xfc98j
print(a)


# In[86]:


bin(10+20j)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




