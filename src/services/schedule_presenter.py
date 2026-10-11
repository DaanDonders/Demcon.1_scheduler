from models.show import Show
from models.stage import Stage
import json


def format_schedule(shows: list[Show], stages: list[Stage]) -> dict:
    # Group shows by stage_number
    stage_dict = {}
    for stage in stages:
        stage_dict[stage.number] = []

    for show in shows:
        if show.stage_number is not None:
            stage_dict.setdefault(show.stage_number, []).append(show)

    # Build sorted stages list
    sorted_stage_numbers = sorted(stage_dict.keys())
    stages_output = []

    for stage_num in sorted_stage_numbers:
        # Sort shows within each stage by start time
        stage_shows = sorted(stage_dict[stage_num], key=lambda s: s.start_time)
        shows_output = [
            {
                "name": s.name,
                "start_time": s.start_time,
                "end_time": s.end_time,
            }
            for s in stage_shows
        ]
        stages_output.append(
            {
                "stage_number": stage_num,
                "shows": shows_output,
            }
        )

    return {"stages": stages_output}
