#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Object Reusability
# Mutability and Immutability
# Python programming components
# Literal, constant, variables, identifiers, Reserved Words, Expression Statements


# In[8]:


# Object Reusability
# int - -5 to 256 - Integer Caching
# String - A-Z, a-z, 0-9, _ - String Interning
# True, False None

# FLoat(0-1), Complex(float+float*j), Derived Data types - [], [-inf to +inf]

# a = 10
# b = 10
# print(id(a))
# print(id(b))

# a = 1000
# b = 1000
# print(id(a))
# print(id(b))

# my_str1 = 'Python_Class1'
# my_str2 = 'Python_Class1'
# print(id(my_str1))
# print(id(my_str2))

my_str1 = 'Python Class1'
my_str2 = 'Python Class1'
print(id(my_str1))
print(id(my_str2))


# In[2]:


import sys
a = 10
print(sys.getsizeof(a))


# In[18]:


# Mutability - The object in which modification is possible are called Mutable Objects.
# List, Set, Dictionary, Bytearray
# Item assignment is possible.
# Modifications are done in the existong object(methods, item assignment)

# lst = [10, 10.20, 10+20j, 'Python', True, None]
# print('Before Item Assignment')
# print(lst, id(lst))
# lst[0] = 111
# print()
# print('After Item Assignment')
# print(lst, id(lst))


# d = {1:100, 10.2:200.30, 20+30j:30-40j, 'a':'Python', False:True}
# print('Before Item Assignment')
# print(d, id(d))
# d[1] = 111
# print()
# print('After Item Assignment')
# print(d, id(d))

lst = [10,20,30]
print(lst, id(lst))
print()
lst = lst*2
print(lst1, id(lst1))
print(lst, id(lst))


# Immutability - The object in which modification is not possible are called Immutable Objects.
# Tuple, Frozenset, Bytes, string
# Item assignment is not possible.
# Immutable objects create a new object

# tpl = (1, 2, 3, 4)
# Item assignmet is not possible
# tpl[0] = 111

# print('Before Operation')
# print(tpl, id(tpl))
# tpl= tpl + (11, 22, 33)
# print('After Operation')
# print(tpl, id(tpl))


# In[22]:


# import numpy as np
# arr = np.array([10,20,30])
# print(arr, id(arr))
# print(arr+2, id(arr+2))


# In[36]:


# Frozenset
s = set([10,20,30,4])
print(s, type(s))
# s.add(100)
# print(s)
# print()

fz = frozenset([11, 22, 33, 44, 55])
print(fz)
fz.add(111)
print(fz)


# In[33]:


# a = 10
# print(a, id(a))
# a = a+2
# print(a,id(a))

lst = [10,20,30]
print(lst, id(lst))
lst = lst * 2
print(lst, id(lst))


# In[35]:


len([10,20,30,40])


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




