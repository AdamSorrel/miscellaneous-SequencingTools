from Bio import SeqIO
import argparse
import os

parser = argparse.ArgumentParser(description='# Counting length of sequences.')

parser.add_argument('-i','--in', dest='IN', help='Input file.')
parser.add_argument('-o','--out', dest='OUT', help='Output file.')

args = parser.parse_args()

################################################################################

def findDiffLength(args):
    i = 0
    with open(args.IN, 'r') as f_in, open(args.OUT, 'a') as f_out:
        for record in SeqIO.parse(f_in, "phylip"):
            print(len(record))
            quit()

def convert2phylip(args):
    with open(args.IN, "r") as f_in, open(args.OUT, "w") as f_out:
        sequences = SeqIO.parse(f_in, "fasta")
        count = SeqIO.write(sequences, f_out, "phylip")

        print("Converted %i records" % count)

findDiffLength(args)

#convert2phylip(args)
