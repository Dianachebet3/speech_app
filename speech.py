import speech_recognition as sr
print(sr.__version__)
recognizer = sr.Recognizer()
recognizer.energy_threshold = 300
import warnings
warnings.filterwarnings('ignore')
import speech_recognition as sr
import streamlit as st

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
    st.info("Transcribing...")

    try:
        # using google speech recognition
        print("Text: "+recognizer.recognize_google(audio))
    except:
         print("Sorry, I did not get that")


         def main():
             st.title("Speech Recognition App")
             st.write("Click on the microphone to start speaking:")

             # add a button to trigger speech recognition
             if st.button("Start Recording"):
                 text = transcribe_speech()
                 st.write("Transcription: ", text)


         if __name__ == "__main__":
             main()