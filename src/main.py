from services.input_parser import parse_shows
from services.festival_planner import sort_shows
from services.festival_planner import plan_shows


input_data = """show_1 29 33
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

shows = parse_shows(input_data)
sorted_shows = sort_shows(shows)
stages = plan_shows(sorted_shows)


for show in sorted_shows:
    print(show)

for stage in stages:
    print(stage)