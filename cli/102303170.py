import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from mashup_core.downloader import download_videos
from mashup_core.audio_processor import convert_and_trim
from mashup_core.merger import merge_audios



def main():
    if len(sys.argv) != 5:
        print("Usage: python program.py <Singer> <NumVideos> <Duration> <OutputFile>")
        return

    singer = sys.argv[1]
    n = int(sys.argv[2])
    duration = int(sys.argv[3])
    output = sys.argv[4]

    if n <= 10:
        print("Number of videos must be > 10")
        return

    if duration <= 20:
        print("Duration must be > 20 seconds")
        return

    try:
        print("Downloading videos...")
        path = download_videos(singer, n)

        print("Processing audio...")
        trimmed = convert_and_trim(path, duration)

        print("Merging...")
        merge_audios(trimmed, output)

        print("Mashup created:", output)

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
