import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Common technical skills
SKILLS = {
    "python",
    "java",
    "c",
    "c++",
    "html",
    "css",
    "javascript",
    "react",
    "nodejs",
    "node.js",
    "flask",
    "django",
    "sql",
    "mysql",
    "mongodb",
    "git",
    "github",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "data science",
    "tensorflow",
    "keras",
    "pandas",
    "numpy",
    "opencv",
    "power bi",
    "excel",
    "aws",
    "azure",
    "docker",
    "linux"
}


def extract_skills(text):
    text = text.lower()
    found_skills = set()

    for skill in SKILLS:
        if skill in text:
            found_skills.add(skill)

    return found_skills


def compare_skills(resume_text, job_text):
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_text)

    matched = sorted(list(resume_skills & job_skills))
    missing = sorted(list(job_skills - resume_skills))

    if len(job_skills) == 0:
        score = 0
    else:
        score = round((len(matched) / len(job_skills)) * 100, 2)

    return matched, missing, score