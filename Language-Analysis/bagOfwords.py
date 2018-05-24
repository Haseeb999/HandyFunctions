def bagOfwords(data):
    '''
    Counts the repitition of words in data.
    '''
    counter = {}
    for line in data:
        for word in line.lower().split(' '):
            if word in counter:
                counter[word] += 1
            if word not in counter:
                counter[word] = 1
    return counter
