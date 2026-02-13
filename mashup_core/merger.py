from pydub import AudioSegment

def merge_audios(files, output_name):
    final_audio = AudioSegment.empty()

    for file in files:
        audio = AudioSegment.from_mp3(file)
        final_audio += audio

    final_audio.export(output_name, format="mp3")
