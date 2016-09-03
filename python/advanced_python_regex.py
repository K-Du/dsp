import urllib2
import pandas as pd
from collections import Counter

faculty_url = urllib2.urlopen('https://raw.githubusercontent.com/K-Du/dsp/master/python/faculty.csv')
faculty_csv = pd.read_csv(faculty_url, skipinitialspace = True)

degrees = list(faculty_csv.degree)

# Remove periods from list of degrees
degrees = map(lambda x: x.replace('.', ''), degrees)

# Separate degrees for people who have multiple degrees
degrees = [x.split() for x in degrees]

# Flatten the list
degrees = sum(degrees, [])

# Count total number of different degrees and number of each degree
print len(Counter(degrees))
print Counter(degrees)

# Count total number of different job titles and number of each title
print len(Counter(faculty_csv.title))
print Counter(faculty_csv.title)

# List the email addresses
print list(faculty_csv.email)

# List and count the unique email address domains
print len(set(x.split('@')[1] for x in list(faculty_csv.email)))
print set(x.split('@')[1] for x in list(faculty_csv.email))
