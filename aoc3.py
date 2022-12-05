import string
text = open('text3.txt', 'r')

data = text.readlines()

ans = 0

strings = []
for line in data:
    strings.append(line.strip())

common = []

values = dict()
for index, letter in enumerate(string.ascii_lowercase):
   values[letter] = index + 1

for index, letter in enumerate(string.ascii_uppercase):
   values[letter] = index + 27

# for line in strings:
#     half = slice(0, len(line)//2)
#     half2 = slice(len(line)//2, len(line))
#     unique_1 = [w for w in set(line[half]) if w in line[half2]]
#     common.append(''.join(unique_1))

for i in range(0, len(strings), 3):
    one = strings[i]
    two = strings[i+1]
    three = strings[i+2]
    unique_1 = [w for w in set(one) if w in two]
    ok = [w for w in set(''.join(unique_1)) if w in three]
    common.append(''.join(ok))



for char in common:
    ans += values[char]



print(ans)