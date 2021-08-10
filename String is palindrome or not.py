#!/usr/bin/env python
# coding: utf-8

# # A program to find the strings is palindrome or not 

# In[ ]:


string = input("Enter the string :")

if string == string[::-1]:
    print("This is a palindrome string :",string)
else:
    print("This is not a palindrome string :",string)


# In[ ]:




