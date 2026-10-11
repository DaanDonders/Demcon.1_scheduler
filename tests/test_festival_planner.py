import sys
import os

# Add src directory to python path so tests can find models and services packages when run from root
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
from models.show import Show
from models.stage import Stage
from services.festival_planner import sort_shows, plan_shows


class TestFestivalPlanner(unittest.TestCase):
    def test_sort_shows(self):
        shows = [
            Show("C", 20, 25),
            Show("A", 1, 5),
            Show("B", 10, 15),
        ]
        sorted_shows = sort_shows(shows)
        self.assertEqual([s.name for s in sorted_shows], ["A", "B", "C"])
        self.assertEqual([s.start_time for s in sorted_shows], [1, 10, 20])

    def test_plan_shows_empty(self):
        stages = plan_shows([])
        self.assertEqual(stages, [])

    def test_plan_shows_single(self):
        shows = [Show("solo", 5, 10)]
        sorted_shows = sort_shows(shows)
        stages = plan_shows(sorted_shows)
        
        self.assertEqual(len(stages), 1)
        self.assertEqual(shows[0].stage_number, stages[0].number)

    def test_plan_shows_stage_reuse_boundary(self):
        # Inclusive time boundary test: Show 1 ends at 10.
        # Show 2 starts at 11 (previous_end < next_start), so it can reuse the stage.
        # Show 3 starts at 10 (previous_end >= next_start), so it conflicts and requires a new stage.
        shows = [
            Show("show_1", 1, 10),
            Show("show_2", 11, 15),
            Show("show_3", 10, 12),
        ]
        sorted_shows = sort_shows(shows)
        stages = plan_shows(sorted_shows)

        # show_1 and show_2 can share a stage, but show_3 overlaps with show_1 (ends at 10, starts at 10).
        # Therefore, exactly 2 stages should be required.
        self.assertEqual(len(stages), 2)
        
        # Verify every show has a stage assigned
        for show in shows:
            self.assertIsNotNone(show.stage_number)

        # Verify no overlapping shows on the same stage
        stage_assignments = {}
        for show in shows:
            stage_assignments.setdefault(show.stage_number, []).append(show)

        for stage_num, assigned_shows in stage_assignments.items():
            # Sort assigned shows by start time
            assigned_shows.sort(key=lambda s: s.start_time)
            for i in range(len(assigned_shows) - 1):
                current_show = assigned_shows[i]
                next_show = assigned_shows[i + 1]
                # A stage's previous show must end strictly before the next show starts
                self.assertLess(current_show.end_time, next_show.start_time)

    def test_plan_shows_multiple_stages(self):
        # 3 fully overlapping shows at the same time must require 3 separate stages.
        shows = [
            Show("a", 1, 10),
            Show("b", 1, 10),
            Show("c", 1, 10),
        ]
        sorted_shows = sort_shows(shows)
        stages = plan_shows(sorted_shows)
        self.assertEqual(len(stages), 3)
        stage_numbers = {show.stage_number for show in shows}
        self.assertEqual(len(stage_numbers), 3)


    def test_plan_shows_unsorted_non_overlapping(self):
        # Regression test: non-overlapping shows in reverse chronological order
        shows = [
            Show("B", 10, 20),
            Show("A", 1, 5),
        ]
        stages = plan_shows(shows)
        self.assertEqual(len(stages), 1)
        self.assertEqual(shows[0].stage_number, stages[0].number)
        self.assertEqual(shows[1].stage_number, stages[0].number)

    def test_plan_shows_overlapping_assigned_different_stages(self):
        # Overlapping shows must be assigned to different stages
        shows = [
            Show("show_1", 1, 10),
            Show("show_2", 5, 15),
        ]
        stages = plan_shows(shows)
        self.assertEqual(len(stages), 2)
        self.assertNotEqual(shows[0].stage_number, shows[1].stage_number)


if __name__ == "__main__":
    unittest.main()

