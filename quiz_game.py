Question = ["日本で1番高い山は？", "日本で2番目にた高い山は？", "日本で1番低い山は？"]
ans = ["富士山", "北岳", "天保山"]

for i in range(3):
	print(Question[i])
	Player_ans = input()
	if Player_ans == ans[i]:
		print("正解です")
	else:
		print("不正解です")
		