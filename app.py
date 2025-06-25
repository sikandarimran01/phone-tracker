from flask import Flask, request, jsonify

app = Flask(__name__)
latest_location = {}

@app.route('/location', methods=['POST'])
def receive_location():
    global latest_location
    latest_location = request.json
    return {"status": "received"}

@app.route('/track')
def track():
    lat = latest_location.get("latitude", 0)
    lon = latest_location.get("longitude", 0)
    return {
        "latitude": lat,
        "longitude": lon,
        "map": f"https://maps.google.com/?q={lat},{lon}"
    }
