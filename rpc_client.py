import xmlrpc.client

server = xmlrpc.client.ServerProxy(
    "https://isomorphic-porky-bernetta.ngrok-free.dev/RPC2",
    allow_none=True
)

print("📡 Connected to RPC Server")

print("Fare:", server.calculate_fare(10, 20, 1.5))
print("Driver:", server.assign_driver("Perungudi"))
print("ETA:", server.estimate_eta(10))
