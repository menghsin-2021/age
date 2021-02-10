driving = input('請問你有沒有開過車?')
if driving != '有' and driving != '沒有':
	print('給我輸入"有"或"沒有"')
	raise SystemExit
	
age = input('請問你的年齡?')
age = int(age)
if driving == '有':
	if age >= 18:
		print('你通過測驗囉!')
	else:
		print('嘿嘿 偷開車')
elif driving == '沒有':
	if age >= 18:
		print('快去考駕照啦')
	else:
		print('讚 快可以考駕照了')
else:
	print('給我重新輸入！！(有/沒有)')
