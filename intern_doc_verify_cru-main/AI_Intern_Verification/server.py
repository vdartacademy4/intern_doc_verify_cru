from flask import Flask, render_template, jsonify
from flask_cors import CORS
import pandas as pd
import os

from app import run_pipeline
from email_fetcher import fetch_emails
from flask import send_from_directory

app = Flask(__name__)
print("Template Folder:", app.template_folder)
print("Static Folder:", app.static_folder)
print("Current Working Directory:", os.getcwd())
CORS(app)


# ------------------------------------
# HOME PAGE
# ------------------------------------
@app.route("/")
def home():
    return render_template("index.html")


# ------------------------------------
# PROCESS EMAILS
# ------------------------------------
@app.route("/process", methods=["GET"])
def process():

    print("\n========== PROCESS STARTED ==========")

    try:

        candidates = fetch_emails()

        print("Candidates Found:", len(candidates))
        print(candidates)

        if len(candidates) > 0:
            run_pipeline(candidates)

        print("========== PROCESS COMPLETED ==========")

        return jsonify({
            "success": True,
            "message": "Processing Completed"
        })

    except Exception as e:

        print("ERROR:", e)

        return jsonify({
            "success": False,
            "message": str(e)
        })# ------------------------------------
# LOAD CANDIDATE TABLE
# ------------------------------------
@app.route("/candidates")
def candidates():

    from datetime import datetime

    today = datetime.now().strftime("%Y-%m-%d")

    csv_path = os.path.join(
        "output",
        f"report_{today}.csv"
    )

    if not os.path.exists(csv_path):
        return jsonify([])

    df = pd.read_csv(csv_path)
    df = df.sort_index(ascending=False)
    df = df.fillna("")

    return jsonify(df.to_dict(orient="records"))


@app.route("/file/<folder>/<filename>")
def open_file(folder, filename):

    folder_path = os.path.join("processed", folder)

    if not os.path.exists(folder_path):
        folder_path = os.path.join("uploads", folder)

    return send_from_directory(folder_path, filename)


# ------------------------------------
# DASHBOARD STATS
# ------------------------------------
from datetime import datetime

# ------------------------------------
# DASHBOARD STATS
# ------------------------------------
@app.route("/stats")
def stats():

    today = datetime.now().strftime("%Y-%m-%d")

    csv_path = os.path.join(
        "output",
        f"report_{today}.csv"
    )

    if not os.path.exists(csv_path):
        return jsonify({
            "total": 0,
            "verified": 0,
            "manual": 0,
            "mismatch": 0
        })

    df = pd.read_csv(csv_path)
    df = df.fillna("")

    total = len(df)

    verified = len(df[df["Final_Status"] == "VERIFIED"])
    manual = len(df[df["Final_Status"] == "MANUAL REVIEW"])
    mismatch = len(df[df["Final_Status"] == "MISMATCH"])

    return jsonify({
        "total": total,
        "verified": verified,
        "manual": manual,
        "mismatch": mismatch
    })
if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )