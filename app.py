import streamlit as st
import pdfplumber

st.set_page_config(page_title="PDF Özetleyici", page_icon="📄")

st.title("📄 PDF Özetleyici")

uploaded_file = st.file_uploader("PDF yükle", type=["pdf"])

# PDF okuma
def extract_text(pdf_file):
    text = ""

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            # daha agresif text çıkarma
            page_text = page.extract_text(x_tolerance=2, y_tolerance=2)
            
            if page_text:
                text += page_text + "\n"

    return text

# Basit özetleme
def summarize(text):
    sentences = text.split(".")
    sentences = [s.strip() for s in sentences if len(s.strip()) > 30]

    if len(sentences) == 0:
        return "Özet üretilemedi ❌ (PDF boş olabilir)"

    return ". ".join(sentences[:5]) + "."

# UI
if uploaded_file:
    st.info("PDF okunuyor...")

    text = extract_text(uploaded_file)

    st.subheader("📄 Çıkarılan Metin")
    st.write(text[:2000])

    st.write("---")

    if st.button("🧠 Özetle"):
        summary = summarize(text)
        st.subheader("🧠 Özet")
        st.success(summary)