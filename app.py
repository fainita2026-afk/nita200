import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="University Admission Predictor",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 University Admission Predictor")
st.write("Predict the estimated chance of university admission.")

st.header("Student Information")

cgpa = st.slider(
    "CGPA",
    min_value=0.0,
    max_value=10.0,
    value=8.0,
    step=0.1
)

gre = st.slider(
    "GRE Score",
    min_value=260,
    max_value=340,
    value=320,
    step=1
)

toefl = st.slider(
    "TOEFL Score",
    min_value=0,
    max_value=120,
    value=100,
    step=1
)

university_rating = st.number_input(
    "University Rating",
    min_value=1,
    max_value=5,
    value=3,
    step=1
)

research = st.selectbox(
    "Research Experience",
    options=["No", "Yes"]
)

research_value = 1 if research == "Yes" else 0

prediction = (
    0.05
    + (cgpa / 10) * 0.40
    + ((gre - 260) / 80) * 0.18
    + (toefl / 120) * 0.14
    + (university_rating / 5) * 0.08
    + research_value * 0.15
)

prediction = min(max(prediction, 0), 1)

st.subheader("Predicted Chance of Admission")

st.metric(
    "Chance of Admit",
    f"{prediction * 100:.2f}%"
)

st.header("Input Metrics")

labels = [
    "CGPA",
    "GRE",
    "TOEFL",
    "University Rating",
    "Research"
]

values = [
    cgpa / 10,
    (gre - 260) / 80,
    toefl / 120,
    university_rating / 5,
    research_value
]

fig, ax = plt.subplots()
ax.bar(labels, values)
ax.set_ylim(0, 1)
ax.set_ylabel("Normalized Score")
ax.set_title("Student Input Profile")
plt.xticks(rotation=20)

st.pyplot(fig)

st.success("Prediction generated successfully.")