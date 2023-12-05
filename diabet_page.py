import pickle
import streamlit as st
import numpy as np
from sklearn.preprocessing import StandardScaler

diabet_model = pickle.load(open("diabet_model.pkl", "rb"))

def diabetes_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data)

    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    scaler = StandardScaler()
    std_data = scaler.fit_transform(input_data_reshaped)
    prediction = diabet_model.predict(std_data)
    return prediction
  
def get_diabet_page():
    st.title('Прогноз диабета')
    col1, col2 = st.columns(2)  

    with col1:
        Age = st.text_input('Возраст')

    with col2:
        Pregnancies = st.text_input('Количество беременностей')
        
    with col1:
        Glucose = st.text_input('Уровень глюкозы (мг/дл)')
    
    with col2:
        BloodPressure = st.text_input('Артериальное давление')
    
    with col1:
        SkinThickness = st.text_input('Толщина кожи')
    
    with col2:
        Insulin = st.text_input('Уровень инсулина (мг/дл)')
    
    with col1:
        BMI = st.text_input('Индекс массы тела')
    
    with col2:
        DiabetesPedigreeFunction = st.text_input('Риск наследственного диабета (0-1)')
    
    
    result = ''
    
    if st.button('Прогноз'):
        diab_prediction = diabetes_prediction([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
        
        if (diab_prediction[0] == 1):
          result = 'Вы диабетик'
        else:
          result = 'Вы не диабетик'
        
    st.success(result)
