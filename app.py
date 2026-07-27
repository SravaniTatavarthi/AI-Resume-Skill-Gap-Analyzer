from flask import Flask, render_template, request
import os

from resume_parser import extract_resume_text
from job_parser import extract_job_description
from skill_matcher import compare_skills

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    resume = request.files["resume"]
    job = request.files["job"]

    resume_path = os.path.join(app.config["UPLOAD_FOLDER"], resume.filename)
    job_path = os.path.join(app.config["UPLOAD_FOLDER"], job.filename)

    resume.save(resume_path)
    job.save(job_path)

    resume_text = extract_resume_text(resume_path)
    job_text = extract_job_description(job_path)

    matched, missing, score = compare_skills(resume_text, job_text)

    return render_template(
        "result.html",
        matched=matched,
        missing=missing,
        score=score,
    )


if __name__ == "__main__":
    app.run(debug=True)