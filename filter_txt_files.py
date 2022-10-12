with open(r'./txt/return.txt', 'r') as infile, \
     open(r'./txt/final.txt', 'w') as outfile:
    data = infile.read()
    data = data.replace("/n", "")
    outfile.write(data)