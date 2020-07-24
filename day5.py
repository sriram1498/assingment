#!/usr/bin/env python
# coding: utf-8

# # sort it in ascending order but all zeros in right hand side

# In[1]:


list1=[0,1,2,10,4,1,0,56,2,0,1,3,0,56,0,4]


# In[2]:


list2=list1.sort(reverse=1)


# In[3]:


print(list1)


# # sort list

# In[10]:


list2=[10,20,40,60,70,80]


# In[11]:


list2.sort(reverse=1)


# In[13]:


print(list2)


# In[15]:


list3=[(10,4),(2,4),(6,7),(2,6)]


# In[16]:


def fun1(x):
    return x[0]+x[1]
list3.sort(key=fun1)
print(list3)


# In[ ]:




