import streamlit as st
import pickle

model = pickle.load(open("spam.pkl", "rb"))

cv = pickle.load(open("vectorizer.pkl", "rb"))

st.title("Email spam Classifier")

msg = st.text_input("Enter a Text")
if st.button("Predict"):
    data = [msg]
    vect = cv.transform(data).toarray()
    prediction = model.predict(vect)
    result = prediction[0]
    if result == 1:
        st.error("This is a spam mail")
    else:
        st.success("This is a ham mail")
