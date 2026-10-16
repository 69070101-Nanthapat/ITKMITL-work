"""AIRPORT"""
start_input = input()
exit_input = input()

start_parts = start_input.split('.')
start_hr = int(start_parts[0])
start_min = int(start_parts[1])

exit_parts = exit_input.split('.')
exit_hr = int(exit_parts[0])
exit_min = int(exit_parts[1])


if not (0 <= start_hr <= 23 and 0 <= start_min <= 59\
        and 0 <= exit_hr <= 23 and 0 <= exit_min <= 59):
    print("ERROR")
else:
    start_total_mins = start_hr * 60 + start_min
    exit_total_mins = exit_hr * 60 + exit_min
    duration_mins = exit_total_mins - start_total_mins

    if duration_mins < 0 or duration_mins > 1440:
        print("ERROR")
    elif duration_mins <= 15:
        print("FREE")
    else:
        parked_hours = duration_mins // 60
        if duration_mins % 60 > 0:
            parked_hours += 1

        if parked_hours == 1:
            print(25)
        elif parked_hours == 2:
            print(50)
        elif parked_hours == 3:
            print(80)
        elif parked_hours == 4:
            print(110)
        elif parked_hours == 5:
            print(145)
        elif parked_hours == 6:
            print(180)
        elif 7 <= parked_hours <= 24:
            print(250)
        else:
            print("ERROR")
