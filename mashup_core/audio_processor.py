from pydub import AudioSegment
import os

def convert_and_trim(path, duration):
    trimmed_files = []

    for file in os.listdir(path):
        if file.endswith(".webm") or file.endswith(".m4a") or file.endswith(".mp4"):
            full_path = os.path.join(path, file)

            audio = AudioSegment.from_file(full_path)
            trimmed = audio[:duration * 1000]

            new_file = full_path + ".mp3"
            trimmed.export(new_file, format="mp3")

            trimmed_files.append(new_file)

    return trimmed_files
