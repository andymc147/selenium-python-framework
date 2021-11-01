import csv

def getCSVData(fileName):

    # create an empty list to store rows
    rows = []

    # open the csv file
    dataFile = open(fileName, "r")

    # create a CSV reader from CSV file
    reader = csv.reader(dataFile)

    # skip the headers
    next(reader)   # This csv file has a first record (column names) that we don't want to process

    #add rows from
    for row in reader:
        rows.append(row)
    return rows

