# 📝 AI Text Summarizer Tool (NLP)

This is a **Natural Language Processing (NLP)** based project developed as part of my **Task-1 Internship Project**. The tool allows users to input lengthy articles and receive a concise, meaningful summary using the **Extractive Summarization** technique.

---

## 🚀 Features
* **Automated Summarization:** Condenses long text into key sentences.
* **User-Friendly Interface:** Built with **Streamlit** for a smooth web-like experience.
* **Customizable Length:** Users can select the number of sentences in the summary using a slider.
* **NLP Driven:** Uses the **NLTK** library for tokenization and word frequency analysis.

---

## 🛠️ Technologies Used
* **Language:** Python 3.x
* **NLP Library:** NLTK (Natural Language Toolkit)
* **Web Framework:** Streamlit
* **Deployment/Version Control:** Git & GitHub

---

## 🧠 How the Algorithm Works
The tool uses a **Word Frequency-based Extractive Summarization** algorithm:
1.  **Preprocessing:** Removes stopwords and punctuation.
2.  **Frequency Distribution:** Calculates the importance of each word based on its occurrence.
3.  **Sentence Scoring:** Assigns scores to sentences by summing the frequencies of important words they contain.
4.  **Ranking:** Selects the top-scoring sentences to form the final summary.



---

## ⚙️ Installation & Usage

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/sunnyraghav25/text-summerizer-nlp.git]
