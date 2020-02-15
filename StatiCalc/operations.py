import math


def mean(data_set):
    sum = 0
    for i in range(len(data_set)):
        sum += float(data_set[i])
    ave = sum / len(data_set)
    return ave


def median(data_set):
    data_set.sort()
    length = len(data_set)
    med_class = (length // 2)-1
    if length % 2 == 0:
        med = (data_set[med_class] + data_set[med_class+1]) / 2
    else:
        med = float(data_set[med_class])
    return med


def mode(data_set):
    global max_key
    count, max_count = {}, 0
    for data in data_set:
        if data in count.keys():
            count[data] += 1
        else:
            count[data] = 1
    for data in data_set:
        if count[data] > max_count:
            max_count = count[data]
            max_key = data
    return max_key


def deviation(data_set):
    sum, result = 0, {}
    average = mean(data_set)
    for data in data_set:
        sum += (data - average) ** 2
    result['var'] = sum / len(data_set)
    result['std'] = math.sqrt(result['var'])
    result['cv'] = (result['std'] / average) * 100
    return result
