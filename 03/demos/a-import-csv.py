import csv 
print(dir(csv))

# Import data using the csv module, with a reader
with open('data\\users-simple-five.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',',quotechar='"')
    for row in csv_reader:
        print(row)


# Can also import as DictReader
field_names = ['Id', 'Reputation', 'Location', 'DisplayName']
with open('data\\users-simple-five.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file, fieldnames=field_names)
    for row in csv_reader:
        print(row)
        print(row['DisplayName'] + ' has a reputation of ' + row['Reputation'])

# Can load unquoted as numbers
with open('data\\users-simple-five.csv') as csv_file:
    csv_reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
    for row in csv_reader:
        print(row)

# But not very flexible
with open('users-five.csv') as csv_file:
    csv_reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
    for row in csv_reader:
        print(row)

 