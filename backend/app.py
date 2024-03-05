from flask import Flask, jsonify, request
from bsm_model import calculate_bsm_value
from polygon_client import client

app = Flask(__name__)


@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.json
    ticker = data.get("ticker")
    # Additional parameters for BSM
    result = calculate_bsm_value(ticker)  # Simplified
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)
