from models.show import Show
from models.stage import Stage
import heapq


def sort_shows(shows: list[Show]) -> list[Show]:
    return sorted(shows, key=lambda show: show.start_time)

def plan_shows(shows: list[Show]) -> list[Stage]:
    sorted_shows = sort_shows(shows)
    stages = []
    stage_number = 0

    for show in sorted_shows:
        if stages and show.start_time >= stages[0][0]:
            _, _, stage = heapq.heappop(stages)

            show.stage_number = stage.number
            stage.available_from = show.end_time + 1
            heapq.heappush(stages, (stage.available_from, stage.number, stage))
        else:
            stage_number += 1

            new_stage = Stage(
                number=stage_number,
                available_from=show.end_time + 1
            )

            show.stage_number = new_stage.number
            heapq.heappush(stages, (new_stage.available_from, new_stage.number, new_stage))

    return [stage for _, _, stage in stages]