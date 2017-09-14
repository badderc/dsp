"""Part III: Dictionary"""

filename = '/faculty.csv'

# Q6: dictionary with last names as keys
fin = open(filename, 'r')
d = {}
for line in fin:
    temp = line.strip().split(',')
    if temp[0] != 'name': # skip first line with column names
        name = temp[0].split(' ')[-1] # just last name of faculty
        title = temp[2] # abbreviate their title
        div = title.find('of ')
        if div == -1:
            div = title.find('is ')
        title2 = title[0:div].strip()
        stats = [temp[1].strip(), title2, temp[3].strip()]
        if name in d:
            d[name].append(stats)
        else:
            d[name] = [stats]

fin.close()
# print first three dictionary pairs
i = 0
for key in d:
    if i == 3:
        break
    print key, d[key], '\n'
    i += 1

# Q7: dictionary with name tuples as keys
fin = open(filename, 'r')
d = {}
for line in fin:
    temp = line.strip().split(',')
    if temp[0] != 'name':
        name = (temp[0].split(' ')[0], temp[0].split(' ')[-1]) # create name tuple
        title = temp[2]  # abbreviate their title
        div = title.find('of ')
        if div == -1:
            div = title.find('is ')
        title2 = title[0:div].strip()
        stats = [temp[1].strip(), title2, temp[3].strip()]
        if name in d:
            d[name].append(stats)
        else:
            d[name] = stats

fin.close()

i = 0
for key in d:
    if i == 3:
        break
    print key, d[key], '\n'
    i += 1

# Q8: print in alphabetical order by last name
for k in sorted(d.keys(), key=lambda n: n[1]):
    print k, d[k]
