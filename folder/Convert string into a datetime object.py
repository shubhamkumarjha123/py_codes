#!/usr/bin/env python
# coding: utf-8

# # Convert string into a datetime object.

# In[2]:


from datetime import datetime

date_string = "Feb 25 2020  4:20PM"
datetime_object = datetime.strptime(date_string, '%b %d %Y %I:%M%p')
print(datetime_object)


# In[ ]:




