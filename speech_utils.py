# speech_utils.py
import speech_recognition as sr

def transcribe_speech():
    """
    Captures audio from the microphone and converts it to text.
    Returns a tuple: (transcribed_text, error_message)
    """
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        # Adjust for ambient noise to improve accuracy
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            # Listen to the user's input with a timeout of 10 seconds
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=30)
            text = recognizer.recognize_google(audio)
            return text, None
        except sr.WaitTimeoutError:
            return None, "Listening timed out. No speech detected."
        except sr.UnknownValueError:
            return None, "Sorry, I couldn't understand the audio. Please try speaking clearly or type your answer."
        except sr.RequestError as e:
            return None, f"Could not request results from Speech Recognition service; {e}"
        except Exception as e:
            return None, f"An error occurred: {str(e)}"