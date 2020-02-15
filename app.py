from StatiCalc.control import StatiCalc

calc = StatiCalc()
calc.start()

while True:
    try:
        calc.run()
    except ZeroDivisionError:
        print("Enter a data only at a time! Previously initiated creation of dataset is discarded. Now create a new "
              "dataset")
        continue
