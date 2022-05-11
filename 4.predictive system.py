# -*- coding: utf-8 -*-
"""
Created on Wed May 11 19:15:15 2022

@author: PRIYANKA
"""

import numpy as np
import pickle

#loading the saved model
loaded_model=pickle.load(open("C:\\Users\\PRIYANKA\\excelr_p\\trained_model.sav",'rb'))

input_data = (5,0,3,0,122,2,0,0,3418.18,3370.87,1)

# changing the input_data to numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array as we are predicting for one instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0] == 0):
  print('The claim is fraud')
else:
  print('The claim is genuine')