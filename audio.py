
import sounddevice as sd
import wave
import numpy as np
import tempfile
import whisper

def record_audio(duration, sample_rate=16000):
    print(f"Recording for {duration} seconds...")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype="float32")
    sd.wait()
    print("Recording complete.")

    # Save the recording to a temporary WAV file
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as temp_file:
        wav_file_path = temp_file.name
        with wave.open(wav_file_path, "wb") as wav_file:
            wav_file.setnchannels(1)
            wav_file.setsampwidth(2)
            wav_file.setframerate(sample_rate)
            wav_file.writeframes((audio * 32767).astype(np.int16).tobytes())

    return wav_file_path

def transcribe_audio(file_path, model_name="base"):
    print(f"Loading Whisper model: {model_name}...")
    model = whisper.load_model(model_name)
    print("Model loaded. Transcribing audio...")
    result = model.transcribe(file_path)
    return result["text"]
