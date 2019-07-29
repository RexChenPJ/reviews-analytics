data = []
count = 0

with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0: #如果count餘數是0才印出(%為求餘數)
			print(len(data)) #目前讀取進度
print(len(data))
print(data[0])
print('--------------------------------------')
print(data[1])