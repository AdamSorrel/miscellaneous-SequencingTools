from Bio import SeqIO
import argparse
import os

parser = argparse.ArgumentParser(description='# Divides the rep_seq file.')

parser.add_argument('-i','--in', dest='IN', help='Input file.')
parser.add_argument('-o','--out', dest='OUT', help='Output folder.')
parser.add_argument('-c','--count', dest='COUNT', default=1000, help='Number of sequences that should be deposited in each separate file . [Default = 1000]')

args = parser.parse_args()

################################################################################

# If there wasn't one already, adding forward slash '/'
if args.OUT[-1] != '/':
    args.OUT = ''.join(args.OUT + '/')

if not os.path.exists(args.OUT):
    os.makedirs(args.OUT)

file_in = args.IN

# Retrieving the name of the file to split as an output name template.
file_out_name = file_in.split("/")[-1]
file_out_name = file_out_name.split(".")[0]
file_out_name = args.OUT + file_out_name

file_counter = 1
seq_counter = 0

with open(file_in, 'r') as f_in:
    file_out = file_out_name + "_" + str(file_counter) + ".fasta"

    f_out_handle = open(file_out, 'a')
    for record in SeqIO.parse(f_in, "fasta"):

        seq_counter = seq_counter + 1

        if seq_counter > args.COUNT:

            seq_counter = 0
            file_counter = file_counter + 1

            # New output filename
            file_out = file_out_name + "_" + str(file_counter) + ".fasta"

            # Closing the output handle file
            f_out_handle.close()

            f_out_handle = open(file_out, 'a')

        SeqIO.write(record,f_out_handle,"fasta")


    f_out_handle.close()

