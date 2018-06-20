import os
import csv

#declare variables
header = ['emp_id','first_name','last_name','dob','ssn','state']
emp_id = []
first_name = []
last_name = []
dob = []
ssn = []
state = []

#dictionary of state abbreviations
abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
def find_first(name):
    name_parts = name.split(" ")
    return name_parts[0]

def find_last(name):
    name_parts = name.split(" ")
    return name_parts[1]

def find_ssn(digits):
    number = digits.split("-")
    last_four = "***-**-" + number[2]
    return last_four
confirm = 'y'
while confirm == 'y':
    #read csv file
    file_name = input("What is the name of the file you would like to read? \n(be sure to include \"\")\n")
    csvpath = os.path.join('Resources',file_name)
    with open (csvpath) as csvfile:
        csvreader = csv.reader(csvfile,delimiter = ',' )
        header = next(csvreader)
        for row in csvreader:
            emp_id.append(int(row[0]))
            first = find_first(row[1])
            first_name.append(first)
            last = find_last(row[1])
            last_name.append(last)
            dob.append(row[2])
            number = find_ssn(row[3])
            ssn.append(number)
            state.append(abbrev[row[4]])
        #create a zipped list
        zipped_list = zip(emp_id,first_name,last_name,dob,ssn,state)
    
    #write to csv file
    output_name = input("What would you like to name your output file?")
    output_file = os.path.join("Output", output_name)
    with open (output_file,"w") as datafile:
        writer = csv.writer(datafile)
        writer.writerow(header)
        writer.writerows(zipped_list)

    confirm = input("Would you like to continue? ['y'] or ['n']")


