import string
text = open('text4.txt', 'r')

data = text.readlines()

ans = 0

codes = []
for line in data:
    line = line.strip()
    codes.append(line.split(','))

newcodes = []
for line in codes:
    line[0] = line[0].split('-')
    line[1] = line[1].split('-')
    newcodes.append([list(range(int(line[0][0]), int(line[0][1])+1)), list(range(int(line[1][0]), int(line[1][1])+1))])

# for line in newcodes:
#     if set(line[0]).intersection(set(line[1])) == set(line[0]) or set(line[0]).intersection(set(line[1])) == set(line[1]):
#         ans += 1

for line in newcodes:
    if len(set(line[0]).intersection(set(line[1]))) > 0:
        ans += 1

print(ans)

def integers(a, b):
    return list(range(a, b+1))