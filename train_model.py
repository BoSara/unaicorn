#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier



data = pd.read_csv('heart-disease.csv')


x = data.drop(['target'], axis=1)
y = data['target']


x_train, x_test, y_train, y_test = train_test_split(x , y ,test_size = 0.2)


rfc = RandomForestClassifier()
rfc_model = rfc.fit(x_train, y_train)
y_pred = rfc_model.predict(x_test)

import pickle

filename = 'heart_model.sav'
pickle.dump(rfc_model,open(filename, 'wb'))


# In[ ]:




