import os

os.chdir("/home/stovicek_lab/MiSeq/Nanopore/samples/")
files = os.listdir()

for entry in files:

    with open(entry, "r") as f_in, open("../"+ entry[:-6] + "_out.fq", "w") as f_out:
        for line in f_in:
            if line != "--\n":
                f_out.write(line)
