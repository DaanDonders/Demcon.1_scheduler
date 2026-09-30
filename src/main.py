from services.input_parser import parse_shows


input_data = """show_1 36 39
show_2 30 33
show_3 29 36"""

shows = parse_shows(input_data)

for show in shows:
    print(show)