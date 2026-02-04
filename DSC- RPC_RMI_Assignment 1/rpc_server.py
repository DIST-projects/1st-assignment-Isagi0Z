"""
RPC SERVER
----------
Remote Course Performance Service
Hosted on Cloud VM (EC2)
"""

from xmlrpc.server import SimpleXMLRPCServer

class CourseService:

    def __init__(self):
        self.records = {}

    def register_score(self, course_id, student_name, score):
        self.records[course_id] = {
            "student": student_name,
            "score": score
        }
        return "Course score registered successfully"

    def get_record(self, course_id):
        if course_id not in self.records:
            return "Record not found"
        return self.records[course_id]

    def performance_status(self, course_id):
        if course_id not in self.records:
            return "Record not found"

        score = self.records[course_id]["score"]

        if score >= 85:
            return "Excellent"
        elif score >= 65:
            return "Satisfactory"
        elif score >= 50:
            return "Needs Improvement"
        else:
            return "Fail"


server = SimpleXMLRPCServer(("0.0.0.0", 8000), allow_none=True)
server.register_instance(CourseService())

print("RPC Course Performance Service running on port 8000...")
server.serve_forever()
