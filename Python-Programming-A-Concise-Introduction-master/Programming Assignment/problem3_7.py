import csv
def problem3_7(csv_pricefile, flower):
    fin = open(csv_pricefile)
    reader = csv.reader(fin)
    for row in reader:
        if row[0]==flower:
            print(row[1])