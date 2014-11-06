# takes one command-line arg: name of file containing hackerschool/private source

from sys import argv

with open(argv[1],"r") as f:
    twitterlines = [x for x in f.readlines() if 'https://twitter' in x]

twitterhandles = []

for i in twitterlines:
    temp = i[i.index("m")+2:i.index('">')]
    twitterhandles.append(temp)

with open("hackerschoolers","w") as g:
    for j in twitterhandles:
        g.write(j+'\n')
