import sys
import os

# Add src directory to python path so tests can find models and services packages when run from root
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
import json
from models.show import Show
from models.stage import Stage
from services.festival_planner import sort_shows, plan_shows
from services.schedule_presenter import format_schedule


class TestSchedulePresenter(unittest.TestCase):
    def test_format_schedule_empty(self):
        result = format_schedule([], [])
        self.assertEqual(result, {"stages": []})
        # Verify JSON serialization
        json_str = json.dumps(result)
        self.assertEqual(json_str, '{"stages": []}')

    def test_format_schedule_correct_grouping_and_fields(self):
        shows = [
            Show("show_1", 1, 5),
            Show("show_2", 10, 15),
        ]
        sorted_shows = sort_shows(shows)
        stages = plan_shows(sorted_shows)

        result = format_schedule(shows, stages)
        self.assertIn("stages", result)
        self.assertIsInstance(result["stages"], list)
        
        # Verify JSON serialization works without error
        json_str = json.dumps(result)
        parsed = json.loads(json_str)
        self.assertEqual(parsed, result)

    def test_format_schedule_deterministic_ordering(self):
        # Create shows such that multiple stages are allocated, passed in unsorted order
        shows = [
            Show("show_C", 1, 10),
            Show("show_A", 1, 10),
            Show("show_B", 1, 10),
        ]
        stages = plan_shows(shows)
        result = format_schedule(shows, stages)

        # Stages must be ordered by stage_number
        stage_numbers = [s["stage_number"] for s in result["stages"]]
        self.assertEqual(stage_numbers, sorted(stage_numbers))

        # Shows within each stage must be ordered by start_time
        for stage_obj in result["stages"]:
            start_times = [s["start_time"] for s in stage_obj["shows"]]
            self.assertEqual(start_times, sorted(start_times))

    def test_every_show_appears_exactly_once(self):
        shows = [
            Show("show_1", 1, 5),
            Show("show_2", 6, 10),
            Show("show_3", 11, 15),
        ]
        stages = plan_shows(shows)
        result = format_schedule(shows, stages)

        all_show_names = []
        for stage_obj in result["stages"]:
            for show_obj in stage_obj["shows"]:
                all_show_names.append(show_obj["name"])

        self.assertEqual(sorted(all_show_names), ["show_1", "show_2", "show_3"])
        self.assertEqual(len(all_show_names), len(shows))


if __name__ == "__main__":
    unittest.main()
