import urllib2
import pandas as pd
from collections import OrderedDict

faculty_url = urllib2.urlopen('https://raw.githubusercontent.com/K-Du/dsp/master/python/faculty.csv')
faculty_csv = pd.read_csv(faculty_url, skipinitialspace = True)


faculty_dict = {}
for i in faculty_csv.index:
    # key is the last name
    key = faculty_csv.name[i].split()[-1]
    faculty_dict.setdefault(key, [])
    faculty_dict[key].append([faculty_csv.degree[i],\
    ' '.join(faculty_csv.title[i].split()[:-2]), faculty_csv.email[i]])

    
professor_dict = {}
for i in faculty_csv.index:
    # key is a tuple of first name and last name
    key = (faculty_csv.name[i].split()[0], faculty_csv.name[i].split()[-1])
    professor_dict.setdefault(key, [])
    professor_dict[key].append([faculty_csv.name[i], faculty_csv.degree[i], \
    ' '.join(faculty_csv.title[i].split()[:-2]), faculty_csv.email[i]])
  
ordered_prof = OrderedDict()
for i in faculty_csv.index:
    # key is a tuple of first name and last name
    key = (faculty_csv.name[i].split()[0], faculty_csv.name[i].split()[-1])
    ordered_prof.setdefault(key, [])
    ordered_prof[key].append([faculty_csv.name[i], faculty_csv.degree[i], \
    ' '.join(faculty_csv.title[i].split()[:-2]), faculty_csv.email[i]])
    
# In this case the raw list was already sorted, but if not, use the following
ordered_prof = OrderedDict(sorted(ordered_prof.iteritems(), key = lambda x: x[0][1][0]))

    
