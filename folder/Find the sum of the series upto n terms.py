#!/usr/bin/env python
# coding: utf-8

# # Find the sum of the series upto n terms.

# In[1]:


n = 5
# first number of sequence
start = 2
sum_seq = 0

# run loop n times
for i in range(0, n):
    print(start, end="+")
    sum_seq += start
    # calculate the next term
    start = start * 10 + 2
print("\nSum of above series is:", sum_seq)


# In[ ]:




