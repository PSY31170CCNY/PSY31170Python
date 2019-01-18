# classproject.py
# this is an analysis fo the NYC restaurant inspection data
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
UID=1 # CAMIS field holds a unique id
name=2 # the DBA field "doing business as"
borough=3 # BORO field has code numbers for the 5 boroughs
bcodes = {'1':'Manhattan','2':'Bronx','3':'Brooklyn','4':'Queens',\
          '5':'StatenIsland'} # to convert the codes into text
bldg = 4 # building number
street = 5
zipcode = 6
#skip phone
cuisine = 8
idate = 9 # inspection date
action = 10 # action taken due to inspection


# The data show the restaurant name, type of cuisine, location, borough,
# inspection grade and date of inspection.

#The analysis compares Chinese and Mexican cuisine restaurants in Brooklyn
# a Restaurant class is defined to hold the data:
class Restaurant:
    def __init__(self,name='', uniqueid='', cuisine='',location = '',\
                 borough='',grade='',inspectdate='')
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
    datareader = csv.reader(csvfile,delimiter = ' ', quotechar='|')
    for row in datareader:
        # here we have to know the positions in the list of fields
        # of the data values we want to use:
        r = Restaurant(r[
