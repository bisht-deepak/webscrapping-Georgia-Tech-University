#!/usr/bin/env python
# coding: utf-8

# In[1]:


#dated 24-02-2022


# In[2]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[3]:


baseURL= "https://ece.gatech.edu/faculty-staff-directory/"
facultyfilterURL= "?field_group_filter_value=1"
publicationsURL= "#publications-patents/"

root= requests.get(baseURL+facultyfilterURL)
soup= BeautifulSoup(root.text, "html.parser")

#access publications page
grandDict= {}
for i in range(129):
    authorName= soup.find_all("div", {"class": "field-full-name"})[i].text.replace("\n", "")
    authorURL= authorName.lower().replace(" ", "-")[:-1]
    root2= requests.get(baseURL+authorURL+publicationsURL)
    soup2= BeautifulSoup(root2.text, "html.parser")
    d= []
    try:
        branch= soup2.find("div", {"id":"publication-patents"})
        leaves= branch.findChildren("p")
         
        for j in range(len(leaves)):
            publication= leaves[j].text
            d.append(publication)
            j+=1    
    except:
        d.append("--------------------------NONE--------------------------------")
  
    i+=1
    grandDict[authorName]= d


# In[4]:


grandDict


# In[1]:


# dataFrame= pd.DataFrame(grandDict)


# In[ ]:




