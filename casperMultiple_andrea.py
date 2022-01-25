#from Bio import SeqIO
import argparse
import os
from subprocess import Popen

parser = argparse.ArgumentParser(description='# This program renames sequences and trims primers from a sequence.')

parser.add_argument('-i','--in', dest='IN', help='Input folder name.')
parser.add_argument('-n','--name', dest='NAME', help='Output file name prefix (Osnat, Ahuva, ...).')

args = parser.parse_args()

################################################################################

os.chdir(args.IN)

files = os.listdir()

for entry in files:
    name = entry.split("_")
    sampleName = name[0].split("-")
    sampleName = sampleName[0]
    sampleName = sampleName[6:]
    print(sampleName)
    if name[3] == "R1":
        fOutR1 = entry
        fOutR2 = "".join(name[0] + "_" + name[1] + "_" + name[2] + "_" + "R2" + "_" + name[4])
        usearchCommand = ['casper', fOutR1, fOutR2, '-o', ''.join('../' + args.NAME + "_" + sampleName + '_merged')]
        p = Popen(usearchCommand,shell = False)
        p.wait()
