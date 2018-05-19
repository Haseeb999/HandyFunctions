def selection_sort(LIST):
    start = []
    while len(LIST) != 0:
        a = min(LIST)
        start.append(a)
        LIST.remove(a)
    return start
