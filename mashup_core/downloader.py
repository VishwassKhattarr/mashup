import yt_dlp
import os
os.makedirs("temp", exist_ok=True)


def download_videos(singer, n, path="temp"):
    os.makedirs(path, exist_ok=True)

    query = f"ytsearch{n}:{singer} songs"

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": f"{path}/%(title)s.%(ext)s"
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([query])

    return path
