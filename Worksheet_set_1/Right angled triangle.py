#!/usr/bin/env python
# coding: utf-8

# In[ ]:


choice = input("which side(a,b,c) do you want to calculate :")
if choice == 'c':
    a = float(input("Enter the length of side a :"))
    b = float(input("Enter the length of side b :"))
    c =  (a * a  + b * b)**0.5
    print("The length of side c %f"%(c))
elif choice == 'b':
    a = float(input ("Enter the length of side a :"))
    c = float(input("Enter the length of side c :"))
    b = (c*c - a*a)**0.5
    print("The length of the side c %f: "%(b))
elif choice == 'a':
    b = float(input('Enter the length of b side :'))
    c = float(input('Enter the length of c side :'))
    a = (c*c - b*b)**0.5
    print("The length of the side a %f"%(a))
else:
    print('Invalid Input')


# In[ ]:




