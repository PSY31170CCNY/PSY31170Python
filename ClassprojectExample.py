# classproject.py
# this is an analysis of the NYC restaurant inspection data
# found in this file:
# DOHMH_New_York_City_Restaurant_Inspection_Results.csv
# downloaded from https://data.cityofnewyork.us/Health/DOHMH-New-York-City-Restaurant-Inspection-Results/43nn-pn8j
# on 1/18/2019
# we can use the csv module to read in the file
# the csv module docs show this example of to how to do this:
##>>> import csv
##>>> with open('eggs.csv', newline='') as csvfile:
##...     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
##...     for row in spamreader:
##...         print(', '.join(row))
import csv # get the module

# The data dictionary can be found in the spreadsheet file at this link:
# https://data.cityofnewyork.us/api/views/43nn-pn8j/files/ec33d2c8-81f5-499a-a238-0213a38239cd?download=true&filename=RestaurantInspectionDataDictionary_09242018.xlsx
# also downloaded 1/18/2019
# the data fields are named in the first column, so these will be the order
# they appear in each of the csv data rows. We can make variables to hold
# the column numbers of the data fields we want to use:
UID=0 # CAMIS field holds a unique id
name=1 # the DBA field "doing business as"
borough=2 # BORO field has code numbers for the 5 boroughs
bcodes = {'1':'Manhattan','2':'Bronx','3':'Brooklyn','4':'Queens',\
          '5':'StatenIsland'} # to convert the codes into text
bldg = 3 # building number
street = 4
zipcode = 5
#skip phone
cuisine = 7
idate = 8 # inspection date
action = 10 # action taken due to inspection9
gradefield = 14


# The data show the restaurant name, type of cuisine, location, borough,
# inspection grade and date of inspection.

#The analysis compares Chinese and Mexican cuisine restaurants in Brooklyn
# a Restaurant class is defined to hold the data:
class Restaurant:
    def __init__ (self, name='', uniqueid='', cuisine='',location = '',\
                 borough='',grade='',inspectdate=''):
        self.cuisine = cuisine
        self.location = location
        self.borough = borough
        self.grade = grade
        self.inspectdate = inspectdate
        self.name = name
        self.uniqueid = uniqueid

# Read the data in, one line at a time, saving the Chinese and Mexican
# restaurants in two dictionaries
Chinese = {}
Mexican = {}
datafile = "DOHMH_New_York_City_Restaurant_Inspection_Results.csv"

with open(datafile, newline='') as csvfile:
    datareader = csv.reader(csvfile,delimiter = ',', quotechar='|')
    for row in datareader:
        # skip this row unless this is a Mexican or Chinese restaurant
        #print (len(row),row)
        lc = row[cuisine].lower() # convert cuisine to lowercase to be sure case doesn't matter
        if not(('chinese' in lc) or ('mexican' in lc)): # separate booleans with parens to avoid confusion
            continue # to next row
        # here we have to know the positions in the list of fields
        # of the data values we want to use to create a Restaurant object, so
        # we can use the column number variables we defined earlier:
        r = Restaurant(row[name],row[UID],row[cuisine],' '.join([row[bldg],row[street]]),\
                       row[borough],row[gradefield],row[idate])
        # put the restaurant object r into the right dictionary:
        if lc in 'chinese':
            Chinese[row[UID]]=r
        else:
            Mexican[row[UID]]=r
# now we have dictionaries of all the Mexican and Chinese restaurant inspections
# Let's see how many there are:
Mexcount = len(Mexican)
Chicount= len(Chinese)
# let's get the keys to make it easy to iterate through the dictionaries:
mexkeys=Mexican.keys()
chikeys=Chinese.keys()
# let's see how many of each grade the two restaurant types received:
def gradecount(restdict,gradefield=14): # make a function to 
    #return a dict of grades with counts eg{'A':100,'B':35}
    klist=restdict.keys()
    gradedict={}
    for r in klist:
        row=restdict[r] # returns a Restaurant object
        grade=row.grade
        if grade in gradedict:
            gradedict[grade] += 1
        else:
            print(grade,str(row.uniqueid))
            gradedict[grade]=1 # if it isn't in the dict, add it
    return gradedict
        
Mexgrades = gradecount(Mexican,gradefield)
Chigrades = gradecount(Chinese,gradefield)
for g in 'ABCZ': # some grade field have non-grade text, just get letter grades
    print ('Mexican grade ',g ,Mexgrades[g])
    print ('Chinese grade ',g ,Chigrades[g])
        
