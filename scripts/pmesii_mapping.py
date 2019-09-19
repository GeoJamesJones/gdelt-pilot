import csv

pmesii_dict = {}
csv_file = "data/EventOntology.csv"
with open(csv_file, 'rb') as f:
    csvreader = csv.reader(f, delimiter=',')
    for row in csvreader:
        iRow = [int(row[8]), int(row[8][:1]), int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[5]), int(row[6]), int(row[7])]
        pmesii_dict[row[9]] = iRow

with open("mappings.txt", 'w') as w:
    w.write(str(pmesii_dict))
w.close()
    

print(pmesii_dict)