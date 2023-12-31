data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line.strip())

#print(data[0])

wc = {} # word_count
for d in data:
    words = d.split()
    for word in words:   
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1
    #print(wc)

for word in wc:
    if wc[word] > 100000:
        print(word, wc[word])
print(len(wc))

while True:
    word = input('找啥: ')
    if word == 'q':
        break
    if word in wc:
        print(word, '出現過', wc[word], '次')
    else:
        print('沒出現過喔')
print('結束')

    






# sum = 0   
# for d in data:
#     sum = sum + len(d)

# print('每筆留言平均長度為', sum / len(data), '個字')

# new = []
# for d in data:
#     if len(d) < 100:
#         new.append(d)
# print('共有', len(new), '筆留言長度小於100')

# good = []
# for d in data:
#     if 'good' in d:
#         good.append(d)
# #good = [d for d in data if 'good' in d] 
# print('共有', len(good), '筆留言包含good')




