data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line.strip())

sum = 0   
for d in data:
    sum = sum + len(d)

print('每筆留言平均長度為', sum / len(data), '個字')

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('共有', len(new), '筆留言長度小於100')

good = []
for d in data:
    if 'good' in d:
        good.append(d)
#good = [d for d in data if 'good' in d] 
print('共有', len(good), '筆留言包含good')
print(good[0])


