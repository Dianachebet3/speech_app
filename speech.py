import speech_recognition as sr
import streamlit as st
import warnings

# Ignore warnings related to speech recognition
warnings.filterwarnings('ignore')


# Function to transcribe speech from the microphone
def transcribe_speech():
    recognizer = sr.Recognizer()
    recognizer.energy_threshold = 300  # Adjust the threshold for ambient noise

    with sr.Microphone() as source:
        st.info("Please wait. Calibrating microphone...")  # Inform user of calibration
        recognizer.adjust_for_ambient_noise(source)
        st.info("Say something!")
        audio = recognizer.listen(source)

    st.info("Transcribing...")

    try:
        # Use Google Speech Recognition to transcribe the audio to text
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Sorry, I did not get that."
    except sr.RequestError:
        return "Sorry, the service is unavailable. Please try again later."


# Main function to display the Streamlit UI
import streamlit as st
import speech_recognition as sr

def recognize_audio_file(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
    return recognizer.recognize_google(audio)

def main():
    st.title("Speech Recognition App")
    st.write("Upload an audio file to transcribe")

    uploaded_file = st.file_uploader("Choose an audio file", type=["wav", "mp3"])

    if uploaded_file is not None:
        st.info("Transcribing...")
        try:
            text = recognize_audio_file(uploaded_file)
            st.success("Transcription successful!")
            st.write("Transcribed Text:")
            st.write(text)
        except Exception as e:
            st.error(f"Error: {e}")

if __name__ == "__main__":
    main()



