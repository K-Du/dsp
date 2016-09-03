# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import urllib2
import pandas as pd

football_url = urllib2.urlopen('https://raw.githubusercontent.com/K-Du/dsp/master/python/football.csv')
football_csv = pd.read_csv(football_url)

# Find difference between Goals and Goals Allowed
football_csv['Goals - Goals Allowed'] = abs(football_csv['Goals'] - football_csv['Goals Allowed'])

# Sort the dataframe by "Goals - Goals Allowed" 
football_csv.sort_values(by = 'Goals - Goals Allowed', inplace = True)

# Get the team name with smallest difference
print football_csv.head(1)['Team'].iloc[0]

# Answer is Aston Villa with a difference of 1 goal
