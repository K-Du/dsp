import urllib2
import pandas as pd

faculty_url = urllib2.urlopen('https://raw.githubusercontent.com/K-Du/dsp/master/python/faculty.csv')
faculty_csv = pd.read_csv(faculty_url, skipinitialspace = True)

faculty_csv.email.to_csv('emails.csv', index = False)
