from datetime import datetime, timedelta
users = [
    {
        "name": "Ivan",
        "birthday": datetime(1996, 9, 30)
    },
    {
        "name": "Igor",
        "birthday": datetime(1996, 9, 1)
    },
    {
        "name": "Brad",
        "birthday": datetime(1996, 9, 29)
    },
    {
        "name": "Serj",
        "birthday": datetime(1996, 9, 26)
    },
    {
        "name": "Bohdan",
        "birthday": datetime(1996, 9, 17)
    },
    {
        "name": "Andrey",
        "birthday": datetime(2000, 9, 24)
    }
    ,
    {
        "name": "Brad2",
        "birthday": datetime(1996, 9, 26)
    },
    {
        "name": "Serj2",
        "birthday": datetime(1996, 9, 23)
    },
    {
        "name": "Bohdan2",
        "birthday": datetime(1996, 9, 24)
    }
]
date_birthday={
        "Monday":[],
        "Tuesday":[],
        "Wednesday":[],
        "Thursday":[],
        "Friday":[],
    }
def get_birthdays_per_week (users):
    tooday=datetime.today()
    next_week = tooday - timedelta(days=tooday.weekday())-timedelta(days=3)
    print(next_week)
    #end = start + timedelta(days=6)
    #next_week =start
    two_weeks= next_week + timedelta(7)
    print(two_weeks)
    for name in users:
        name['birthday']=name['birthday'].replace(year=tooday.year)
        if next_week <= name['birthday'] <= two_weeks:
            print(name['birthday'])
            if name['birthday'].weekday() in (0,5,6):
                date_birthday["Monday"].append(name["name"])
            elif name['birthday'].weekday() in (1,1):
                date_birthday["Tuesday"].append(name["name"])
            elif name['birthday'].weekday() in (2,2):
                date_birthday["Wednesday"].append(name["name"])
            elif name['birthday'].weekday() in (3,3):
                date_birthday["Thursday"].append(name["name"])
            elif name['birthday'].weekday() in (4,4):
                date_birthday["Friday"].append(name["name"])
    return date_birthday
print(get_birthdays_per_week(users))