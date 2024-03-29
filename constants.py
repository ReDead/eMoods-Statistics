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

# Number of decimal places you want outputed
PRECISION = 2

# -----------------------------------

# DO NOT MODIFY

DATE = 'DATE (YYYY-MM-DD)'
SEVERITY_LEVELS = ['None', 'Mild', 'Moderate', 'Severe']
DESTINATION += '/' if DESTINATION[-1] != '/' else ''