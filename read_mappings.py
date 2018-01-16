# this changes the mapping into a more c++ friendly format
import sys

path = sys.argv[1]
lines = []
with open(path, 'r') as f:
    for l in f:
        temp = l.strip().split('\t');
        line = '\n'.join([temp[0],temp[2],temp[3],temp[5],temp[7],temp[8]])
        lines.append(line)

with open('temp', 'w') as f:
    f.write('\n'.join(lines))

