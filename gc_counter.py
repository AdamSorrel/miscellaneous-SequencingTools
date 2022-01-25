import argparse
import pandas as pd

parser = argparse.ArgumentParser(description='# Counting the GC content in fastq or fasta files.')

parser.add_argument('-i','--in', dest='IN', help='Input file.')
parser.add_argument('-o','--out', dest='OUT', help='Output file.')

args = parser.parse_args()

################################################################################

def GC_counter(sequence):
    A_count = sequence.count("A")
    T_count = sequence.count("T")

    G_count = sequence.count("G")
    C_count = sequence.count("C")

    GC_count = ((G_count + C_count)*100)/(A_count + T_count + G_count + C_count)

    return GC_count

input_format = "Unknown"

with open(args.IN, 'r') as f_in:
    for line in f_in:
        if line[0] == ">" and input_format != "putative fastq":
            input_format = "fasta"
            print("Input file determined as fasta format.")

        if line[0] == "@":
            # Possibly a fasta file. Verifying the presence of the "+" operator between sequence and quality files
            # Skipping one loop (the sequence loop)
            input_format = "putative fastq"
            continue
        if line[0] == "+" and input_format == "putative fastq":
            input_format = "fastq"
            print("Input file determined as fasta format.")

        if input_format == "fasta" or input_format == "fastq":
            # Input format has been determined
            break


output_dictionary = {}

# The actual search
if input_format == "fasta":
    with open(args.IN, 'r') as f_in:
        while True:
            header = f_in.readline()
            sequence = f_in.readline()

            if not sequence:
                break

            try:
                output_dictionary[header] = GC_counter(sequence)
            except:
                print("Header: {}".format(header))
                print("Sequence: {}".format(sequence))

                quit()


if input_format == "fastq":
    with open(args.IN, 'r') as f_in:
        while True:
            header = f_in.readline()
            sequence = f_in.readline()

            plus = f_in.readline()
            quality = f_in.readline()

            if not sequence:
                break

            output_dictionary[header.rstrip()] = GC_counter(sequence)


# Generating a pandas data frame
df1 = pd.DataFrame(list(output_dictionary.items()), columns=['Header', 'GC content'])

df1.to_csv(args.OUT)

