import argparse
import re

parser = argparse.ArgumentParser(description='# Program parsing the casper log file.')

parser.add_argument('-i','--in', dest='IN', help='Input file name.')
parser.add_argument('-o','--out', dest='OUT', help='Output filename.')

args = parser.parse_args()

flag = False

output = []

with open(args.IN, 'r') as f_in, open(args.OUT, 'w') as f_out:
    f_out.write("\t".join(["Forward read", "Reverse read", "Total number of reads", "Merged reads",
                 "Merged reads percentage [%]" , "Unmerged reads", "Unmerged reads percentage [%]", "\n"]))
    for line in f_in:

        # File names
        if "Input Files" in line:
            flag = True
            continue

        elif line.strip() == "":
            flag = False

        elif "Merging Result Statistics" in line:
            flag = True
            continue

        elif "TIME" in line:
            flag = False

            # Appending end line and writing into an output file
            output.append("\n")
            f_out.write("\t".join(output))
            output = []

        # Attaching a piece of information to a line
        if flag == True:
            text = line.split(":")[1]
            text = text.strip()
            if "%" in text:
                text = text.split(" ")
                text[1] = text[1][1:-2]
                for element in text:
                    output.append(element)
            else:
                output.append(text)

