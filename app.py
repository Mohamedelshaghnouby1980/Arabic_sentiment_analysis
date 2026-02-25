import streamlit as st
import joblib

# 1. تحميل الموديل (تأكد أن الاسم هو نفس اسم الملف اللي نزلته)
model = joblib.load('arabic_sentiment_app.pkl')

# 2. واجهة البرنامج
st.title("محلل المشاعر العربية 🤖")
user_input = st.text_input("اكتب مراجعتك هنا:")

if st.button("تحليل"):
    if user_input:
        prediction = model.predict([user_input])[0]
        result = "إيجابي 😊" if prediction == 1 else "سلبي 😡"
        st.write(f"النتيجة: {result}")
    else:
        st.write("من فضلك اكتب نصاً أولاً!")