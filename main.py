import os
from flask import Flask, request, render_template, redirect, url_for, flash
from google.cloud import storage

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Path to your service account JSON
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:\DIVISON\eyasusales-23ab199bf100.json"

# Your GCS bucket name
GCS_BUCKET_NAME = "eyasusalesbucket"

# Initialize GCS client
storage_client = storage.Client()
bucket = storage_client.bucket(GCS_BUCKET_NAME)

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if "file" not in request.files:
            flash("No file part in the request.")
            return redirect(url_for("upload_file"))

        file = request.files["file"]

        if file.filename == "":
            flash("No file selected.")
            return redirect(url_for("upload_file"))

        # Upload to GCS
        blob = bucket.blob(file.filename)
        blob.upload_from_file(file)
        flash(f"File '{file.filename}' uploaded successfully to {GCS_BUCKET_NAME}!")

        return redirect(url_for("upload_file"))

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
