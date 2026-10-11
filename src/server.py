import sys
import os
import json
from http.server import HTTPServer, BaseHTTPRequestHandler

# Ensure src directory is in python path when run from root or src
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from services.input_parser import parse_shows
from services.festival_planner import plan_shows
from services.schedule_presenter import format_schedule

SAMPLE_INPUT = """show_1 29 33
show_2 2 9
show_3 44 47
show_4 26 30
show_5 15 20
show_6 8 15
show_7 2 9
show_8 30 34
show_9 1 9
show_10 20 28
show_11 1 4
show_12 2 11
show_13 26 29
show_14 5 10
show_15 37 44
show_16 27 35
show_17 36 39
show_18 4 10
show_19 35 44
show_20 22 30
show_21 15 20
show_22 42 46
show_23 6 9
show_24 19 23
show_25 31 38
show_26 37 41
show_27 30 36
show_28 14 21
show_29 5 13
show_30 33 36"""


class ScheduleAPIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/api/schedule":
            try:
                shows = parse_shows(SAMPLE_INPUT)
                stages = plan_shows(shows)
                schedule_dict = format_schedule(shows, stages)

                response_body = json.dumps(schedule_dict).encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Content-Length", str(len(response_body)))
                self.end_headers()
                self.wfile.write(response_body)
            except Exception as e:
                err_body = json.dumps({"error": str(e)}).encode("utf-8")
                self.send_response(500)
                self.send_header("Content-Type", "application/json; charset=utf-8")
                self.send_header("Content-Length", str(len(err_body)))
                self.end_headers()
                self.wfile.write(err_body)
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        # Suppress or format standard server log output if desired
        super().log_message(format, *args)


def run(server_class=HTTPServer, handler_class=ScheduleAPIHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting schedule API server on http://localhost:{port}...")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print("Server stopped.")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    run(port=port)

