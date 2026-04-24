import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import heapq
import sys

# 1. Setup and Error Handling for NLTK
def setup_nltk():
    try:
        nltk.download('punkt', quiet=True)
        nltk.download('stopwords', quiet=True)
        nltk.download('punkt_tab', quiet=True)
    except Exception as e:
        print(f"Error downloading NLTK data: {e}")

def summarize_text(text, summary_size=3):
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text.lower())
    
    # Calculate Word Frequencies
    word_frequencies = {}
    for word in words:
        if word.isalnum() and word not in stop_words:
            word_frequencies[word] = word_frequencies.get(word, 0) + 1

    if not word_frequencies:
        return "Not enough meaningful words to summarize."
        
    max_freq = max(word_frequencies.values())
    for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word] / max_freq)

    # Score Sentences
    sentences = sent_tokenize(text)
    sentence_scores = {}
    for sent in sentences:
        for word in word_tokenize(sent.lower()):
            if word in word_frequencies:
                if len(sent.split(' ')) < 40: 
                    sentence_scores[sent] = sentence_scores.get(sent, 0) + word_frequencies[word]

    # Handle cases where text is too short
    actual_size = min(len(sentences), summary_size)
    summary_sentences = heapq.nlargest(actual_size, sentence_scores, key=sentence_scores.get)
    
    return ' '.join(summary_sentences)

# --- Deliverable UI ---
if __name__ == "__main__":
    setup_nltk()
    
    print("="*50)
    print("      NLP TEXT SUMMARIZATION TOOL")
    print("="*50)
    
    print("\nPaste your article/text below (Press Enter then Ctrl+D or Ctrl+Z to finish):")
    # Using sys.stdin.read() allows multi-line pasting easily
    try:
        user_input = sys.stdin.read()
    except EOFError:
        pass

    if user_input.strip():
        print("\n" + "-"*20)
        print("GENERATING SUMMARY...")
        print("-"*20)
        
        # You can ask the user how many sentences they want
        result = summarize_text(user_input, summary_size=3)
        
        print("\nRESULT:")
        print(result)
    else:
        print("No text provided. Exiting.")