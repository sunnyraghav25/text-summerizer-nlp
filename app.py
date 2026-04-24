import streamlit as st
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import heapq

# NLTK Data Setup
@st.cache_resource
def load_nltk():
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('punkt_tab')

load_nltk()

def summarize_text(text, num_sentences):
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text.lower())
    
    word_frequencies = {}
    for word in words:
        if word.isalnum() and word not in stop_words:
            word_frequencies[word] = word_frequencies.get(word, 0) + 1

    if not word_frequencies:
        return "Not enough meaningful words to summarize."
        
    max_freq = max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word] / max_freq)

    sentences = sent_tokenize(text)
    sentence_scores = {}
    for sent in sentences:
        for word in word_tokenize(sent.lower()):
            if word in word_frequencies:
                sentence_scores[sent] = sentence_scores.get(sent, 0) + word_frequencies[word]

    actual_size = min(len(sentences), num_sentences)
    summary_sentences = heapq.nlargest(actual_size, sentence_scores, key=sentence_scores.get)
    return ' '.join(summary_sentences)

# --- STREAMLIT UI ---
st.set_page_config(page_title="NLP Summarizer", page_icon="📝")

st.title("📝 AI Text Summarizer Tool")
st.markdown("##### Final Year Internship Project - Task 1")

text_input = st.text_area("Paste your lengthy article here:", height=250)
num_sent = st.slider("Select number of sentences for summary:", 1, 10, 3)

if st.button("Generate Summary"):
    if text_input.strip():
        with st.spinner('Analyzing text...'):
            result = summarize_text(text_input, num_sent)
            st.success("Summary Generated!")
            st.subheader("Result:")
            st.write(result)
    else:
        st.warning("Please paste some text first!")