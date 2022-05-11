# -*- coding: utf-8 -*-
"""
Created on Wed May 11 18:47:58 2022

@author: PRIYANKA
"""

import pandas as pd
import numpy as np
import pickle
import streamlit as st


#loading the saved model
loaded_model=pickle.load(open("C:\\Users\\PRIYANKA\\excelr_p\\trained_model.save",'rb'))

#CREATING A FUNCTION FOR PREDICTION

def insurance_prediction(input_data):

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return'The claim is fraud'
    else:
      return'The claim is genuine'
    
      
def main():
    # giving the title
    st.title("HEALTH INSURANCE PREDICTION")
    

    #getting the input data from user
    Age=st.text_input("SELECT AGE :('0 to 17':1, '18 to 29':2,'30 to 49':3,'50 to 69':4,'70 or Older':5)")
    Gender=st.text_input("SELECT GENDER :('F':0, 'M':1, 'U':2 )")
    Days_spend_hsptl=st.text_input("DAYS SPENT IN HOSPITAL")
    Admission_type=st.text_input("SELECT TYPE OF ADMISSION : ('Elective':0, 'Urgent':1, 'Emergency':2, 'Newborn':3, 'Not Available':5,'Trauma':4)")
    ccs_diagnosis_code=st.text_input("CSS DIAGNOSIS CODE ")
    Code_illness=st.text_input("CODE OF ILLNESS")
    Surg_Description=st.text_input("SURGICAL DESCRIPTION:('Medical':0, 'Surgical':1)")
    Emergency_dept=st.text_input("EMERGENCY DEARTMENT :('Y':0, 'N':1)")
    Tot_charg=st.text_input("TOTAL CHARGE")
    Tot_cost=st.text_input("TOTAL COST")
    Payment_Typology=st.text_input("TYPE OF PAYMENT")
    
    #code for prediction
    insurance_claim=''
    
    if st.button("PREDICT"):
       insurance_claim=insurance_prediction([Age,Gender,Days_spend_hsptl,Admission_type,ccs_diagnosis_code,Code_illness,Surg_Description,Emergency_dept,Tot_charg,Tot_cost,Payment_Typology])
    
    st.success(insurance_claim)     

if __name__=='__main__':
    main()
     
