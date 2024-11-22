from TTS.api import TTS
tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=True)

# generate speech by cloning a voice using default settings
tts.tts_to_file(text="Once upon a time in the snowy North Pole, Santa Claus and his elves were busy preparing for Christmas Eve. The workshop buzzed with activity—elf engineers polished toy trains, craftspersons stitched teddy bears, and bakers packed cookies for Santa's snack breaks.",
                file_path="output.wav",
                speaker_wav="santasVoice.wav",
                language="en")