data = []
count = 0


with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 100000 == 0: #如果count餘數是0才印出(%為求餘數)
			print(len(data)) #目前讀取進度
print('檔案讀取完畢，總共有', len(data), '資料')

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