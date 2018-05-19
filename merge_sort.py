def merge_sort(LIST):
    start = []
    end = []
    a = LIST[0]
    b = LIST[-1]
    while (LIST.index(a) == LIST.index(b) and len(LIST) <=2):
        a = min(LIST)
        b = max(LIST)
        start.append(a)
        end.append(b)
        LIST.remove(a)
        LIST.remove(b)
    end.reverse()
    return start + end
