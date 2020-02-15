# StatiCalc
A Simple Statistical Calculator. A command based simple stastical calculator. User can create any number of datasets and calculate and store its statistical parameters seperately. Simple commands are the guides through the app.

## How do I calculate?
#### Operational Commands
1. `help`                  - To get a command list
2. `developer`             - To get details about developer
3. `quit` (or) `q`        - Quit StatiCalc

#### Manipulating Commands
1. `create dataset`       - Create a data set
2. `select dataset`       - Select a data set
3. `drop dataset`         - Delete a data set
4. `change dataset`       - Change to another data set
5. `exit dataset`         - Exit from current dataset
6. `modify dataset`       - Modify current dataset
7. `show dataset`         - Show current dataset
            
#### Modification Commands
1. `add`                  - Add a new data to dataset
2. `change`               - Modify an existing data in the dataset
3. `delete`               - Delete a data from dataset
4. `exit modify`          - Complete modification and close modification environment
            
#### Functional Commands
1. `mean`                 - Mean of current data set
2. `median`               - Median
3. `mode`                 - Mode
4. `variance`             - Variance
5. `sd`                   - Standard deviation
6. `cv`                   - Coefficient of variance
7. `all`                  - Calculate all above functions

## How to contribute?
#### Adding functions
To add a function `myfunc`, 
* Create a function to calculate the new function `myfunc()` in `StatiCalc/operations.py`
* Define a property, `myfunc_value`, for `Data` class of `StatiCalc/data.py`
* Create a method, `myfunc()`, in `Data` class of `StatiCalc/data.py` to update the property using `myfunc` defined in `StatiCalc/operations.py` by importing it to `StatiCalc/data.py`
* Create a command in `terminal` method of `StatiCalc` class in `StatiCalc/control.py` to access and print the `myfunc_value` of `data_set` under the first `else`. 
* Update `StatiCalc/helper.py` with the command added in the `StatiCalc/control.py`
* Create a new instance of `Developer` class in `StatiCalc/developer.py` and fill with your contact details.

#### Anyother debugging
All other contributions are appreciated as an issue or a pull request of this repo 
