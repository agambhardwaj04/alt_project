import streamlit as st
import joblib 
import numpy as np
st.set_page_config(
    page_title="Multi Disease Predictor",
    page_icon="🩺",  
    layout="wide"
)

def set_background_url(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )



#### Sidebar ####
st.sidebar.header("⚖️ Multi-Disease Predictor")
st.sidebar.markdown("\n\n")
st.sidebar.header("🧭 Navigation")
st.sidebar.subheader("Please select the Disease you are concerned about.")
st.sidebar.markdown("\n\n")
st.sidebar.markdown("\n\n")
st.sidebar.markdown("\n\n")

#### ---- ####
#### INTRODUCTION ####

page = st.sidebar.selectbox("Choose from Below 👇", ["🌐 Home","🧠 Parkinson's", "💉 Diabetes", "🤰 Maternal Health","🫀 Heart Health","📊 Conclusions"])

if page == "🌐 Home":
    st.title("Multi-Disease Predictor Prediction App")
    st.header("Indroduction")
    st.write("Welcome to the Multi-Disease Prediction System")
    st.write("This application uses Machine Learning models to predict the likelihood of multiple diseases like Parkinsons, Diabetes, Heart Health and also predicts about Maternal Health based on user-provided health information. It's designed to assist in early detection and awareness, helping users understand potential health risks.It can be used by Healthcare Professionals, just give the input from your report to know about the disease")

    col1, col2 = st.columns([2,2])

    with col1:
        st.subheader("Parkinson's")
        st.image("https://www.ucl.ac.uk/comprehensive-clinical-trials-unit/sites/comprehensive_clinical_trials_unit/files/styles/medium_image/public/exenatide_2.jpg?itok=OeqYqx1P", use_container_width =True)
        with st.expander("Know more"):
          st.write("Parkinson's is a chronic and progressive neurological condition that affects the brain's ability to control movement. It results from the gradual loss of nerve cells in a region of the brain called the substantia nigra, which leads to a reduction in dopamine levels — a neurotransmitter essential for coordinating smooth and balanced muscle activity. The exact cause of Parkinson's disease is not fully understood, but it is thought to involve a combination of genetic predisposition and environmental triggers. While there is no known cure, early diagnosis and ongoing management can significantly improve a person's quality of life.")
        with st.expander("Symptoms"):
            st.subheader('Key Symptoms')
            st.write("* Tremors, especially in hands or fingers at rest")
            st.write("* Slowness of movement (bradykinesia)")
            st.write("* Freezing of gait (sudden inability to move")
            st.write("* Depression or anxiety")
            st.write("* Memory problems or confusion")
            st.write("* Balance problems and frequent falls")
            st.write("* Reduced facial expressions")
            st.write("* Shuffling walk or dragging of feet")     



    with col2: 
        st.subheader("Diabetes")
        st.image("Images/resized_image.png", use_container_width =True)
        with st.expander("Know more"):
          st.write("Diabetes is a chronic metabolic disorder that occurs when the body is unable to properly regulate blood glucose (sugar) levels. It results either from insufficient insulin production by the pancreas or the body's inability to effectively use the insulin it produces. There are several types of diabetes, with Type 1 and Type 2 being the most common. If not managed properly, diabetes can lead to serious long-term health complications affecting the heart, kidneys, eyes, and nerves. While there is no permanent cure, it can be effectively managed through lifestyle changes, medication, and regular monitoring of blood sugar levels.")


        with st.expander("Symptoms"):
          st.subheader('Key Symptoms')
          st.write("* Frequent urination (polyuria)")
          st.write("* Excessive thirst (polydipsia)")
          st.write("* Increased hunger (polyphagia)")
          st.write("* Fatigue or feeling tired")
          st.write("* Blurred vision")
          st.write("* Slow healing of cuts and wounds")
          st.write("* Frequent infections (e.g., skin, gum, or bladder infections)")
          st.write("* Dry mouth and itchy skin")  


    col3, col4 = st.columns(2)
    with col3:
      st.subheader("Maternal Health")
      st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT0gxNrFzm__0f95rwIL9A0abd0P3DEQS1q8w&s",use_container_width=True)
      with st.expander("Know more"):
          st.write("Maternal health focuses on the overall well-being of women throughout pregnancy, childbirth, and the postnatal period. It involves providing access to quality healthcare services, skilled birth attendants, and proper medical support to ensure a safe and healthy experience for both mother and child. Promoting maternal health is essential for reducing risks associated with childbirth and for supporting the long-term development of families and communities.")
          st.write("Poor maternal health refers to inadequate physical, emotional, or medical well-being of women during pregnancy, childbirth, or after delivery. It often results from limited access to quality healthcare, poor nutrition, lack of education, and social or economic barriers. When maternal health is neglected, it can lead to serious complications that affect both the mother and the baby")

      with st.expander("Symptoms"):
          st.subheader('Key Symptoms')
          st.write("* Persistent fatigue or weakness")
          st.write("* Excessive or prolonged nausea and vomiting")
          st.write("* Swelling in hands, feet, or face ")
          st.write("* Bleeding during pregnancy")
          st.write("* Delayed fetal movement or unusual baby activity")
          st.write("* Severe abdominal or pelvic pain")
          st.write("* Frequent headaches or vision problems")
          st.write("* Shortness of breath or chest pain")
          

    with col4:
        st.subheader("Heart Health")
        st.image("Images/resized_heart_image_344x289.jpg",use_container_width=True)
        with st.expander("Know more"):
            st.write("Heart health is essential for the proper functioning of the body, as the heart is responsible for pumping oxygen-rich blood to all organs and tissues. Maintaining good cardiovascular health supports energy levels, mental clarity, and the body’s ability to recover from illness or stress. It involves a combination of healthy lifestyle choices, such as eating nutrient-rich foods, staying physically active, managing stress, and getting regular medical check-ups. Factors like genetics, environment, and daily habits all influence heart health over time. Fostering heart health not only helps prevent life-threatening conditions but also contributes to a longer, more active, and fulfilling life..")
              

        with st.expander("Symptoms"):
              st.subheader('Key Symptoms')
              st.write("* Chest pain, tightness, or discomfort")
              st.write("* Shortness of breath, especially during activity or while lying down")
              st.write("* Irregular heartbeat (palpitations or fluttering)")
              st.write("* Cold sweats or nausea")
              st.write("* Fainting or near-fainting episodes")
              st.write("* Reduced ability to exercise or perform physical activities")
              st.write("* Swelling in legs, ankles, or feet (edema)")
              st.write("* Pain in the neck, jaw, throat, upper back, or arms")


elif page == "🧠 Parkinson's":
    
    set_background_url('https://images.unsplash.com/photo-1732454827988-95972d793f1b?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8OHx8ZGFyayUyMGJyYWluJTIwcGFya2luc29uJTIwYmFja2dyb3VuZGltYWdlc3xlbnwwfHwwfHx8MA%3D%3D')
    st.title("🧠 Parkinson's Predictor ")
    st.subheader("Please fill the values below from your Report")

    with st.form("in"):
        st.subheader("Input Values : ")

        features = []
        feature_names = [
            "MDVP:Fo(Hz)", "MDVP:Fhi(Hz)", "MDVP:Flo(Hz)", "MDVP:Jitter(%)", "MDVP:Jitter(Abs)","MDVP:RAP", "MDVP:PPQ", "Jitter:DDP", "MDVP:Shimmer", "MDVP:Shimmer(dB)",
            "Shimmer:APQ3", "Shimmer:APQ5", "MDVP:APQ", "Shimmer:DDA", "NHR", "HNR",
            "RPDE", "DFA", "spread1", "spread2", "D2", "PPE"
        ] 

        for name in feature_names:
            val = st.number_input(name, min_value=-100.0, max_value=200.0000, value=0.00, step=0.1,format='%.6g')
            features.append(val)

        submitted = st.form_submit_button("Submit")

        if submitted:
          scaler = joblib.load("Models/parkinson_scaler.joblib")
          model_parkinson = joblib.load("Models/parkinson.joblib")

          # Inside your form submission
          features_scaled = scaler.transform([features])
          prediction = model_parkinson.predict(features_scaled)


          if prediction[0] == 1:
            st.markdown(
              "<div style='color: white; background-color: red; padding: 8px; border-radius: 5px;'>"
              "⚠️ <strong>Parkinson’s Detected</strong>, Please contact a Doctor"
              "</div>",
                unsafe_allow_html=True
            )
          else:
            st.markdown(
              "<div style='color: white; background-color: green; padding: 8px; border-radius: 5px;'>"
              "✅ <strong>No Parkinson’s</strong>, but if you have symptoms, Please confirm with a Doctor"
              "</div>",
              unsafe_allow_html=True
            )

elif page == "💉 Diabetes":
    set_background_url('https://www.diabetesqualified.com.au/wp-content/uploads/2025/02/blood-drop-in-a-dome-future-tech-style-GettyImages-1485107320.png')
    st.title("💉 Diabetes Predictor")
    st.subheader("Please fill the values below from your Report")
    

    with st.form("in"):
        st.subheader("Input Values : ")

        features1 = []
        feature_names1 = [
            'Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age'
        ] 

        for name in feature_names1:
            val = st.number_input(name, min_value=0.0, max_value=541.0, value=0.00, step=1.0,format='%.3f')
            features1.append(val)

        submitted = st.form_submit_button("Submit")

        if submitted:
          scaler = joblib.load("Models/diabetes_scaler.joblib")
          model_diabetes = joblib.load("Models\diabetes.joblib")

          # Inside your form submission
          features_scaled = scaler.transform([features1])
          prediction1 = model_diabetes.predict(features_scaled)


          if prediction1[0] == 1:
            st.markdown(
              "<div style='color: white; background-color: red; padding: 8px; border-radius: 5px;'>"
              "⚠️ <strong>You have Diabetes.</strong> Please contact a Doctor"
              "</div>",
                unsafe_allow_html=True
            )
          else:
            st.markdown(
              "<div style='color: white; background-color: green; padding: 8px; border-radius: 5px;'>"
              "✅ <strong>No Diabetes detected</strong>, but if you have symptoms, Please confirm with a Doctor"
              "</div>",
              unsafe_allow_html=True
            )

elif page == "🤰 Maternal Health":
    set_background_url("https://images.unsplash.com/photo-1656267964814-88f33e184c5f?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTB8fG1hdGVybmFsJTIwaGVhbHRoJTIwZGFyayUyMGJhY2tncm91bmR8ZW58MHx8MHx8fDA%3D")
    st.title("🤰 Maternal Health Predictor")
    st.subheader("Please fill the values below from your Report")
    with st.form("in"):
        st.subheader("Input Values : ")

        features = []
        feature_names = [
            'Age','SystolicBP','DiastolicBP','BS','BodyTemp','HeartRate'
        ] 

        for name in feature_names:
            val = st.number_input(name, min_value=0.0, max_value=370.0, value=0.0, step=1.0,format='%.1f')
            features.append(val)

        submitted = st.form_submit_button("Submit")

        if submitted:
          scaler = joblib.load("Models/maternal_scaler.joblib")  
          model = joblib.load("Models/maternal.joblib")

          
          X_input = scaler.transform([features])  

          pred = model.predict(X_input)[0]


          risk_map = {0: "High Risk", 1: "Low Risk", 2: "Mid Risk"}  
          if pred == 0:
            st.markdown(
              "<div style='color: white; background-color: red; padding: 8px; border-radius: 5px;'>"
              "⚠️ <strong>High Risk Detected.</strong> Please contact a Doctor."
              "</div>",
              unsafe_allow_html=True
            )
          elif pred == 2:
            st.markdown(
              "<div style='color: black; background-color: yellow; padding: 8px; border-radius: 5px;'>"
              "🧑‍⚕️<strong>Mid Risk Detected.</strong> Please monitor your health and consult a doctor if needed."
              "</div>",
              unsafe_allow_html=True
            )
          else:
            st.markdown(
              "<div style='color: white; background-color: green; padding: 8px; border-radius: 5px;'>"
              "✅ <strong>No Risk Detected</strong>, but if you have symptoms, please confirm with a Doctor."
              "</div>",
              unsafe_allow_html=True
            ) 


elif page == "🫀 Heart Health":
    set_background_url('https://t3.ftcdn.net/jpg/15/58/90/42/360_F_1558904203_zER6SbU509l3MDaIjhEnYcUM2MAE6ysq.jpg')
    
    st.title(" Heart Health Predictor")
    st.subheader("Please fill the values below from your Report")
    with st.form("in"):
        st.subheader("Input Values : ")

        features2 = []
        feature_names2 = [
            'age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal'
        ]  

        for name in feature_names2:
            val = st.number_input(name, min_value=0.0, max_value=500.0, value=0.00, step=1.0,format='%.1f')
            features2.append(val)

        submitted = st.form_submit_button("Submit")
        if submitted:
          scaler = joblib.load("Models/heart_scaler.joblib")
          model_heart = joblib.load("Models/heart.joblib")

          # Inside your form submission
          features_scaled = scaler.transform([features2])
          prediction1 = model_heart.predict(features_scaled)


          if prediction1[0] == 1:
            st.markdown(
              "<div style='color: white; background-color: red; padding: 8px; border-radius: 5px;'>"
              "⚠️ <strong>Your Heart Health is poor.</strong> Please contact a Doctor"
              "</div>",
                unsafe_allow_html=True
            )
          else:
            st.markdown(
              "<div style='color: white; background-color: green; padding: 8px; border-radius: 5px;'>"
              "💓<strong>Healthy Heart Detected</strong>, but if you have symptoms, Please confirm with a Doctor"
              "</div>",
              unsafe_allow_html=True
            )

elif page == "📊 Conclusions":
    
    st.title("📊 Conclusions & Model Analysis")
    st.markdown("Review the performance of each disease prediction model below:")

    tab1, tab2, tab3, tab4 = st.tabs([
        "🧠 Parkinson's Disease",
        "💉 Diabetes",
        "🤰 Maternal Health",
        "🫀 Heart Disease"
    ])

    with tab1:
        st.header("🧠 Parkinson's Disease")

        with st.expander("🔍 Model Details"):
          st.markdown("""
        ### 🧪 **Model Summary**
        - ✅ **Model Used:** Random Forest Classifier  
        - 📏 **Scaler:** StandardScaler  
        - 🧬 **Encoding:** Not required  
        - 🧠 **Features Used:**
            - `MDVP:Fo(Hz)`
            - `MDVP:Flo(Hz)`
            - `MDVP:Jitter(%)`
            - `MDVP:Jitter(Abs)`
            - `MDVP:Shimmer(dB)`
            - `MDVP:RAP`
            - `MDVP:PPQ`
            - `Jitter:DDP`
            - `MDVP:Shimmer`
            - `Shimmer:APQ3`
            - `Shimmer:APQ5`
            - `MDVP:APQ`
            - `Shimmer:DDA`
            - `RPDE`
            - `DFA`
            - `NHR`
            - `HNR`
            - `DFA`
            - `spread1`
            - `spread2`
            - `D2`
            - `PPE`
        """)



        with st.expander("📈 Performance Metrics"):
            st.markdown("""
        ### ✅ **Performance Overview**
        - **Accuracy:** `95%`
        - **Precision:**  
          - ❌ No Parkinson's: `1.00`  
          - ✅ Parkinson's: `0.94`
        - **Recall:**  
          - ❌ No Parkinson's: `0.71`  
          - ✅ Parkinson's: `1.00`
        - **F1 Score:**  
          - ❌ No Parkinson's: `0.83`  
          - ✅ Parkinson's: `0.97`
        """)

        with st.expander("📊 Confusion Matrix and Visuals"):
            st.subheader("Least affecting Factors for Positive Parkinson's")
            st.image('Images/subplot_parkinson.png',caption="Least affecting Factors for Positive Parkinson's")
            st.subheader("Most affecting Factors for Positive Parkinson's")
            st.image('Images/subplot_parkinson_positive.png',caption="Factors affecting Most for Positive Parkinson's")
            st.subheader("Confusion Matrix")
            st.image("Images\cm_parkinson.png", caption="Confusion Matrix")

        with st.expander("🧠 Observations & Insights"):
            st.markdown("""
            - High accuracy due to robust vocal feature patterns.
            - Random Forest handles non-linearity and noise well.
            - Feature importance is high for jitter and shimmer measurements.
            """)

    with tab2:
        st.header("💉 Diabetes Prediction")
        with st.expander("🔍 Model Details"):
          st.markdown("""
        ### 🧪 **Model Summary**
        - ✅ **Model Used:** Random Forest Classifier 
        - 📏 **Scaler:** StandardScaler  
        - 🧠 **Features Used:**
            - `Pregnancies`
            - `Glucose`
            - `BloodPressure`
            - `SkinThickness`
            - `Insulin`
            - `BMI`
            - `DiabetesPedigreeFunction`
            - `Age`""",unsafe_allow_html=True
          )



        with st.expander("📈 Performance Metrics"):
           st.markdown("""
        ### ✅ **Performance Overview**
        - **Accuracy:** `79.2%`
        - **Precision:**  
          - 🟩 **No Diabetes (Class 0):** `0.79`  
          - 🟥 **Diabetes (Class 1):** `0.81`
        - **Recall:**  
          - 🟩 **No Diabetes (Class 0):** `0.93`  
          - 🟥 **Diabetes (Class 1):** `0.55`
        - **F1 Score:**  
          - 🟩 **No Diabetes (Class 0):** `0.85`  
          - 🟥 **Diabetes (Class 1):** `0.65`
        """)

        with st.expander("📊 Confusion Matrix and Visuals"):
            st.subheader("Factors affecting the Outcome for Diabetes")
            st.image('Images/subplot_diabetes.png',caption="Factors affecting the Outcome for Diabetes")
            st.subheader("Confusion Matrix")
            st.image("Images\cm_diabetes.png", caption="Confusion Matrix")

        with st.expander("🧠 Observations & Insights"):
          st.markdown("""
        - The model is good at identifying **non-diabetic individuals**.
        - It **misses some diabetic cases** (low recall for Class 1).
        - Suggests a need for better **recall sensitivity** toward diabetic predictions.

        """)

    with tab3:
      st.header("🤰 Maternal Health Prediction")

      with st.expander("🔍 Model Details"):
        
        st.markdown("""
       ### 🧪 **Model Summary**
       - **✅ Model Used:** XGBoost Classifier  
       - **📏Scaler:** StandardScaler  
       - **🧬Encoding:** Label Encoding  
       - **🧠Features Used:**  
         - `Age`
         - `SystolicBP` 
         - `DiastolicBP`
         - `BS (Blood Sugar)`
         - `BodyTemp` 
         - `HeartRate`
        """)

      with st.expander("📊 Model Performance Summary"):
        st.markdown("""
        ### ✅ **Performance Overview**
        - **Accuracy:** `84.2%`
        - **Precision:**  
          - 🟢 **Low Risk:** `0.85`  
          - 🟡 **Mid Risk:** `0.87`  
          - 🔴 **High Risk:** `0.81`
        - **Recall:**  
          - 🟢 **Low Risk:** `0.87`  
          - 🟡 **Mid Risk:** `0.82`  
          - 🔴 **High Risk:** `0.84`
        - **F1 Score:**  
          - 🟢 **Low Risk:** `0.86`  
          - 🟡 **Mid Risk:** `0.85`  
          - 🔴 **High Risk:** `0.83`
        """)
      with st.expander("📊 Confusion Matrix and Visuals"):
            st.subheader("*Systolic BP, Diastolic BP, Blood Sugar* are the factors affecting maternal health the most")
            st.image('Images/subplot_maternal.png',caption="*Systolic BP, Diastolic BP, Blood Sugar* are the factors affecting maternal health the most")
            st.subheader("Confusion Matrix")
            st.image("Images\cm_maternal.png", caption="Confusion Matrix")

      with st.expander("🧠 Observations & Insights"):
        st.markdown("""
        -  The model performs **very well across all risk levels**, especially in **recall**.
        - Low-risk patients are identified very accurately (87% recall).
        - High-risk detection is good, but slight improvement possible in **precision**.
        """)


    with tab4:
        st.header("🫀 Heart Disease Prediction")
        with st.expander("🔍 Model Details"):
          st.markdown("""
        ### 🧪 **Model Summary**
        - **✅ Model Used:** Desicion Tree Classifier  
        - **📏 Scaler:** StandardScaler  
        - **🧬 Encoding:** No Encoding  
        - **🧠 Features Used:**  
          - `Age`
          - `Sex`
          - `CP`
          - `Trestbps`
          - `Cholesterol`
          - `FastingBS`
          - `RestingECG`
          - `Thalach`
          - `ExerciseAngina`
          - `Oldpeak`
          - `ST_Slope`
          - `CA` 
          - `Thal`          
        """)

        with st.expander("📊 Model Performance Summary"):
          st.markdown("""
        ### ✅ **Performance Overview**
        - **Accuracy:** `88.52%`
        - **Precision:**  
          - 💚 **No Heart Disease (0):** `0.87`  
          - ❤️ **Heart Disease (1):** `0.90`
        - **Recall:**  
          - 💚 **No Heart Disease (0):** `0.90`  
          - ❤️ **Heart Disease (1):** `0.88`
        - **F1 Score:**  
          - 💚 **No Heart Disease (0):** `0.88`  
          - ❤️ **Heart Disease (1):** `0.89`
        """)

        with st.expander("📊 Confusion Matrix and Visuals"):
            st.header("*Important Features Impacting Prediction*")
            st.subheader("Features that affects target[1]")
            st.image("Images\subplot_heart.png", caption="Features affecting heart health the most")
            st.subheader("Features that affects target[0]")
            st.image("Images\subplot_heart_negative.png", caption="Features affecting heart health the least")
            st.subheader("Confusion Matrix")
            st.image("Images/cm_heart.png", caption="Confusion Matrix")

        with st.expander("🧠 Observations & Insights"):
          st.markdown("""
        - **High accuracy** (88.52%) tells model is well-trained.
        -  Model performs **very well for detecting non-heart disease cases** (high recall).
        -  **Precision for heart disease is very good**, so when the model predicts it, it's mostly correct.
        """)


#### ---- ####
st.sidebar.markdown("\n\n")
st.sidebar.markdown("---")
st.sidebar.markdown("\n\n")
st.sidebar.markdown("\n\n")
st.sidebar.markdown("\n\n")
st.sidebar.markdown("\n\n")
st.sidebar.markdown("\n\n")
st.sidebar.markdown("\n\n")
st.sidebar.markdown("\n\n")
st.sidebar.markdown("\n\n")

st.sidebar.subheader("Thanks for trusting and visiting HealthWise!❤️")
#### ---- ####




