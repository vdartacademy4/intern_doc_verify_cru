from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)

@app.route("/candidates")
def candidates():

    try:
        df = pd.read_csv("output/report.csv")

        return jsonify(
            df.fillna("").to_dict(orient="records")
        )

    except Exception as e:

        return jsonify({
            "error": str(e)
        })

if __name__ == "__main__":
    app.run(debug=True)