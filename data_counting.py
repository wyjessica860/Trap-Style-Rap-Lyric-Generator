from collections import Counter
import re
# number of singer:418

with open('data/singer.txt','r') as f:
    sing_already = f.read()
sing_already = re.split(', |\n',sing_already)

a = Counter(sing_already)
sum = 0

for i in list(a.keys()):
    if i.isnumeric():
        sum += a[i]*int(i)
print(sum)       
# there are 8548 songs in total