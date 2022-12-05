import string
text = open('text5.txt', 'r')

data = text.readlines()

ans = 0

# [M] [H]         [N]                
# [S] [W]         [F]     [W] [V]    
# [J] [J]         [B]     [S] [B] [F]
# [L] [F] [G]     [C]     [L] [N] [N]
# [V] [Z] [D]     [P] [W] [G] [F] [Z]
# [F] [D] [C] [S] [W] [M] [N] [H] [H]
# [N] [N] [R] [B] [Z] [R] [T] [T] [M]
# [R] [P] [W] [N] [M] [P] [R] [Q] [L]
#  1   2   3   4   5   6   7   8   9 


#im a modern genius
crates = [['R', 'N', 'F', 'V', "L", "J", "S", "M"], ["P", "N", "D", "Z", "F", "J", "W", "H"], ["W", "R", "C", "D", "G"], ["N", "B", "S"], ["M,", "Z", "W", "P", "C", "B", "F", "N"], ["P", "R", "M", "W"], ["R", "T", "N", "G", "L", "S", "W"], ["Q", "T", "H", "F", "N", "B", "V"], ["L", "M", "H", "Z", "N", "F"]]
# for line in data:
#     line = line.strip()
#     line = line.split(' ')
#     num = int(line[1])
#     start = int(line[3]) - 1
#     end = int(line[5]) - 1
#     for i in range(num):
#         crates[end].append(crates[start][len(crates[start]) - 1])
#         crates[start] = crates[start][:-1]

for line in data:
    line = line.strip()
    line = line.split(' ')
    num = int(line[1])
    start = int(line[3]) - 1
    end = int(line[5]) - 1
    for el in crates[start][-num:]:
        crates[end].append(el)

    for i in range(num):
        crates[start] = crates[start][:-1]

for line in crates:
    print(line[-1])

