# Import necessary packages
import nltk # Natural Language Toolkit for text processing
import streamlit as st # Streamlit for creating the web app
import speech_recognition as sr # SpeechRecognition for speech-to-text
import random
import string

# Download NLTK data if needed
nltk.download('punkt') # Download punkt sentence tokenizer
nltk.download('wordnet') # Download WordNet lemmatizer data


# Preprocessing Functions
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

# Function to preprocess text input: lowercasing, removing punctuation, tokenization, and lemmatization
def preprocess_text(text):
    text = text.lower() # Convert text to lowercase
    text = ''.join([char for char in text if char not in string.punctuation]) # Remove punctuation
    tokens = nltk.word_tokenize(text) # Tokenize the text into words
    tokens = [lemmatizer.lemmatize(token) for token in tokens] # Lemmatize words to their base form
    return tokens # Return the preprocessed tokens

# Load and preprocess the chatbot dataset
# Note: This is a simple dictionary for demo purposes; a larger dataset would improve the chatbot's responses
responses = {
    "hi": "Hello! How can I help you today?",
    "how are you": "I'm good, thank you! How about you?",
    "what is your name": "I am your friendly chatbot!",
    "bye": "Goodbye! Have a great day!"
}

# Function to generate chatbot response
def chatbot_response(user_input):
    user_input = user_input.lower() # Convert user input to lowercase
    for key in responses.keys(): # Iterate through the keys in the responses dictionary
        if key in user_input: # If the key is found in the user input
            return responses[key] # Return the corresponding response
    return "I'm sorry, I didn't understand that." # Default response if no key is found

# Function to recognize speech from microphone
def recognize_speech_from_mic():
    recognizer = sr.Recognizer() # Create a speech recognizer object
    mic = sr.Microphone() # Create a microphone object

    with mic as source:
        st.info("Listening...") # Display a message while listening
        recognizer.adjust_for_ambient_noise(source) # Adjust for ambient noise
        audio = recognizer.listen(source) # Listen for speech from the microphone

    try:
        st.success("Processing your speech...") # Display a message while processing
        text = recognizer.recognize_google(audio) # Recognize speech using Google Speech Recognition API
        return text # Return the recognized text
    except sr.UnknownValueError:
        return "Sorry, I could not understand your speech." # Handle unknown value error
    except sr.RequestError:
        return "Could not request results; check your internet connection." # Handle request error

# Streamlit App
st.title("Voice-Enabled Chatbot") # Set the title of the app

input_mode = st.radio("Choose input mode:", ("Text", "Speech")) # Create a radio button to choose input mode

# Handle text input
if input_mode == "Text":
    user_input = st.text_input("Enter your message:") # Create a text input field
    if st.button("Send"): # Create a button to send the message
        if user_input: # If user input is not empty
            response = chatbot_response(user_input) # Generate chatbot response
            st.text_area("Chatbot:", value=response, height=150) # Display chatbot response

# Handle speech input
elif input_mode == "Speech":
    if st.button("Start Listening"): # Create a button to start listening
        user_input = recognize_speech_from_mic() # Recognize speech from microphone
        st.write(f"You said: {user_input}") # Display the recognized speech
        response = chatbot_response(user_input) # Generate chatbot response
        st.text_area("Chatbot:", value=response, height=150) # Display chatbot response