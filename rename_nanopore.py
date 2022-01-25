from Bio import SeqIO
import argparse
import os

parser = argparse.ArgumentParser(description='# This program renames sequences and  trims primers from a sequence.')

parser.add_argument('-i','--in', dest='IN', help='Input folder.')
parser.add_argument('-o','--out', dest='OUT', help='Output folder.')
#parser.add_argument('-r','--remove', dest='REMOVE', help='A an original file name part, that should be replaced by a suffix "_renamed.fastq".')


args = parser.parse_args()

################################################################################

def renameSeq(file_in, args):
    name = file_in.split(".")[0]
    name = name.split("_")[-1]
    name = "nano" + name
    number = 1
    file_out = "".join('../' + args.OUT.split('/')[-2] + '/' + name + "_renamed.fastq")

    with open(file_in, 'r') as f_in, open(file_out, 'a') as f_out:
        for record in SeqIO.parse(f_in, "fastq"):
            record.id = "".join(name + "." + str(number))
            record.name = ""
            record.description = ""
            number += 1
            SeqIO.write(record,f_out,"fastq")


# If there wasn't one already, adding forward slash '/'
if args.OUT[-1] != '/':
    args.OUT = ''.join(args.OUT + '/')

if args.IN[-1] != '/':
    args.IN = ''.join(args.IN + '/')

# If output folder doesn't exist, create one
if not os.path.exists(args.OUT):
    os.makedirs(args.OUT)

os.chdir(args.IN)

files = os.listdir()

for entry in files:
    renameSeq(entry, args)
