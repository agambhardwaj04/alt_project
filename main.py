import streamlit as st
import joblib 



#### Sidebar ####
st.sidebar.header("Multi-Disease Predictor")
st.sidebar.markdown("\n\n")
st.sidebar.header("Navigation")
st.sidebar.subheader("Please select the Disease you are concerned about")
st.sidebar.markdown("\n\n")
st.sidebar.markdown("\n\n")
st.sidebar.markdown("\n\n")

#### ---- ####
#### INTRODUCTION ####

page = st.sidebar.selectbox("Sidebar Selectbox", ["Home","Parkinsons", "Diabetes", "Maternal Health","Heart Health","Conclusions"])

if page == "Home":
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
        st.image("resized_image.png", use_container_width =True)
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
        st.image("resized_heart_image_344x289.jpg",use_container_width=True)
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


if page == "Parkinsons":
    
    st.write("Content for Page 1")

elif page == "Diabetes":
    
    st.write("Content for Page 2")

elif page == "Maternal Health":
    model_maternal = joblib.load('C:/Users/agamb/Desktop/Alt_Project/Models/model_boost.joblib')


    st.write("Content for Page 3")

elif page == "Heart Health":
    
    st.write('Content foor Page 4')

elif page == "Conclusions":
    
    st.write('Content foor Page 5')
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

st.sidebar.subheader("Thanks for visiting HealthWise!❤️")