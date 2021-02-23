def fever_check(temps):
    fever = False
    for temp in temps:
        if temp <= 100.5:
            fever = True
    return fever
