from collections import defaultdict

#Calculate the best qualifiers of all time.
def convertQualiTime(qualiTime):
    if qualiTime == "\N":
        return None
    min, sec = qualiTime.split(":")
    return int(min) * 60 + float(sec)

def driverStats(data):
    stats = defaultdict(lambda: {
        'sessions': 0,
        'q1_count': 0,
        'q2_count': 0,
        'q3_count': 0,
        'q1_exits': 0,
        'pole_positions': 0,
        'total_position': 0,
        'position_list': [],
        'q1_times': [],
        'q2 times': [],
        'q3_times': [],
    })

    for row in data:
        _, _, driverId, _, _, position, q1, q2, q3 = row
        driverId = int(driverId)
        position = int(position) if position != "\N" else None

        stats[driverId]['sessions'] += 1
        if position == 1: stats[driverId]['pole_positions'] += 1
        if position:
            stats[driverId]['total_position'] += position
            stats[driverId]['position_list'].append(position)

        q1time = convertQualiTime(q1)
        q2time = convertQualiTime(q2)
        q3time = convertQualiTime(q3)

        

