from models.show import Show


def parse_shows(input_data: str) -> list[Show]:
    shows = []

    for line in input_data.strip().splitlines():
        name, start, end = line.split()

        shows.append(
            Show(
                name=name,
                start_time=int(start),
                end_time=int(end)
            )
        )

    return shows