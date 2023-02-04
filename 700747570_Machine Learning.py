#!/usr/bin/env python
# coding: utf-8

# In[9]:


#initializing for loop to print increment star pattern.
for i in range(1,6):
        print("*"*i)#for increasing star pattern
#initializing for loop to print decrement star pattern.
for i in range(4,0,-1):
        print("*"*i)#for decreasing star pattern.


# In[10]:


#initializing list.
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#using for loop to print the elements in odd indexes
for i in my_list[1::2]:
    print(i,end=' ')


# In[11]:


#initializing list.
x = [23,'Python', 23.98]
#initializing empty list to append.
n=[]
length = len(x)
#initializing for loop to extract elements.
for i in range(length):
    n.append(type(x[i]))
#printing the list and its datatypes
print(x)
print(n)


# In[5]:


#initializing the list.
Sample_List=[1,2,3,3,3,3,4,5]
Unique_List=[]
#for loop to print the unique elements from the list.
for i in Sample_List:
    if i not in Unique_List:
        Unique_List.append(i)
print(Sample_List)
print(Unique_List)


# In[12]:


#it takes user input.
s= input('Enter your string:')
#initializing the variables
upper_case=lower_case=0
#initializing for loop.
for i in s:
    #checking if the letter is upper letter.
    if i.isupper():#it returns true if all the letters are uppercase else false.
        upper_case+=1
    elif i.islower():
        lower_case+=1
    else:
        pass
#printing the upper case.
print("No. of upper-case characters",upper_case)
#printing the lower case.
print("No. of lower-case Characters",lower_case)


# In[ ]:




