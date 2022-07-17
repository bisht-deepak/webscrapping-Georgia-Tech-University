#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#dated 21st of May, 2022


# In[1]:


import requests
from bs4 import BeautifulSoup
import re
import pandas as pd


# In[2]:


#important links
georgiaTechBaseURL= "https://www.ece.gatech.edu/faculty-staff-directory"
landingPageURL= "?field_group_filter_value=1"


# In[3]:


#preparing soup
with requests.Session() as s:
    root= s.get(georgiaTechBaseURL+landingPageURL)
    soup = BeautifulSoup(root.text, "html.parser")


# In[8]:


grandList= []
for i in range(0, 129, 1):
    d= {}
    
    name= soup.find_all("div", {"class": "field-full-name"})[i]
    d["name"]= name.find("a").text
    
    title= soup.find_all("div", {"class": "field-jobtitle"})[i]
    d["jobtitle"]= title.text.replace("\n", "").replace(" ", "")

    mailid= soup.find_all('a', attrs={"href": re.compile("^mailto:")})[i]
    d["email_address"]= mailid.get('href')[7:]
        
    phone= soup.find_all("div", {"class": "field-work-phone"})[i]
    phone= phone.text.replace("\n", "").replace(" ", "")
    if phone== "":
        d["work_phone"]= None
    else:
        d["work_phone"]= phone
    
    #extract office address
    try:
        office= soup.find_all("div", {"class": "faculty-staff-content"})[i]
        d["office_address"]= office.find("div", {"class": "field-office"}).text.replace("\n", "").replace(" ", "") 
        #problem faced- total listings= 129, total offices= 116
    except:
        d["office_address"]= None   
    grandList.append(d)


# In[9]:


dF= pd.DataFrame(grandList)


# In[10]:


dF.head(5)


# In[214]:


dF.to_csv("Georgia Tech Landing Page.csv")


# In[233]:


#completed 24th of May, 2022

