def study_schedule(permanence_period, target_time):
    try:
        students = 0
        for login, logout in permanence_period:
            if login <= target_time <= logout:
                students += 1
        return students
    except TypeError:
        return None
