from backend import app
import requests
from flask import Flask, request, jsonify

SECRET_ADMIN_CODE = "SuperSecure2025!"

@app.route("/")
def home():
    return "Welcome to the Arrivo backend!"


@app.route("/retrieve-bus-data", methods=["GET"])
def retrieve_bus_data():


    """
    Endpoint to retrieve bus data.
    This is a placeholder function that should be replaced with actual logic.
    """
    with open("bus_data.json", "r") as f:
        bus_data = f.read()
        
    return bus_data, 200, {"Content-Type": "application/json"}





@app.route('/verify-admin-code', methods=['POST'])
def verify_admin_code():
    data = request.get_json()
    if data.get("code") == SECRET_ADMIN_CODE:
        return jsonify({"valid": True})
    else:
        return jsonify({"valid": False}), 403
