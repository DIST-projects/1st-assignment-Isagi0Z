"""
RPC CLIENT
----------
Connects to cloud-hosted Course Performance Service
"""

import xmlrpc.client

server = xmlrpc.client.ServerProxy("http://EC2_PUBLIC_IP:8000")

print(server.register_score("CSE201", "Kow", 78))
print("Course Record:", server.get_record("CSE201"))
print("Performance:", server.performance_status("CSE201"))

print(server.register_score("CSE202", "Gow", 92))
print("Course Record:", server.get_record("CSE202"))
print("Performance:", server.performance_status("CSE202"))
