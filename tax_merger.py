import argparse
import os
import pandas as pd

parser = argparse.ArgumentParser(description='Preparing a barplot from phyloseq barplot data.')

parser.add_argument('--input','-i', dest='IN', type=str, help='Input folder', required=True)
parser.add_argument('--output', '-o', dest='OUT', type=str, help='Output file', required=True, default="taxonomy.csv")

args = parser.parse_args()

#######################################################################################################################

tax_dict = {}

def taxonomy_parser(file_in, tax_dict):
    otu_name = "none"
    with open(file_in) as f_in:

        for line in f_in:
            line = line.split(" ")
            if line[0] == "sequence_identifier:":
                otu_name = line[1].rstrip()
                if len(otu_name) < 7:
                    m = 7 - len(otu_name)
                    otu_name = otu_name[0:3] + "0"*m + otu_name[(m-4):]
            if line[0] == "lca_tax_slv:" and otu_name != "none":
                taxonomy = line[1].rstrip()
                taxonomy = taxonomy.split(";")
                if taxonomy[-1] == "":
                    tax_check = taxonomy[:-1]
                else:
                    tax_check = taxonomy
                if len(tax_check) < 6:
                    n = 6 - len(tax_check)
                    tax_check = tax_check + ["Unclassified"]*n
                    #taxonomy = ",".join(tax_check)
                    taxonomy = tax_check
                #else:
                    #taxonomy = ",".join(taxonomy)
                if len(taxonomy) > 6:
                    taxonomy = taxonomy[:-1]
                if len(taxonomy) > 6:
                    print(taxonomy)
                    print(file_in)
                    taxonomy = ["Unclassified"]*6
                tax_dict[otu_name] = taxonomy
                otu_name = "none"
    return tax_dict

os.chdir(args.IN)

files = os.listdir()

for file_in in files:
    if file_in[:len(args.IN)] == args.IN:
        taxonomy_parser(file_in, tax_dict)

labels = ["Domain", "Phylum", "Class", "Order", "Family", "Genus"]
df1 = pd.DataFrame.from_dict(tax_dict, orient="index", columns=labels)

df1.sort_values

os.chdir("../")

df1.to_csv("taxonomy.csv", index=True, index_label= "Name")