with open("croatia.csv") as f:
    lines = f.readlines()
for line in lines:
    size = len(line)
    s = ""
    found = False
    for i in range(size):
        if found and line[i+1] == ',':
            value = float(s)
            s = ""
            if line[i] == 'M':
                value *= 1000000
            elif line[i] == 'K':
                value *= 1000
            value = int(value)
            print(str(value), end='')
            found = False
        elif line[i] == '€':
            found = True
        elif not found:
            print(line[i], end='')
        elif found:
            s+=line[i]
   
