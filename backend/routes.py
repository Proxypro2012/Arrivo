from backend import app

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
