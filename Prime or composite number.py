#!/usr/bin/env python
# coding: utf-8

# # A program to find the number is prime or composite

# In[ ]:


num = int(input("Enter the number :"))

count = 0;

for i in range(1,num):
    if num % i == 0:
        count = count+1
if count > 2:
    print("%d is the composite number "%num)
else:
    print("%d is the prime " %num)


# In[ ]:




