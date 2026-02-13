from flask import Flask, render_template, request
import threading
import sys, os, shutil

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from mashup_core.downloader import download_videos
from mashup_core.audio_processor import convert_and_trim
from mashup_core.merger import merge_audios
from utils import zip_file, send_email

app = Flask(__name__)


# background job
def process_mashup(singer, n, duration, email):
    try:
        print("Starting background job...")

        path = download_videos(singer, n)
        trimmed = convert_and_trim(path, duration)

        output = "final.mp3"
        merge_audios(trimmed, output)

        zipname = zip_file(output)
        send_email(email, zipname)

        # cleanup
        if os.path.exists("temp"):
            shutil.rmtree("temp")

        if os.path.exists("final.mp3"):
            os.remove("final.mp3")

        if os.path.exists(zipname):
            os.remove(zipname)

        print("Job completed")

    except Exception as e:
        print("Background job error:", e)


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":
        singer = request.form["singer"]
        n = int(request.form["videos"])
        duration = int(request.form["duration"])
        email = request.form["email"]

        # run in background thread
        thread = threading.Thread(
            target=process_mashup,
            args=(singer, n, duration, email)
        )
        thread.start()

        return """
        ✅ Mashup generation started!<br>
        You will receive email when ready.<br>
        (You can close this page)
        """

    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
