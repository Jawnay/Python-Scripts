# open the input file and read all lines
with open("input.txt", "r") as f:
    lines = f.readlines()

# filter out lines that are completely blank
cleaned = [line for line in lines if line.strip() != ""]

# write cleaned lines to output file
with open("output.txt", "w") as f:
    f.writelines(cleaned)
