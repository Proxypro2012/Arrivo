from backend import app

@app.route("/")
def home():
    return "Welcome to the Arrivo backend!"
