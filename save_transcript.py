from utils.audio_utils import transcribe_audio
from utils.file_utils import save_text

if __name__ == "__main__":
    path = "sample_audio/sample.wav"
    text = transcribe_audio(path)
    if "❌" not in text:
        save_text(text, "transcripts/transcript.txt")
        print("✅ Transcription saved in transcripts/transcript.txt")
    else:
        print(text)

