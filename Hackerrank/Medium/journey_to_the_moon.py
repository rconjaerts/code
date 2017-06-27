'''
Problem: https://www.hackerrank.com/challenges/journey-to-the-moon
Solved: False

Issue: Some errors on testcases
'''

inp = input().split(" ")
numb_astr = int(inp[0])
numb_lines = int(inp[1])
all_astr = {}

# build list of astronauts per country
for _ in range(numb_lines):
    inp = input().split(" ")
    astr1 = int(inp[0])
    astr2 = int(inp[1])
    
    if astr1 in all_astr and astr2 in all_astr:
        all_astr[astr1].extend(all_astr[astr2])
        all_astr[astr2] = all_astr[astr1]
    elif astr1 in all_astr:
        astr_c = all_astr[astr1]
        astr_c.append(astr2)
        for x in astr_c:
            all_astr[x] = astr_c
    elif astr2 in all_astr:
        astr_c = all_astr[astr2]
        astr_c.append(astr1)
        for x in astr_c:
            all_astr[x] = astr_c
    else:
        all_astr[astr1] = [astr1, astr2]
        all_astr[astr2] = [astr1, astr2]        
        
# calculate size of each country
country_sizes = []
for x in range(numb_astr):
    if not x in all_astr:
        country_sizes.append(1)        

for x in range(numb_astr):
    if x in all_astr:
        country_sizes.append(len(all_astr[x]))
        values = all_astr[x]
        for val in values:
            if val in all_astr:
                del all_astr[val]

# count number of different combinations
sum1 = 0
result = 0
for x in country_sizes:
    result += sum1*x
    sum1 += x

print(result)