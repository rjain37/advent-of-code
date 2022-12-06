from collections import Counter
import string
text = open('text6.txt', 'r')

data = text.read()

ans = 0

for i in range(0, len(data)- 13, 1):
    freq = Counter(data[i:i+14])
    # print(data[i:i+4])
    if(len(freq) == 14):
        print(str(i+14))
        break

# for line in f:


print(ans)