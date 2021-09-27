from termcolor import colored
from StatiCalc import data
from StatiCalc.developer import Developer
from StatiCalc.starter import printer
from StatiCalc.helper import helper

dev = Developer()


class StatiCalc:
    def __init__(self):
        self.user = ''

    def start(self):
        for i in range(25):
            print(colored("* ", 'red'), end='')
            print(colored(". ", 'red'), end='')
        print("\n")
        printer()
        print(colored("Welcome to StatiCalc", 'green'))

    def run(self):
        while True:
            command = input(">>>").lower()
            if command == 'quit' or command == 'q':
                print("Hope you had a great time! See you again. Bye!")
                exit()
            elif command == 'create dataset':
                while True:
                    status = data.data_init()
                    if status:
                        break
            elif command == 'select dataset':
                data_class = data.data_select()
                if data_class:
                    self.terminal(data_class.name)
            elif command == 'drop dataset':
                data.data_delete()
            elif command == 'exit dataset':
                print("No dataset is currently selected!")
            elif command == 'help':
                helper()
            elif command == 'developer':
                self.developer()
            elif command == 'mean' or command == 'median' or command == 'mode' or command == 'variance' or command == 'sd' or command == 'sd' or command == 'cv' or command == 'all' or command == 'modify dataset' or command == 'show dataset':
                print(colored("Please select a dataset", 'yellow'))
            else:
                print("Sorry, Invalid Command")

    def terminal(self, name):
        while True:
            command = input(f"({name})>>>")
            if command == 'quit' or command == 'q':
                print("Hope you had a great time! See you again. Bye!")
                exit()
            elif command == 'change dataset':
                while True:
                    data_class = data.data_select()
                    if not data_class:
                        continue
                    else:
                        self.terminal(data_class.name)
            else:
                data_set = data.data_dict[name]
                if command == 'mean':
                    print(f"Mean = {data_set.mean_value}")
                elif command == 'median':
                    print(f"Median = {data_set.median_value}")
                elif command == 'mode':
                    print(colored("Mode calculation may have errors", 'red'))
                    print(f"Mode = {data_set.mode_value}")
                elif command == 'variance':
                    print(f"Variance = {data_set.variance}")
                elif command == 'sd':
                    print(f"Standard Deviation = {data_set.std}")
                elif command == 'cv':
                    print(f"Coefficient of Variation = {data_set.cv}")
                elif command == 'sample_var':
                    print(f"Sample Variance = {data_set.sample_var}")
                elif command == 'sample_sd':
                    print(f"Sample Standard Deviation = {data_set.sample_sd}")
                elif command == 'all':
                    print(f"Mean = {data_set.mean_value}")
                    print(f"Median = {data_set.median_value}")
                    print(f"Mode = {data_set.mode_value}")
                    print(f"Variance = {data_set.variance}")
                    print(f"Standard Deviations = {data_set.std}")
                    print(f"Coefficient of Variation = {data_set.cv}")
                    print(f"Sample Standard Deviation = {data_set.sample_sd}")
                    print(f"Sample Variance = {data_set.sample_var}")
                elif command == 'show dataset':
                    print(data_set.data)
                elif command == 'modify dataset':
                    data_set.modify()
                elif command == 'help':
                    helper()
                elif command == 'drop dataset':
                    status = data.data_delete()
                    if status:
                        return
                elif command == 'exit dataset':
                    return
                else:
                    print("Sorry, Invalid Command")

    def developer(self):
        print(f"""---CONTACT DEVELOPER---
                Name : {dev.name}
                Email : {dev.email}
                Website : {dev.web}
                Company : {dev.company}
                """)

