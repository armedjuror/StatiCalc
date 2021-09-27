from StatiCalc.operations import mean, median, mode, deviation, sample_deviation
from termcolor import colored
from StatiCalc.helper import helper

data_dict = {}


class Data:
    def __init__(self, name):
        self.name = name
        self.data = []
        self.mean_value = 0
        self.median_value = 0
        self.mode_value = 0
        self.variance = 0
        self.cv = 0
        self.std = 0
        self.sample_var = 0
        self.sample_sd = 0

    def collect_data(self):
        data_set = self.data
        print(colored("Data will be read until the first non-numeric character", 'red'))
        while True:
            data = input("Enter a data : ")
            try:
                float(data)
                data_set.append(float(data))
            except:
                break
            # if data.isdigit():
            #     data_set.append(float(data))
            # else:
            #     break
        self.data = data_set

    def modify(self):
        print(f"Current dataset : {self.data}")
        print("You could change, add or delete a data \n What you want to do?")
        while True:
            command = input(f"(modify - {self.name})>>>")
            if command == 'change':
                flag, i = 0, 0
                change = float(input("Which data you want to change (Will change first matching data) : "))
                for i in range(len(self.data)):
                    if change == self.data[i]:
                        flag = 1
                        break
                if flag:
                    changed = float(input("New value : "))
                    self.data[i] = changed
                    print(f"Dataset updated successfully! \n New dataset : {self.data}")
                else:
                    print('Data not found')
            elif command == 'delete':
                flag, i = 0, 0
                delete = float(input("Which data you want to delete : "))
                for i in range(len(self.data)):
                    if delete == self.data[i]:
                        flag = 1
                        break
                if flag:
                    self.data.remove(delete)
                    print(f"Data {delete} is deleted successfully \n New dataset : {self.data}")
            elif command == 'add':
                add = float(input("Enter the new data : "))
                self.data.append(add)
                print(f"Data {add} is added successfully \n New dataset : {self.data}")
            elif command == 'help':
                helper()
            elif command == 'exit modify':
                self.all()
                return
            else:
                print("""Command not recognised! Even if this was a valid command, it might not work under modification 
                      environment. Please 'exit modify' and try. or command 'help' for command list. Only 
                      modification commands will work under modification environment""")

    def mean(self):
        self.mean_value = mean(self.data)

    def median(self):
        self.median_value = median(self.data)

    def mode(self):
        self.mode_value = mode(self.data)

    def deviation(self):
        deviations = deviation(self.data)
        self.variance = deviations['var']
        self.std = deviations['std']
        self.cv = deviations['cv']

    def sample_deviation(self):
        sample_deviations = sample_deviation(self.data)
        self.sample_sd = sample_deviations['sample_sd']
        self.sample_var = sample_deviations['sample_var']

    def all(self):
        self.mean()
        self.median()
        self.mode()
        self.deviation()
        self.sample_deviation()


def data_init():
    name = input("Enter the name of current data set : ")
    if name in data_dict:
        print(colored("Sorry, name already selected. Choose a different name", 'yellow'))
        return 0
    data_set = Data(name)
    print("Enter the data to the dataset : ")
    data_set.collect_data()
    data_set.all()
    data_dict[name] = data_set
    return 1


def list_data():
    if len(data_dict.keys()) == 0:
        print("Sorry, No data sets available, Please create one")
        return
    print("AVAILABLE DATA SETS ARE FOLLOWING, SELECT ANYONE: ")
    for dat in data_dict.keys():
        print(f"- {dat}")


def data_select():
    list_data()
    if len(data_dict.keys()) == 0:
        return
    while True:
        name = input(">>>").lower()
        if name not in data_dict:
            print("Sorry, that data set not found! Please select anyone from the list")
        else:
            return data_dict[name]


def data_delete():
    list_data()
    name = input(">>>")
    if name not in data_dict:
        print("Sorry, that data set not found! Please select anyone from the list")
        return 0
    else:
        del data_dict[name]
        print(f"Data set of name {name} deleted successfully.")
        return 1