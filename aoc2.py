text = open('text.txt', 'r')

data = text.readlines()

elf = []
me = []
for line in data:
    line = line.split(' ')
    elf.append(line[0])
    me.append(line[1].strip())

points = 0

for i in range(len(elf)):
    match elf[i]:
        case 'A':
            match(me[i]):
                case 'X':
                    points += 3
                case 'Y':
                    points += 3
                    points += 1
                case 'Z':
                    points += 6
                    points += 2
        case 'B':
            match(me[i]):
                case 'X':
                    points += 1
                case 'Y':
                    points += 3
                    points += 2
                case 'Z':
                    points += 3
                    points += 6
        case 'C':
            match(me[i]):
                case 'X':
                    points += 2
                case 'Y':
                    points += 6
                case 'Z':
                    points += 6
                    points += 1
            
print(points)