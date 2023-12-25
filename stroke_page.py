import pickle
import pandas as pd
import streamlit as st


stroke_model = pickle.load(open(".\models\stroke_model.pkl", "rb"))

males = {"Муж": 1, "Жен": 0}
ever_married = {"Да": 1, "Нет": 0}
hypertension = {"Да": 1, "Нет": 0}
heart_disease = {"Да": 1, "Нет": 0}
residence_type = {"Городской": 1, "Сельский": 0}

work_type = {
    "Никогда не работал": "work_type_Never_worked",
    "Официально трудоустроен": "work_type_Private",
    "Самозанятый": "work_type_Self_employed",
    "Ребенок": "work_type_children",
}
work_type_val = {
    "work_type_Never_worked": 0,
    "work_type_Private": 0,
    "work_type_Self_employed": 0,
    "work_type_children": 0,
}

smoke_status = {
    "Никогда не курил": "smoking_status_never_smoked",
    "Раньше курил": "smoking_status_formerly_smoked",
    "Курю": "smoking_status_smokes",
}
smoke_status_val = {
    "smoking_status_never_smoked": 0,
    "smoking_status_formerly_smoked": 0,
    "smoking_status_smokes": 0,
}


def get_stroke_page():
    st.title("Прогноз инсульта")
    col1, col2 = st.columns(2)

    with col1:
        age = st.text_input("Возраст")

    with col2:
        option = st.selectbox("Пол", males.keys(), 0)
        gender_Male = males[option]

    with col1:
        avg_glucose_level = st.text_input("Уровень глюкозы (мг/дл)")

    with col2:
        bmi = st.text_input("Индекс массы тела")

    with col1:
        option = st.selectbox("Когда-либо был женат?", ever_married.keys(), 0)
        ever_married_Yes = ever_married[option]

    with col2:
        option = st.selectbox("Тип работы", work_type.keys(), 0)
        work_type_val[work_type[option]] = 1
        work_type_Never_worked = work_type_val["work_type_Never_worked"]
        work_type_Private = work_type_val["work_type_Private"]
        work_type_Self_employed = work_type_val["work_type_Self_employed"]
        work_type_children = work_type_val["work_type_children"]

    with col1:
        option = st.selectbox("Тип проживания", residence_type.keys(), 0)
        Residence_type_Urban = residence_type[option]

    with col2:
        option = st.selectbox("Курите", smoke_status.keys(), 0)
        smoke_status_val[smoke_status[option]] = 1
        smoking_status_never_smoked = smoke_status_val["smoking_status_never_smoked"]
        smoking_status_formerly_smoked = smoke_status_val[
            "smoking_status_formerly_smoked"
        ]
        smoking_status_smokes = smoke_status_val["smoking_status_smokes"]

    with col1:
        option = st.selectbox("Гипертония?", hypertension.keys(), 0)
        hypertension_1 = hypertension[option]

    with col2:
        option = st.selectbox("Сердечные заболевания?", heart_disease.keys(), 0)
        heart_disease_1 = heart_disease[option]

    result = ""

    if st.button("Прогноз"):
        df = pd.DataFrame(
            {
                "age": age,
                "avg_glucose_level": avg_glucose_level,
                "bmi": bmi,
                "gender_Male": gender_Male,
                "hypertension_1": hypertension_1,
                "heart_disease_1": heart_disease_1,
                "ever_married_Yes": ever_married_Yes,
                "work_type_Never_worked": work_type_Never_worked,
                "work_type_Private": work_type_Private,
                "work_type_Self-employed": work_type_Self_employed,
                "work_type_children": work_type_children,
                "Residence_type_Urban": Residence_type_Urban,
                "smoking_status_formerly smoked": smoking_status_formerly_smoked,
                "smoking_status_never smoked": smoking_status_never_smoked,
                "smoking_status_smokes": smoking_status_smokes,
            },
            index=[0],
        )

        prediction = stroke_model.predict(df)[0]

        if prediction == 1:
            result = "Вы подвержены инсульту"
        else:
            result = "Вы не подвержены инсульту"

    st.success(result)
