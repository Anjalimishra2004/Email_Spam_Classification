import streamlit as st
import pickle

model = pickle.load(open("spam.pkl", "rb"))
cv = pickle.load(open("vectorizer.pkl", "rb"))

def main():
	st.title("Email Spam Classification")
	st.subheader("Build with streamlit & Python")
	msg = st.text_input("Enter a Text: ")

main()
