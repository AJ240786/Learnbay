#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Memory Management in Python
# Raw Memory Allocator, Object Specific Allocator Python Virtual Machine & Interpreter
# Memory deallocation in Python
# Namespace and scope
# Automatic garbage collection in Python 
# Memory management visualisation
# Object Reusability
# Mutability and Immutability
# Python programming components
# Literal, constant, variables, identifiers, Reserved Words, Expression Statements


# In[ ]:


# Type of Errors
    1. Compile time Error - Compiler
    2. Run time Error - Interpreter

# Conclusion
1. Byte code will not be created if we have any compile time Error in source code.
2. Byte code will be generated if there is no compile time Error.
3. If we have run time Error then byte code will be generated but it will do partial execution of code.
    
    


# In[ ]:


# Python Features
1. Python is simple, easy to understand and expressive language.
2. Python is portable and platform independent both.
3. Python is Interpreted PL.
4. Python is Dynamically typed PL.
5. Python is General Purpose PL
    App Development, AI & ML app, Automation, Scripting, Data analysis, Data Scientist and Research
6. Python is Extensinble(Code written in other PL can be used in Python) 
    and Embedded(Code written in Python can be used in Other PL)
7. Huge library Supprt(math, os, sys, datetime, random etc)


# In[ ]:


Memory Management in Python - Automatic
    1. Memory Allocation
        Raw Memmory Allocator
        Object Specific Allocator
        Python Virtual Machine
    2. Memory Deallocation
        Garbage Collector


# In[7]:


emp_name = 'Rahul'
emp_id = 101
emp_sal = 50000.90
def emp_det(e_name, e_id, e_sal):
    e_addr = 'Bengaluru'
    e_is_married = False
    print(f'Employee Name is {e_name}')
    print(f'Employee ID is {e_id}')
    print(f'Employee Salary is {e_sal}')
    print(f'Employee Address is {e_addr}')
    print(f'Employee is Married {e_is_married}')
emp_det(emp_name, emp_id, emp_sal)
# print(emp_name)
# print(emp_id)
# print(emp_sal)
print(e_addr)
print(e_is_married)

# global names - emp_name, emp_id, emp_sal, emp_det - names which are defined outside of the function
# Local Names - e_name, e_id, e_sal, e_addr, e_is_married, - names which are defined inside the function


# In[10]:


import sys
a = 'Python  class is conducted in Morning'
print(sys.getsizeof(a))


# In[11]:


print(dir(__builtins__))


# In[12]:


a = 10
b = 10
c = 10
print(sys.getrefcount(10))


# In[13]:


a = 10
print(sys.getsizeof(a))

b = 1000000000000000000000000000000000000000000000000000000000
a = 10
print(sys.getsizeof(b))


# In[14]:


a = 10.20
print(sys.getsizeof(a))

b = 1000000000000000000000000000000000000000000000000000000000.9000000000000000000000000000000000000000000000000000000000
a = 10
print(sys.getsizeof(b))


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




