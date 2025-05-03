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
def main():
    st.title("Speech Recognition App")
    st.write("Click on the button below to start speaking:")

    # Add a button to trigger speech recognition
    if st.button("Start Recording"):
        # Call transcribe_speech to get the transcribed text
        transcription = transcribe_speech()
        st.write("Transcription: ", transcription)


if __name__ == "__main__":
    main()
