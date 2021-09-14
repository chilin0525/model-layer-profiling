import csv

with open('pyprof', newline='') as csvfile:

    rows = csv.reader(csvfile,delimiter=",")

    for row in rows:
        print( "%-40s %s" % (row[4], row[7]))