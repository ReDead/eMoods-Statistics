# constants.py

# This class contains constants that the program uses to run.
# Some of them you can change to alter the way things are displayed or other configs.
# Other constants are integral to the program working and should not be changed.

# -----------------------------------

# Configs
# Feel free to change these

# Days between each date tick mark on graphs. Must be a positive integer value.
DATE_INTERVAL = 7

# The directory in which you want the output sent to.
# It can be a relative path in the same directory as the program or an exact path
# NOTE: This directory must ALREADY exist before running the program
# Ex: 'out', 'out/', '', '/', 'C://Users/User1/Documents'
DESTINATION = 'out'

# Used for statistics calculating.
# Number of days where another symptom is not considered a new episode.
DAY_THRESHOLD = 2

# Number of days to add on to either end of graphs for spacing
PADDING = 3

# Number of decimal places you want outputed in the stats file
PRECISION = 2

# -----------------------------------

# HTML

# You should not need to change this. However, if you would like to style your html outputs differently, feel free to alter it.
HTML_HEAD = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        h1 {{
            text-align: center;
        }}
        body {{
            display: flex;
            justify-content: center;
        }}
        .container {{
            display: flex;
            flex-direction: column;
            width: 50%;
        }}
        table {{
            border-collapse: collapse;
        }}
        th, td {{
            border: 1px solid #dddddd;
            text-align: left;
            padding: 8px;
        }}
        th {{
            background-color: #f2f2f2;
        }}
    </style>
</head>
'''

# -----------------------------------

# DO NOT MODIFY

DATE = 'DATE (YYYY-MM-DD)'
SEVERITY_LEVELS = ['None', 'Mild', 'Moderate', 'Severe']
DESTINATION += '/' if DESTINATION[-1] != '/' else ''