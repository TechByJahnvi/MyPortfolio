from flask import Flask, render_template


app = Flask(__name__)


PORTFOLIO = {
    "name": "Jahnvi Pandey",
    "title": "Machine Learning Engineer",
    "experience_years": "3 years",
    "tagline": "Building scalable ML systems, retrieval pipelines, and production-ready backend workflows.",
    "top_skills": [
        "NLP",
        "Ranking",
        "Retrieval",
        "Flask APIs",
        "Docker",
        "Kubernetes",
    ],
    "tech_stack": [
        "Python",
        "Flask",
        "TensorFlow",
        "PyTorch",
        "scikit-learn",
        "SQL",
        "Docker",
        "Kubernetes",
        "AWS",
        "Azure",
        "Azure Blob Storage",
        "Azure AI Search",
        "Azure Indexer",
        "Vector DB",
        "MQTT",
        "GitLab CI/CD",
    ],
    "current_project": {
        "name": "Compliance QA Pipeline",
        "status": "Active",
        "summary": (
            "A compliance-review pipeline that takes a YouTube ad URL as input, retrieves "
            "relevant guidance from Digital Influencer Guide 101 and Google YouTube ad "
            "policies, checks whether the ad is compliant, and generates a structured report."
        ),
        "focus": [
            "YouTube ad URL ingestion and compliance review flow",
            "Guideline retrieval from Digital Influencer Guide 101 and Google ad policies",
            "Azure Blob Storage, Azure AI Search, Azure Indexer, and vector retrieval",
            "Structured compliance report generation with grounded findings",
        ],
        "link": "#project-compliance-qa",
    },
    "experience": [
        {
            "company": "HCLSoftware",
            "role": "Specialist Software Engineer · Machine Learning",
            "period": "Apr 2024 — Present",
            "summary": (
                "Owned recommendation, ranking, and retrieval systems with a strong focus on "
                "automation, deployment, and measurable production impact."
            ),
            "highlights": [
                "Reduced ticket resolution time by 75% through improved recommendation quality.",
                "Built scalable feature pipelines on production logs with 10% MoM success-rate improvement.",
                "Shipped containerized ML pipelines with Docker, Kubernetes, and CI/CD.",
                "Developed LLM workflows with monitoring, validation, and fallback logic.",
            ],
            "tags": ["Recommendation", "TF-IDF", "BM25", "Automation", "Kubernetes"],
        },
        {
            "company": "DIC Lohia Corp",
            "role": "Graduate Engineer Trainee · Data Science",
            "period": "Aug 2023 — Apr 2024",
            "summary": (
                "Built real-time industrial data systems spanning telemetry ingestion, dashboards, "
                "and modular application architecture."
            ),
            "highlights": [
                "Built a dashboard application for remote machine monitoring.",
                "Designed reporting architecture for structured operational visibility.",
                "Converted high-frequency machine signals into usable application data.",
                "Reduced debugging time through diagnostics and integration tooling.",
            ],
            "tags": ["Flutter", "Flask", "MQTT", "Realtime Systems"],
        },
        {
            "company": "Lohia Corp",
            "role": "Data Science Intern / Software Intern",
            "period": "Jun 2022 — Apr 2023",
            "summary": (
                "Worked on analytics, dashboards, configuration tooling, and operational data processing."
            ),
            "highlights": [
                "Built log analytics pipelines for downtime and efficiency analysis.",
                "Created dashboards to visualize failure patterns and operational metrics.",
                "Developed validation-driven configuration management tooling.",
            ],
            "tags": ["Analytics", "Visualization", "Validation", "Tooling"],
        },
    ],
}


@app.route("/")
def home():
    return render_template("index.html", portfolio=PORTFOLIO)


if __name__ == "__main__":
    app.run(debug=True)
