from Bio import SeqIO
import argparse
import os

parser = argparse.ArgumentParser(description='# This program trims primers from a sequence.')

parser.add_argument('-f','--folder', dest='FOLD', help='Input folder.')
parser.add_argument('-i','--in', dest='IN', help='General input file name. This is to differentiate from some organisation files, programs etc.')
parser.add_argument('-pre','--prefix', dest='PRE', help='Length of a prefix to trim.')
parser.add_argument('-suff','--suffix', dest='SUFF', help='Length of a suffix to trim.')

args = parser.parse_args()

################################################################################

def renameSeq(file_in, args):
    name = file_in[:-6]
    number = 1
    file_out = "".join('../' + name + '_cut.fastq')


    with open(file_in, 'r') as f_in, open(file_out, 'a') as f_out:
        for record in SeqIO.parse(f_in, "fastq"):
            record = record[int(args.PRE):-int(args.SUFF)]
            SeqIO.write(record,f_out,'fastq')

os.chdir(args.FOLD)

files = os.listdir()

for entry in files:
    if entry[:len(args.IN)] == args.IN:
        renameSeq(entry, args)
