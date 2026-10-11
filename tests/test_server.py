import sys
import os
import json
import unittest
from http.server import HTTPServer
from threading import Thread
import urllib.request

# Add src to python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from server import ScheduleAPIHandler


class TestScheduleAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = HTTPServer(('127.0.0.1', 0), ScheduleAPIHandler)
        cls.port = cls.server.server_port
        cls.server_thread = Thread(target=cls.server.serve_forever, daemon=True)
        cls.server_thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.server_thread.join()

    def test_api_schedule_success(self):
        url = f"http://127.0.0.1:{self.port}/api/schedule"
        with urllib.request.urlopen(url) as response:
            self.assertEqual(response.status, 200)
            self.assertEqual(response.headers.get_content_type(), "application/json")
            data = json.loads(response.read().decode("utf-8"))
            self.assertIn("stages", data)
            self.assertIsInstance(data["stages"], list)
            self.assertGreater(len(data["stages"]), 0)

    def test_api_not_found(self):
        url = f"http://127.0.0.1:{self.port}/api/unknown"
        with self.assertRaises(urllib.error.HTTPError) as ctx:
            urllib.request.urlopen(url)
        self.assertEqual(ctx.exception.code, 404)


if __name__ == "__main__":
    unittest.main()
