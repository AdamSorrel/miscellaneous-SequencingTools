import csv
import argparse

parser = argparse.ArgumentParser(description='# This program parses an output file from a sina alignment into a taxonomy file')

parser.add_argument('-i','--in', dest='IN', help='Input file.')
parser.add_argument('-o','--out', dest='OUT', help='Output file.')

args = parser.parse_args()

################################################################################

header = True

with open(args.IN, 'r') as in_csv, open(args.OUT, 'w') as out_csv:
    inCsv = csv.reader(in_csv, delimiter=',')
    outCsv = csv.writer(out_csv)
    for line in inCsv:
        if header == True:
            line = ['', 'Domain', 'Phylum', 'Class', 'Order', 'Family', 'Genus']
            outCsv.writerow(line)
            header = False
            continue
        try:
            tax = line[13]
        except:
            print("Line is incomplete!")
            print(line[0])
        tax = tax.split(";")
        tax = tax[:-1]
        if len(tax) != 6:
            n = 6 - len(tax)
            filler = ['Unclassified'] * n
            tax = tax + filler
        line = [line[0]]
        line = line + tax
        outCsv.writerow(line)
