import time

data = []
count = 0
#讀取檔案
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 100000 == 0: #如果count餘數是0才印出(%為求餘數)
			print(len(data)) #目前讀取進度
print('檔案讀取完畢，總共有', len(data), '資料')

print(data[0])


#計算每篇留言的平均字數
read_len = 0
for d in data:
	i = len(d)
	read_len = read_len + i #將每則留言加總
print ('留言的平均長度為' , read_len / len(data) ,'字') #去除以總筆數


#篩選留言長度，小於100
#加入到新的清單
new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('留言長度小於100的留言，總共有', len(new) ,'筆')
print(new[0])
print(new[1])

#篩選有提到good的留言

good = []
for d in data:
	if 'good' in d: #如果清單內有good
		good.append(d)
print('一共有', len(good) ,'筆，提到good。')

#上面篩選GOOD清單，快寫法:

good = [d for d in data if 'good' in d]
print(len(good))

#bad有沒有再留言內
#有的話印true
#沒有印false

bad = []
for d in data:
	bad.append('bad' in d)
print(bad)

#快寫法

bad = ['bad' in d for d in data]
print(bad)


#文字計數
start_time = time.time()
wc = {} #word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1 #如果有新增過值+1
		else:
			wc[word] = 1  #新增新的key進wc字典

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])
end_time = time.time()
print('花了', end_time - start_time, '秒')
while  True:
	word = input('請問你想查甚麼字: ')
	if word == 'q':
		break
	if word in wc: 	
		print(word, '出現過的次數為', wc[word])
	else:
		print(word, '這個字沒有出現過喔!')
print('感謝使用本查詢功能!')	




