#!/usr/bin/env python
# coding: utf-8

# ## Grammer checkter using Gingerit and deploying with stremalit

# In[2]:


#Install gingerit and streamlit
#!pip install gingerit
#!pip install streamlit


# In[3]:


#get_ipython().run_line_magic('load_ext', 'watermark')
#get_ipython().run_line_magic('load_ext', 'lab_black')


# In[6]:


from gingerit.gingerit import GingerIt
import gingerit
import streamlit as st

#get_ipython().run_line_magic('watermark', '-a "Sudarshan Koirala" -iv')


# In[8]:


st.title("Grammar & Spell Checker In Python")
text = st.text_area("Enter Text:", value="", height=None, max_chars=None, key=None)
parser = GingerIt()
if st.button("Correct Sentence"):
    if text == "":
        st.write("Please enter text for checking")
    else:
        result_dict = parser.parse(text)
        st.markdown("**Corrected Sentence - **" + str(result_dict["result"]))
else:
    pass


# In[9]:


# convert notebook to .py file
# !jupyter nbconvert --to script gingerit_and_streamlit.ipynb


# Run `streamlit run gingerit_and_streamlit.py` from the terminal

# In[ ]:




