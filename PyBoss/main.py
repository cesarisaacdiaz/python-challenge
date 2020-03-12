import os
import csv

us_state_abbrev = {
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

emp_id = []
first_name = []
last_name = []
emp_dobs = []
ssn = []
state = []


file_csv = os.path.join("employee_data.csv")
file_output = os.path.join("employee_new_db.csv")

with open(file_csv, newline='') as csv_employee:
    csvreader = csv.reader(csv_employee,delimiter=',')
    next(csvreader, None)

    for row in csvreader:
        emp_id.append(row[0])
        nombre = row[1].split(" ")
        first_name.append(nombre[0])
        last_name.append(nombre[1])
        dob= row[2].split("-")

        year = dob[0]
        month = dob[1]
        day = dob[2]

        format_dob = f"{month}/{day}/{year}"
        emp_dobs.append(format_dob)

        #split_ssn = list(row[3])
        #split_ssn[0:3]=("*","*","*")
        #split_ssn[4:6]=("*","*")
        #format_ssn = "".join(split_ssn)

        split_ssn = row[3].split("-")
        format_ssn = ("***-**-"+split_ssn[2])

        ssn.append(format_ssn)

        state_complete = us_state_abbrev[row[4]]

        state.append(state_complete)

        employee_new_db = zip(emp_id,first_name,last_name,emp_dobs,ssn,state)

with open(file_output,"w",newline="") as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["Emp Id","First Name","Last Name","DOB","SSN","State"])
    writer.writerows(employee_new_db)