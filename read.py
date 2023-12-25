data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line.strip())

sum = 0   
for d in data:
    sum = sum + len(d)

print('每筆留言平均長度為', sum / len(data), '個字')

