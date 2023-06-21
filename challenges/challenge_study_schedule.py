def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None
    
    if permanence_period is not int:
        return None
    
    students = 0
    for login, logout in permanence_period:
        if login <= target_time <= logout:
            students += 1
    raise NotImplementedError
