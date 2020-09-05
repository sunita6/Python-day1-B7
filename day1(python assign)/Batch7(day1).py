#!/usr/bin/env python
# coding: utf-8

# # List and it default functions
# 

# In[2]:


lst=["sunita",20,29.87,[1,2,3]]


# In[3]:


lst


# In[4]:


lst.append(45)


# In[5]:


lst


# In[7]:


lst.copy()


# In[14]:


lst.count('sunita')


# In[16]:


lst.append(45)


# In[17]:


lst


# In[18]:


lst.count(45)


# In[21]:


lst.remove(45)


# In[23]:


lst


# In[28]:


lst.sort()


# In[31]:


list1=[20,30,40,10,20,10,50,30]
list1


# In[32]:


list1.sort()


# In[33]:


list1


# In[36]:


lst.pop(2)


# In[37]:


lst


# In[41]:


lst.clear()


# In[42]:


lst


# # dictionary and its default function

# In[26]:


dct={"name":"sunita","age":"27","number":"4567","email":"sunita07@gmail.com"}
dct


# In[27]:


dct.get("name")


# In[13]:


a={1:"one",2:"two",3:"four"}
b={3:"three"}
a.update(b)
print(a)


# In[28]:


dct.popitem()


# In[29]:


dct


# In[30]:


dct.setdefault(4)


# In[31]:


dct


# In[32]:


x=('a','b','c','d')
y=5
print(dct.fromkeys(x,y))


# In[34]:


dict.keys(a)


# # Sets and default Functions

# In[35]:


st={"sunita","letsupgrade",1,2,3,4,5,"chauhan",2.5,5.6}


# In[36]:


st


# In[37]:


st.add("learning Python")


# In[38]:


st


# In[39]:


st1={'chauhan'}
st1.issubset(st)


# In[51]:


print("set1:",st)
print("set2:",st3)
st3={1,2,3,'shetty'}
print("Intersection set:",st3.intersection(st))


# In[54]:


print("set1:",st)
print("set2:",st1)
st.isdisjoint(st1)


# In[57]:


st3={11,22,33,44}
st1.isdisjoint(st3)


# In[64]:


x=set.copy(st3)


# In[65]:


x


# In[68]:


print("set1",st)
print("set2",st1)
print("difference set",st.difference(st1))


# # Tupple and default function

# In[70]:


tup=("sunita","@","gmail.com","@")
tup


# In[71]:


tup.count("@")


# In[73]:


tup.index("gmail.com")


# In[75]:


print(tup[0:2])


# In[76]:


print(tup[:3])


# In[77]:


print(tup[-3:-1])


# In[78]:


tup1=(1,2,3,4)
res=tup+tup1
print(res)


# In[80]:


print(tup.index('sunita'))


# # String and Default functions

# In[81]:


str="Hello everyone"
str


# In[83]:


str1="welcome"
str1.capitalize()


# In[87]:


str.endswith('e')


# In[88]:


str.endswith('m')


# In[90]:


str1.format()


# In[94]:


print(str)
str.find('o')


# In[96]:


str1.encode()

