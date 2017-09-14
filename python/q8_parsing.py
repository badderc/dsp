# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

filename = 'football.csv'

fin = open(filename, 'r')
d = {}
for line in fin:
    temp = line.split(',')
    if temp[0] != 'Team':
        d[temp[0]] = temp[5:7]

fin.close()

d2 = {}
for key in d:
    goals_for = int(d[key][0])
    goals_against = int(d[key][1])
    diff = abs(goals_for - goals_against)
    if diff not in d2:
        d2[diff] = [key]
    else:
        d2[diff].append(key)

print(d2[min(d2)])
