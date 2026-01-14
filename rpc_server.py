from xmlrpc.server import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler

# 👇 VERY IMPORTANT: allow /RPC2
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

server = SimpleXMLRPCServer(
    ("0.0.0.0", 8000),
    requestHandler=RequestHandler,
    allow_none=True
)

print("🚀 RPC Server running on port 8000...")

def calculate_fare(distance_km, time_minutes, surge):
    base_fare = 50
    per_km = 12
    per_min = 2
    return round((base_fare + distance_km * per_km + time_minutes * per_min) * surge, 2)

def assign_driver(location):
    drivers = ["Ravi", "Karthik", "Suresh", "Arun"]
    return drivers[hash(location) % len(drivers)]

def estimate_eta(distance_km):
    return round((distance_km / 40) * 60, 1)

server.register_function(calculate_fare)
server.register_function(assign_driver)
server.register_function(estimate_eta)

server.serve_forever()
