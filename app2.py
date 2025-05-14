import requests
from flask import Flask, request, jsonify, render_template
from transformers import pipeline, XLMRobertaTokenizer, XLMRobertaForSequenceClassification

app =Flask (_name_)

tokenizer = XLMRobertaTokenizer.from_pretrained('cardiffnlp/twitter-xlm-rroberta-base-sentiment')
model=XLMRobertaForSequenceClassification.from_pretrained('cardiffnlp/twitter-xlm-roberta-base-sentiment')
sentiment_analyzer=pipeline('sentiment-analysis', model=model,tokenizer=tokenizer)
emotion_classifier=pipeline("text-classification",model="j-hartmann/emotion-english-distilroberta-base")

def get wikipedia_summary(query):
    url=f"https://en.wikipedia.org/api/rest_v1/page/summary/(query)"
    response requests.get(url)

    if response.status_code = 200:
        data=response.json()
        return data.get('extract','No information found')
    else:
        return 'no information found'

#Function to detect cultural context in text
def detect_cultural_context(text):
    detected_context = []
    cultural_references = ["Holi", "Thanksgiving", "Bollywood", "Diwali", "Carnival", "Oktoberfest"]

#Check if any cultural reference is found in the text
    for reference in cultural_references:
        if reference.lower() in text.lower():

#Fetch the context from Wikipedia for the detected reference
            context_info get_wikipedia_summary(reference)
            detected_context.append({"term": reference, "meaning": context_info))
    return detected_context

#Function to analyze sentiment
def analyze_sentiment(text):
    result = sentiment_analyzer(text)
    return result

# Function to analyze emotion
def analyze_emotion(text):
    result = emotion_classifier(text)
    return result

#Home route
 @app.route('/')
def home():
    return render_template("index.html")

#Analyze route
@app.route('/analyze', methods=['POST'])
def analyze():
try:
    data = request.json
    text = data.get("text", "")

    if not text:

        return jsonify({"error": "No text provided"}), 400

# Analyze sentiment, emotion, and cultural context
    sentiment = analyze_sentiment(text)
    emotion = analyze_emotion(text)
    cultural_context = detect_cultural_context(text)

# Prepare response with dynamic response based on emotion
    response = {
        "sentiment": sentiment,
        "emotion": emotion,
        "cultural_context": cultural_context
    }

    if emotion[0]['label'].lower() in ["anger", "sadness"]:

        response["dynamic_response"] = f"I'm sorry to hear that you're feeling (emotion[0]['label'].lower()}. Is there anythi

    elif emotion[0]['label'].lower() == "joy":

        response["dynamic_response"] = f"I'm so glad to hear that you're feeling (emotion[0]['label'].lower())! Keep it up!"

    else:

        response["dynamic_response"] = "Thank you for sharing your thoughts."

    return jsonify(response)

except Exception as e:
    return jsonify({"error": str(e)}), 500

# Run the Flask app
if_name_ == "_main_":
    app.run(debug=True)


