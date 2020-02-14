import math


def mean(data_set):
    sum = 0
    for i in range(len(data_set)):
        sum += float(data_set[i])
    print(f"Mean = {sum / len(data_set)}")


def median(data_set):
    data_set = data_set.sort()
    print(f"Median = {float(data_set[len(data_set) // 2])}")


def mode(data_set):
    dict, max = {}, 0
    for data in data_set:
        if data in dict.keys():
            dict[data] += 1
        else:
            dict[data] = 1
    for data in data_set:
        if dict[data] > max:
            max = dict[data]
            max_key = data
    print(f"Mode = {max_key}")


def deviation(data_set):
    sum, result = 0, {}
    average = mean(data_set)
    for data in data_set:
        sum += (data - average) ** 2
    result['var'] = sum / len(data_set)
    result['std'] = math.sqrt(result['var'])
    result['cv'] = (result['std'] / average) * 100
    print(f"Variance = {result['var']}")
    print(f"Standard Deviation = {result['std']}")
    print(f"Coefficient of Variation = {result['cv']}")


class Data:
    def __init__(self, *data, **kdata):
        self.data = data
        self.kdata = kdata

    def collect_data(self):
        data_set = []
        while True:
            data = input("Enter a data : ")
            if data.isdigit():
                data_set.append(float(data))
            else:
                break
        self.data = data_set

    def calculate_all(self):
        print("-----------------------------------")
        mean(self.data)
        mode(self.data)
        deviation(self.data)