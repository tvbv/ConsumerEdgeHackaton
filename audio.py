
import sounddevice as sd
import wave
import numpy as np
import tempfile
import whisper
from pydub import AudioSegment
from pydub.playback import play
from elevenlabs_tty import text_to_speech_file


def say(what_to_say: str):
    file = text_to_speech_file(what_to_say)
    audio = AudioSegment.from_file(file, format="mp3")
    play(audio)

def say_with_music(what_to_say: str, music_file: str):
    file = text_to_speech_file(what_to_say)
    combined = combine_audio(file, music_file)
    play(combined)

def play_with_music(audio_file: str, music_file: str):
    combined = combine_audio(audio_file, music_file)
    play(combined)

def play_sound(sound_file: str):
    audio = AudioSegment.from_file(sound_file, format="mp3")
    audio = audio - 12  # Lower the volume by 10 dB
    audio = audio * 2  # Loop the audio
    play(audio)

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

def combine_audio(speech_sound, background_sound):
    # Load your audio files
    speech = AudioSegment.from_file(speech_sound)  # Replace with your Eleven Labs audio file
    background = AudioSegment.from_file(background_sound)  # Replace with your background music file

    # Adjust volumes if necessary
    speech = speech + 5  # Increase volume of speech
    background = background - 7  # Lower volume of background music

    # Adjust the background music to match the length of the speech
    if len(background) > len(speech):
        # Trim the background music
        background = background[:len(speech)]
    else:
        # Loop the background music
        loops_needed = len(speech) // len(background) + 1
        background = (background * loops_needed)[:len(speech)]

    # Overlay the audio files
    combined = background.overlay(speech)
    return combined;
