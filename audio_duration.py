import wave

def get_audio_duration(audio_path):
    with wave.open(audio_path, 'r') as audio:
        frames = audio.getnframes()
        rate = audio.getframerate()
        duration = frames / float(rate)
        return round(duration, 2)

if __name__ == "__main__":
    path = "sample_audio/sample.wav"
    duration = get_audio_duration(path)
    print(f"🕒 Audio Duration: {duration} seconds")

