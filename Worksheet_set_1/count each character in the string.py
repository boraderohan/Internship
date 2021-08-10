#!/usr/bin/env python
# coding: utf-8

# # A program to print the frequency of each of the character present in given string

# In[ ]:


string = input("Enter the string : ")
c = input("Enter character to check frequency : ")
count = 0

for i in string:
    if i == c:
        count = count+1
print(c,"Occurs ",count,"time(s).")


# In[ ]:




