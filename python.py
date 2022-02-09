# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 11:21:48 2022

@author: n
"""

import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

URL = "https://www.cs.unc.edu/~saba/COMP_classes/index.html"
page = requests.get(URL)
x=(page.text)
soup = BeautifulSoup(page.content, "html.parser")
job_elements = list(soup.find_all('table'))
table_MN = (pd.read_html("https://www.cs.unc.edu/~saba/COMP_classes/index.html"))[0].to_numpy()
x=np.delete(table_MN,np.arange(1,len(table_MN),2),0)
x.tofile('sample1.csv',sep=',')
print("hello world")
    

