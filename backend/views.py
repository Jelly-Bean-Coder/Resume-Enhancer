from flask import Blueprint, render_template, request, jsonify
from markupsafe import escape
import resumeScanner

views_bp = Blueprint("views", __name__)

@views_bp.route("/")
def home():
    return render_template("in.html")

@views_bp.route("/analyze", methods=["POST"])
def analyzeData():
    if request.method == "POST":
        resume = request.files["resume"]
        jobDesc = request.form.get("jobDesc")

        return render_template("out.html", text=resumeScanner.prompt(resume.read(), jobDesc))
        