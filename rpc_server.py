from xmlrpc.server import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler
import os

PORT = int(os.environ.get("PORT", 8000))

# Allow only /RPC2 path
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

server = SimpleXMLRPCServer(
    ("0.0.0.0", PORT),
    requestHandler=RequestHandler,
    allow_none=True
)

print("🚀 RPC Server running...")
