from flask import Flask, request, Response
from xmlrpc.server import SimpleXMLRPCDispatcher
import os

app = Flask(__name__)

dispatcher = SimpleXMLRPCDispatcher(allow_none=True, encoding=None)

# ---------- RPC METHODS ----------
def calculate_fare(distance_km, time_minutes, surge):
    base_fare = 50
    per_km = 12
    per_min = 2
    return round((base_fare + distance_km*per_km + time_minutes*per_min) * surge, 2)

def assign_driver(location):
    drivers = ["Ravi", "Karthik", "Suresh", "Arun"]
    return drivers[hash(location) % len(drivers)]

def estimate_eta(distance_km):
    return round((distance_km / 40) * 60, 1)

dispatcher.register_function(calculate_fare)
dispatcher.register_function(assign_driver)
dispatcher.register_function(estimate_eta)

# ---------- HTTP → RPC BRIDGE ----------
@app.route("/RPC2", methods=["POST"])
def rpc_handler():
    response = dispatcher._marshaled_dispatch(request.data)
    return Response(response, content_type="text/xml")

@app.route("/")
def home():
    return "RPC Server is running"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)

