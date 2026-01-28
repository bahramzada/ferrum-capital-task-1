import re
import joblib
import gradio as gr

# -------------------------
# Text preprocessing
# -------------------------
def handle_negation(text):
    text = text.replace("didn't ", "did_not_")
    text = text.replace("don't ", "do_not_")
    text = text.replace("can't ", "can_not_")
    text = text.replace("won't ", "will_not_")
    text = text.replace("isn't ", "is_not_")
    text = text.replace("aren't ", "are_not_")
    text = text.replace("wasn't ", "was_not_")
    text = text.replace("weren't ", "were_not_")
    text = text.replace("not ", "not_")
    return text

def clean_text(text):
    text = text.lower()
    text = handle_negation(text)
    text = re.sub(r"\d+", "", text)
    text = re.sub(r"[^\w\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

# -------------------------
# Load model and vectorizer
# -------------------------
model = joblib.load("models/linear_svm_model.pkl")
tfidf = joblib.load("models/tfidf_vectorizer.pkl")

# Label mapping
label_map = {
    0: "anger",
    1: "joy",
    2: "love",
    3: "sadness",
    4: "fear",
    5: "surprise"
}

# -------------------------
# Prediction function
# -------------------------
def predict_emotion(text):
    cleaned_text = clean_text(text)
    vector = tfidf.transform([cleaned_text])
    prediction = model.predict(vector)[0]
    return label_map[prediction]

# -------------------------
# Gradio Interface
# -------------------------
interface = gr.Interface(
    fn=predict_emotion,
    inputs=gr.Textbox(
        lines=3,
        placeholder="Enter a sentence to analyze emotion..."
    ),
    outputs=gr.Label(label="Predicted Emotion"),
    title="Emotion Classification Demo",
    description=(
        "This demo uses a Linear SVM model trained on an emotion dataset "
        "to predict one of six emotions: anger, fear, joy, love, sadness, surprise."
    ),
    examples=[
        ["I am extremely happy today"],
        ["I feel scared and anxious"],
        ["I miss her so much"],
        ["This makes me so angry"],
        ["I didn't feel humiliated"]
    ]
)

if __name__ == "__main__":
    interface.launch()
