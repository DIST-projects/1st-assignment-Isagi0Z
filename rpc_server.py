from xmlrpc.server import SimpleXMLRPCServer
import os

PORT = int(os.environ.get("PORT", 8000))

server = SimpleXMLRPCServer(("0.0.0.0", PORT), allow_none=True)
print("🚀 RPC Server running...")

def calculate_fare(distance_km, time_minutes, surge):
    if distance_km <= 0 or time_minutes <= 0:
        return "Error: Invalid distance or time"

    base_fare = 50
    per_km = 12
    per_min = 2

    fare = (base_fare + (distance_km * per_km) + (time_minutes * per_min)) * surge
    return round(fare, 2)

def assign_driver(pickup_location):
    drivers = ["Ravi", "Karthik", "Suresh", "Arun"]
    return drivers[hash(pickup_location) % len(drivers)]

def estimate_eta(distance_km):
    avg_speed = 40
    eta = (distance_km / avg_speed) * 60
    return round(eta, 1)

def trip_summary(distance, time, surge, location):
    return {
        "fare": calculate_fare(distance, time, surge),
        "driver": assign_driver(location),
        "eta": estimate_eta(distance)
    }

server.register_function(calculate_fare)
server.register_function(assign_driver)
server.register_function(estimate_eta)
server.register_function(trip_summary)

server.serve_forever()
