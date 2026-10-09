import sys
import os

# Add src directory to python path so tests can find models and services packages when run from root
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
from models.show import Show
from services.input_parser import parse_shows


class TestInputParser(unittest.TestCase):
    def test_parse_shows_standard(self):
        input_data = (
            "show_1 10 15\n"
            "show_2 2 5\n"
            "show_3 20 25"
        )
        shows = parse_shows(input_data)
        self.assertEqual(len(shows), 3)
        self.assertEqual(shows[0].name, "show_1")
        self.assertEqual(shows[0].start_time, 10)
        self.assertEqual(shows[0].end_time, 15)
        self.assertEqual(shows[1].name, "show_2")
        self.assertEqual(shows[1].start_time, 2)
        self.assertEqual(shows[1].end_time, 5)
        self.assertEqual(shows[2].name, "show_3")
        self.assertEqual(shows[2].start_time, 20)
        self.assertEqual(shows[2].end_time, 25)

    def test_parse_shows_whitespace(self):
        input_data = "  show_A   1  5  \n  show_B  6  10  "
        shows = parse_shows(input_data)
        self.assertEqual(len(shows), 2)
        self.assertEqual(shows[0].name, "show_A")
        self.assertEqual(shows[0].start_time, 1)
        self.assertEqual(shows[0].end_time, 5)
        self.assertEqual(shows[1].name, "show_B")
        self.assertEqual(shows[1].start_time, 6)
        self.assertEqual(shows[1].end_time, 10)

    def test_parse_shows_empty(self):
        shows = parse_shows("")
        self.assertEqual(shows, [])


if __name__ == "__main__":
    unittest.main()

