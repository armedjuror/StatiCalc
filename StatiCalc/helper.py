def helper():
    print("""
            ---Operational Commands---
            1. help                 - To get a command list
            2. developer            - To get details about developer
            3. quit (or) q          - Quit StatiCalc

            ---Manipulating Commands---
            1. create dataset       - Create a data set
            2. select dataset       - Select a data set
            3. drop dataset         - Delete a data set
            4. change dataset       - Change to another data set
            5. exit dataset         - Exit from current dataset
            6. modify dataset       - Modify current dataset
            7. show dataset         - Show current dataset
            
            ---Modification Commands---
            1. add                  - Add a new data to dataset
            2. change               - Modify an existing data in the dataset
            3. delete               - Delete a data from dataset
            4. exit modify          - Complete modification and close modification environment

            ---Functional Commands (Will work only after selecting a data set)---
            1. mean                 - Mean of current data set
            2. median               - Median
            3. mode                 - Mode
            4. variance             - Variance
            5. sd                   - Standard deviation
            6. cv                   - Coefficient of variance
            7. sample_sd            - Sample Standard Deviation
            8. sample_var           - Sample Variance
            9. all                  - Calculate all above functions
            """)