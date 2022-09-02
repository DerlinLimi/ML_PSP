# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 10:13:43 2022

@author: Lim
"""

import numpy as np
import pickle
import streamlit as st


loaded_model=pickle.load(open('D:\ML\st\ML_psp\psp_data.sav','rb'))


def psp_predict(age,bmi,elective_surgery,ethnicity,gender,height,icu_admit_source,icu_id,icu_stay_type,icu_type,pre_icu_los_days,weight,apache_2_diagnosis,apache_3j_diagnosis,apache_post_operative,arf_apache,gcs_eyes_apache,gcs_motor_apache,gcs_unable_apache,gcs_verbal_apache,heart_rate_apache,intubated_apache,map_apache,resprate_apache,temp_apache,ventilated_apache,d1_diasbp_max,d1_diasbp_min,d1_diasbp_noninvasive_max,d1_diasbp_noninvasive_min,d1_heartrate_max,d1_heartrate_min,d1_mbp_max,d1_mbp_min,d1_mbp_noninvasive_max,d1_mbp_noninvasive_min,d1_resprate_max,d1_resprate_min,d1_spo2_max,d1_spo2_min,d1_sysbp_max,d1_sysbp_min,d1_sysbp_noninvasive_max,d1_sysbp_noninvasive_min,d1_temp_max,d1_temp_min,h1_diasbp_max,h1_diasbp_min,h1_diasbp_noninvasive_max,h1_diasbp_noninvasive_min,h1_heartrate_max,h1_heartrate_min,h1_mbp_max,h1_mbp_min,h1_mbp_noninvasive_max,h1_mbp_noninvasive_min,h1_resprate_max,h1_resprate_min,h1_spo2_max,h1_spo2_min,h1_sysbp_max,h1_sysbp_min,h1_sysbp_noninvasive_max,h1_sysbp_noninvasive_min,d1_glucose_max,d1_glucose_min,d1_potassium_max,d1_potassium_min,apache_4a_hospital_death_prob,apache_4a_icu_death_prob,aids,cirrhosis,diabetes_mellitus,hepatic_failure,immunosuppression,leukemia,lymphoma,solid_tumor_with_metastasis,apache_3j_bodysystem,apache_2_bodysystem):
    # {'African American': 0, 'Asian': 1, 'Caucasian': 2, 'Hispanic': 3, 'Native American': 4, 'Other/Unknown': 5}
  if ethnicity == 'African American':
    ethnicity = 0
  elif ethnicity == 'Asian':
    ethnicity = 1
  elif ethnicity == 'Caucasian':
    ethnicity = 2
  elif ethnicity == 'Hispanic':
    ethnicity = 3
  elif ethnicity == 'Native American':
    ethnicity = 4
  elif ethnicity == 'Other/Unknown':
    ethnicity = 5
  
  # {'F': 0, 'M': 1}
  if gender == 'F':
    gender = 0
  elif gender == 'M':
    gender = 1

  # {'Accident & Emergency': 0, 'Floor': 1, 'Operating Room / Recovery': 2, 'Other Hospital': 3, 'Other ICU': 4}
  if icu_admit_source == 'Accident & Emergency':
    icu_admit_source = 0
  elif icu_admit_source == 'Floor':
    icu_admit_source = 1
  elif icu_admit_source == 'Operating Room / Recovery':
    icu_admit_source = 2
  elif icu_admit_source == 'Other Hospital':
    icu_admit_source = 3
  elif icu_admit_source == 'Other ICU':
    icu_admit_source = 4
  
  # {'admit': 0, 'readmit': 1, 'transfer': 2}
  if icu_stay_type == 'admit':
    icu_stay_type = 0
  if icu_stay_type == 'readmit':
    icu_stay_type = 1
  if icu_stay_type == 'transfer':
    icu_stay_type = 2

  # {'Cardiac ICU': 0, 'CCU-CTICU': 1, 'CSICU': 2, 'CTICU': 3, 'Med-Surg ICU': 4, 'MICU': 5, 'Neuro ICU': 6, 'SICU':7}
  if icu_type == 'Cardiac ICU':
    icu_type = 0
  elif icu_type =='CCU-CTICU':
    icu_type= 1
  elif icu_type =='CSICU':
    icu_type= 2
  elif icu_type =='CTICU':
    icu_type= 3
  elif icu_type =='Med-Surg ICU':
    icu_type= 4
  elif icu_type =='MICU':
    icu_type= 5
  elif icu_type =='Neuro ICU':
    icu_type= 6
  elif icu_type =='SICU':
    icu_type= 7

  # {'Cardiovascular': 0, 'Gastrointestinal': 1, 'Genitourinary': 2, 'Gynecological': 3, 'Hematological': 4, 'Metabolic': 5, 'Musculoskeletal/Skin': 6, 'Neurological': 7, 'Respiratory': 8, 'Sepsis': 9, 'Trauma': 10}
  if apache_3j_bodysystem == 'Cardiovascular':
    apache_3j_bodysystem = 0
  elif apache_3j_bodysystem == 'Gastrointestinal':
    apache_3j_bodysystem = 1
  elif apache_3j_bodysystem == 'Gynecological':
    apache_3j_bodysystem = 2
  elif apache_3j_bodysystem == 'Gastrointestinal':
    apache_3j_bodysystem = 3
  elif apache_3j_bodysystem == 'Hematological':
    apache_3j_bodysystem = 4
  elif apache_3j_bodysystem == 'Metabolic':
    apache_3j_bodysystem = 5
  elif apache_3j_bodysystem == 'Musculoskeletal/Skin':
    apache_3j_bodysystem = 6
  elif apache_3j_bodysystem == 'Neurological':
    apache_3j_bodysystem = 7
  elif apache_3j_bodysystem == 'Respiratory':
    apache_3j_bodysystem = 8
  elif apache_3j_bodysystem == 'Sepsis':
    apache_3j_bodysystem = 9
  elif apache_3j_bodysystem == 'Trauma':
    apache_3j_bodysystem = 10

  # apache_2_bodysystem_mapping = {'Cardiovascular': 0, 'Gastrointestinal': 1, 'Haematologic': 2, 'Metabolic': 3, 'Neurologic': 4, 'Renal/Genitourinary': 5, 'Respiratory': 6, 'Trauma': 7, 'Undefined diagnoses': 8}
  if apache_2_bodysystem == 'Cardiovascular':
    apache_2_bodysystem = 0
  elif apache_2_bodysystem == 'Gastrointestinal':
    apache_2_bodysystem = 1
  elif apache_2_bodysystem == 'Haematologic':
    apache_2_bodysystem = 2
  elif apache_2_bodysystem == 'Metabolic':
    apache_2_bodysystem = 3
  elif apache_2_bodysystem == 'Neurologic':
    apache_2_bodysystem = 4
  elif apache_2_bodysystem == 'Renal/Genitourinary':
    apache_2_bodysystem = 5
  elif apache_2_bodysystem == 'Respiratory':
    apache_2_bodysystem = 6
  elif apache_2_bodysystem == 'Trauma':
    apache_2_bodysystem = 7
  elif apache_2_bodysystem == 'Undefined diagnoses':
    apache_2_bodysystem = 8
    
  prediction_PSP=np.array([age,bmi,elective_surgery,ethnicity,gender,height,icu_admit_source,icu_id,icu_stay_type,icu_type,pre_icu_los_days,weight,apache_2_diagnosis,apache_3j_diagnosis,apache_post_operative,arf_apache,gcs_eyes_apache,gcs_motor_apache,gcs_unable_apache,gcs_verbal_apache,heart_rate_apache,intubated_apache,map_apache,resprate_apache,temp_apache,ventilated_apache,d1_diasbp_max,d1_diasbp_min,d1_diasbp_noninvasive_max,d1_diasbp_noninvasive_min,d1_heartrate_max,d1_heartrate_min,d1_mbp_max,d1_mbp_min,d1_mbp_noninvasive_max,d1_mbp_noninvasive_min,d1_resprate_max,d1_resprate_min,d1_spo2_max,d1_spo2_min,d1_sysbp_max,d1_sysbp_min,d1_sysbp_noninvasive_max,d1_sysbp_noninvasive_min,d1_temp_max,d1_temp_min,h1_diasbp_max,h1_diasbp_min,h1_diasbp_noninvasive_max,h1_diasbp_noninvasive_min,h1_heartrate_max,h1_heartrate_min,h1_mbp_max,h1_mbp_min,h1_mbp_noninvasive_max,h1_mbp_noninvasive_min,h1_resprate_max,h1_resprate_min,h1_spo2_max,h1_spo2_min,h1_sysbp_max,h1_sysbp_min,h1_sysbp_noninvasive_max,h1_sysbp_noninvasive_min,d1_glucose_max,d1_glucose_min,d1_potassium_max,d1_potassium_min,apache_4a_hospital_death_prob,apache_4a_icu_death_prob,aids,cirrhosis,diabetes_mellitus,hepatic_failure,immunosuppression,leukemia,lymphoma,solid_tumor_with_metastasis,apache_3j_bodysystem,apache_2_bodysystem]).reshape(1,-1)
  prediction=loaded_model.predict(prediction_PSP)
  #print(prediction)

  if (prediction[0]==0):
    return 'The Person will Survive'
  else:
    return 'The Person will not Survive'
  #return prediction_PSP

    
def main():
    st.title('PATIENT SURVIVAL PREDICTION')
    st.sidebar.header('Enter the patient details:')


    age=st.sidebar.slider('Patient Age:',1, 120, value=10)
    bmi=st.sidebar.text_input('Enter Patient BMI:')
    elective_surgery=st.sidebar.selectbox('Elective Surgery:', [0,1])
    ethnicity=st.sidebar.selectbox('Ethnicity:',['African American', 'Asian', 'Caucasian', 'Hispanic', 'Native American', 'Other/Unknown'])
    gender=st.sidebar.selectbox('Select Gender:',['F','M'])
    height=st.sidebar.text_input('Enter Patient Height:')
    icu_admit_source=st.sidebar.selectbox('ICU Admit Scource:',['Accident & Emergency', 'Floor', 'Operating Room / Recovery', 'Other Hospital', 'Other ICU'])
    icu_id=st.sidebar.text_input('Enter ICU ID:')
    icu_stay_type=st.sidebar.selectbox('ICU Stay Type:',['admit', 'readmit', 'transfer'])
    icu_type=st.sidebar.selectbox('ICU Type:',['Cardiac ICU', 'CCU-CTICU', 'CSICU', 'CTICU', 'Med-Surg ICU', 'MICU', 'Neuro ICU', 'SICU'])
    pre_icu_los_days=st.sidebar.text_input('Pre ICU Los_days:')
    weight=st.sidebar.text_input('Enter Patient Weight:')
    apache_2_diagnosis=st.sidebar.text_input('Enter apache_2_diagnosis:')
    apache_3j_diagnosis=st.sidebar.text_input('Enter apache_3j_diagnosis:')
    apache_post_operative=st.sidebar.selectbox('Enter apache_post_operative:', [0,1])
    arf_apache=st.sidebar.selectbox('Enter arf_apache:', [0,1])
    gcs_eyes_apache=st.sidebar.selectbox('Enter gcs_eyes_apache:', [1,2,3,4])
    gcs_motor_apache=st.sidebar.selectbox('Enter gcs_motor_apache:', [1,2,3,4,5,6])
    gcs_unable_apache=st.sidebar.selectbox('Enter gcs_unable_apache:', [0,1])
    gcs_verbal_apache=st.sidebar.selectbox('Enter gcs_verbal_apache :', [1,2,3,4,5])
    heart_rate_apache=st.sidebar.text_input('Enter heart_rate_apache:')
    intubated_apache=st.sidebar.selectbox('Enter intubated_apache:', [0,1])
    map_apache=st.sidebar.slider('Drag map_apache:',35, 250, value=40)
    resprate_apache=st.sidebar.number_input('Enter resprate_apache:',min_value=3,max_value=65,value=10)
    temp_apache=st.sidebar.slider('Drag temp_apache:',32.0, 40.0, value=33.5)
    ventilated_apache=st.sidebar.selectbox('Enter ventilated_apache:', [0,1])
    d1_diasbp_max=st.sidebar.text_input('Enter d1_diasbp_max:')
    d1_diasbp_min=st.sidebar.text_input('Enter d1_diasbp_min:')
    d1_diasbp_noninvasive_max=st.sidebar.text_input('Enter d1_diasbp_noninvasive_max:')
    d1_diasbp_noninvasive_min=st.sidebar.text_input('Enter d1_diasbp_noninvasive_min:')
    d1_heartrate_max=st.sidebar.text_input('Enter d1_heartrate_max:')
    d1_heartrate_min=st.sidebar.text_input('Enter d1_heartrate_min:')
    d1_mbp_max=st.sidebar.text_input('Enter d1_mbp_max:')
    d1_mbp_min=st.sidebar.text_input('Enter d1_mbp_min:')
    d1_mbp_noninvasive_max=st.sidebar.text_input('Enter d1_mbp_noninvasive_max:')
    d1_mbp_noninvasive_min=st.sidebar.text_input('Enter d1_mbp_noninvasive_min:')
    d1_resprate_max=st.sidebar.text_input('Enter d1_resprate_max:')
    d1_resprate_min=st.sidebar.text_input('Enter d1_resprate_min:')
    d1_spo2_max=st.sidebar.text_input('Enter d1_spo2_max:')
    d1_spo2_min=st.sidebar.text_input('Enter d1_spo2_min:')
    d1_sysbp_max=st.sidebar.text_input('Enter d1_sysbp_max:')
    d1_sysbp_min=st.sidebar.text_input('Enter d1_sysbp_min:')
    d1_sysbp_noninvasive_max=st.sidebar.text_input('Enter d1_sysbp_noninvasive_max:')
    d1_sysbp_noninvasive_min=st.sidebar.text_input('Enter d1_sysbp_noninvasive_min:')
    d1_temp_max=st.sidebar.slider('Drag d1_temp_max:',32.0, 40.0, value=33.5)
    d1_temp_min=st.sidebar.slider('Drag d1_temp_min:',32.0, 40.0, value=33.5)
    h1_diasbp_max=st.sidebar.text_input('Enter h1_diasbp_max:')
    h1_diasbp_min=st.sidebar.text_input('Enter h1_diasbp_min:')
    h1_diasbp_noninvasive_max=st.sidebar.text_input('Enter h1_diasbp_noninvasive_max:')
    h1_diasbp_noninvasive_min=st.sidebar.text_input('Enter h1_diasbp_noninvasive_min:')
    h1_heartrate_max=st.sidebar.text_input('Enter h1_heartrate_max:')
    h1_heartrate_min=st.sidebar.text_input('Enter h1_heartrate_min:')
    h1_mbp_max=st.sidebar.text_input('Enter h1_mbp_max:')
    h1_mbp_min=st.sidebar.text_input('Enter h1_mbp_min:')
    h1_mbp_noninvasive_max=st.sidebar.text_input('Enter h1_mbp_noninvasive_max:')
    h1_mbp_noninvasive_min=st.sidebar.text_input('Enter h1_mbp_noninvasive_min:')
    h1_resprate_max=st.sidebar.text_input('Enter h1_resprate_max:')
    h1_resprate_min=st.sidebar.text_input('Enter h1_resprate_min:')
    h1_spo2_max=st.sidebar.text_input('Enter h1_spo2_max:')
    h1_spo2_min=st.sidebar.text_input('Enter h1_spo2_min:')
    h1_sysbp_max=st.sidebar.text_input('Enter h1_sysbp_max:')
    h1_sysbp_min=st.sidebar.text_input('Enter h1_sysbp_min:')
    h1_sysbp_noninvasive_max=st.sidebar.text_input('Enter h1_sysbp_noninvasive_max:')
    h1_sysbp_noninvasive_min=st.sidebar.text_input('Enter h1_sysbp_noninvasive_min:')
    d1_glucose_max=st.sidebar.text_input('Enter d1_glucose_max:')
    d1_glucose_min=st.sidebar.text_input('Enter d1_glucose_min:')
    d1_potassium_max=st.sidebar.text_input('Enter d1_potassium_max:')
    d1_potassium_min=st.sidebar.text_input('Enter d1_potassium_min:')
    apache_4a_hospital_death_prob=st.sidebar.text_input('Enter apache_4a_hospital_death_prob:')
    apache_4a_icu_death_prob=st.sidebar.text_input('Enter apache_4a_icu_death_prob:')
    aids=st.sidebar.selectbox('Select the patient affected by Aids or not:', [0,1])
    cirrhosis=st.sidebar.selectbox('Enter cirrhosis:', [0,1])
    diabetes_mellitus=st.sidebar.selectbox('Enter diabetes_mellitus:', [0,1])
    hepatic_failure=st.sidebar.selectbox('Enter hepatic_failure:', [0,1])
    immunosuppression=st.sidebar.selectbox('Enter immunosuppression:', [0,1])
    leukemia=st.sidebar.selectbox('Enter leukemia:', [0,1])
    lymphoma=st.sidebar.selectbox('Enter lymphoma:', [0,1])
    solid_tumor_with_metastasis=st.sidebar.selectbox('Enter solid_tumor_with_metastasis:', [0,1])
    apache_3j_bodysystem=st.sidebar.selectbox('Select apache_3j_bodysystem:',['Cardiovascular', 'Gastrointestinal', 'Genitourinary', 'Gynecological', 'Hematological', 'Metabolic', 'Musculoskeletal/Skin', 'Neurological', 'Respiratory', 'Sepsis', 'Trauma']) 
    apache_2_bodysystem=st.sidebar.selectbox('Select apache_2_bodysystem:',['Cardiovascular', 'Gastrointestinal', 'Haematologic', 'Metabolic', 'Neurologic', 'Renal/Genitourinary', 'Respiratory', 'Trauma', 'Undefined diagnoses'])



    hospital_death=''

    
    
    if st.button('Survival Prediction'):
        hospital_death = psp_predict(age,bmi,elective_surgery,ethnicity,gender,height,icu_admit_source,icu_id,icu_stay_type,icu_type,pre_icu_los_days,weight,apache_2_diagnosis,apache_3j_diagnosis,apache_post_operative,arf_apache,gcs_eyes_apache,gcs_motor_apache,gcs_unable_apache,gcs_verbal_apache,heart_rate_apache,intubated_apache,map_apache,resprate_apache,temp_apache,ventilated_apache,d1_diasbp_max,d1_diasbp_min,d1_diasbp_noninvasive_max,d1_diasbp_noninvasive_min,d1_heartrate_max,d1_heartrate_min,d1_mbp_max,d1_mbp_min,d1_mbp_noninvasive_max,d1_mbp_noninvasive_min,d1_resprate_max,d1_resprate_min,d1_spo2_max,d1_spo2_min,d1_sysbp_max,d1_sysbp_min,d1_sysbp_noninvasive_max,d1_sysbp_noninvasive_min,d1_temp_max,d1_temp_min,h1_diasbp_max,h1_diasbp_min,h1_diasbp_noninvasive_max,h1_diasbp_noninvasive_min,h1_heartrate_max,h1_heartrate_min,h1_mbp_max,h1_mbp_min,h1_mbp_noninvasive_max,h1_mbp_noninvasive_min,h1_resprate_max,h1_resprate_min,h1_spo2_max,h1_spo2_min,h1_sysbp_max,h1_sysbp_min,h1_sysbp_noninvasive_max,h1_sysbp_noninvasive_min,d1_glucose_max,d1_glucose_min,d1_potassium_max,d1_potassium_min,apache_4a_hospital_death_prob,apache_4a_icu_death_prob,aids,cirrhosis,diabetes_mellitus,hepatic_failure,immunosuppression,leukemia,lymphoma,solid_tumor_with_metastasis,apache_3j_bodysystem,apache_2_bodysystem)
        st.success(hospital_death)
    
        
        

if __name__== '__main__':
    main()
    









