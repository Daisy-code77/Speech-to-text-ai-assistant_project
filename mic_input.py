import speech_recognition as sr

def mic_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Speak something...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print("📝 Transcribed Text:", text)
        except sr.UnknownValueError:
            print("❌ Could not understand audio.")
        except sr.RequestError as e:
            print(f"⚠️ API error: {e}")

if __name__ == "__main__":
    mic_to_text()

