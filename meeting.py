# appoint_str = "APPOINT 1(day) 12:30 30(duration) 2(two person) andrey alex"
appoint_str = ["APPOINT 1 12:30 30 2 andrey alex",
               "APPOINT 1 12:01 30 2 alex sergey",
               "APPOINT 1 12:59 60 2 alex andrey",
               "PRINT 1 alex",
               "PRINT 1 andrey", "PRINT 1 sergey",
               "PRINT 2 alex"]
# PRINT day name

meetings = []
dict_print = {}
for i in appoint_str:
    # print(i)
    input_str = i.split()
    if input_str[0] == "APPOINT":
        day = int(input_str[1])
        hour = int(input_str[2].split(":")[0])
        minute = int(input_str[2].split(":")[1])
        duration = int(input_str[3])

        start_time = (day * 24 * 60) + (hour * 60 + minute)
        end_time = start_time + duration
        names = input_str[5:]
        if len(meetings) != 0:
            for line in meetings:
                if (start_time < line[0]) and (end_time <= line[0]) \
                        or (start_time >= line[1]) and (end_time > line[1]):
                    meetings.append([start_time, end_time, names, day, hour, minute, duration])
                    print("OK")
                    break
                else:
                    print("FAIL")
                    print(names)
                    break

        else:
            meetings.append([start_time, end_time, names, day, hour, minute, duration])
            print("ОК")

    elif input_str[0] == "PRINT":
        for meet in meetings:
            day_ = meet[3]
            if int(input_str[1]) == day_:
                for person in meet[2]:
                    if input_str[2] == person:
                        if meet[5] == 0:
                            min_ = "00"
                        else:
                            min_ = str(meet[5])
                        print(str(meet[4]) + ":" + min_ + " " + str(meet[6]) + " " + str(meet[2]))

