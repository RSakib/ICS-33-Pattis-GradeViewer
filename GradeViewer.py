import pandas as pd
from openpyxl import load_workbook
import warnings

# Before running, "pip install pandas" and "pip install openpyxl"

# Get rid of warning at beginning that happens due to Grades excel
#  being strange in the first row
warnings.filterwarnings("ignore")

#Change this if you don't want inputs
enable_input = True


# This should be the name of the grades excel sheet
if enable_input:
    loc = input("Enter file name (it should be in same directory): ")
else:
    #Default value if no input bool
    loc = "ics33spr21grades.xlsm"

# This is the name of the Grading Sheet that should be in the excel file
#  (It is Caps dependent)
if enable_input:
    sheet_name = input("Enter name of excel sheet (Where grades are located): ")
else:
    #Default value if no input bool
    sheet_name = 'Spring 2021'

# This is the unique hashed ID provide by Pattis
if enable_input:
    hashed_id = int(input("Enter Hashed ID: "))
else:
    #Default value if no input bool
    hashed_id = "Ur hashed id here as an int"




# Create the work sheet and Data Frame
ws = pd.read_excel(loc, sheet_name=sheet_name)
df = pd.DataFrame(ws)

# Specify the row and slice the off the junk columns
row = df.loc[df['Hashed ID'] == hashed_id]
row = row.iloc[:,0:30]

# Print without the index at the beginning
print(row.to_string(index=False))

# Postpone the window close
quit = input('Type q to quit')
while quit != 'q'.lower():
    quit = input("Type q to quit")
