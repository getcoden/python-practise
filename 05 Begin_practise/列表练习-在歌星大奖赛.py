'''
1.【项目：大奖赛计分】

　　在歌星大奖赛中，有 10 个评委为参赛的选手打分，分数为 1~100 分。选手最后得分为：去掉一个最高分和一个最低分后其余 8 个分数的平均值。请编写一个程序实现。
　　【项目扩展 1（选做）】大奖赛编的计分程序，成绩在 0-10 之间，输入错误时要能马上重新输入，选手最后得分为：去掉一个最高分和一个最低分。评委人数（图中为 7）需要在在程序开始运行时输入（这比固定 10 个评委的程序更有适应性了）。
　　【项目扩展 2（选做）】在扩展 1 基础上，输出当前选手的最后得分后，提示 “按任意键计算下一位选手的成绩，退出请选择 N：” 如果输入的不是 N 或 n，可以为下一位选手计算成绩。运行结果如图所示。
'''
# score = [0,0,0,0,0,0,0,0,0,0]
# print('请输入10位评委对选手的打分（0~100分）:')
# for i in range(0, 10):
# 	score[i] = int(input('请输入第%d位评委的打分：' % (i + 1)))
# 	while score[i] < 0 or score[i] > 100:
# 		score[i] = int(input('第%d位打分错误，请重新打分:'% (i + 1)))
# 		score.sort()
# print('去掉一个最高分%d分，去掉一个最低分%d分，最终得分:%.2f' % (score[9], score[0], (sum(score) - score[0] - score[9]) / 8))
		
#【项目扩展 1（代码）】
'''
scores = []
count = int(input('请确认评委人数:'))
print('请输入%d位评委对选手的打分（0~10分）：' % count)
for i in range(count):
	score = float(input('第%d位评委打分:' % (i + 1)))
	while score < 0 or score > 10:
		score = float(input('打分错误，请重新打分（0~10分）：'))
	scores.append(score)
	scores.sort()
print ("去掉一个最高分 %.2f 分，去掉一个最低分 %.2f 分，最终得分：%.2f" %(scores [count-1],scores [0],(sum (scores)-scores [0]-scores [count-1])/(count-2)))
'''
'''
#【项目扩展 2（代码）】
scores = []
flag = ''
count = int(input('请确认评委人数：'))
print('请输入%d位评委对选手的打分（0~10分）：' % count)
while flag != 'n' and flag != 'N':
	for i in range(count):
		score = float(input('第%d位评委打分:' % (i + 1)))
		while score < 0 or score > 10:
			score = float(input('打分错误，请重新打分（0~10分）:'))
		scores.append(score)
		scores.sort()
	print ("去掉一个最高分 %.2f 分，去掉一个最低分 %.2f 分，最终得分：%.2f" %(scores [count-1],scores [0],(sum (scores)-scores [0]-scores [count-1])/(count-2)))
	scores.clear ()
	flag = input ("按任意键计算下一位选手的成绩，退出请选择 N 或 n：")
'''

'''
【项目 - 排队看病模拟】
　编写一个程序，反映病人到医院看病，排队看医生的情况。在病人排队过程中，主要重复两件事：

1）病人到达诊室，将病历本交给护士，排到等待队列中候诊。
2）护士从等待队列中取出下一位病人的病历，该病人进入诊室就诊。
求模拟病人等待就诊这一过程。程序采用菜单方式，其选项及功能说明如下：
1）排队 —— 输入排队病人的病历号，加入到病人排队队列中。
2）就诊 —— 病人排队队列中最前面的病人就诊，并将其从队列中删除。
3）查看排队 —— 从队首到队尾列出所有的排队病人的病历号。
4）不再排队，余下顺序就诊 —— 从队首到队尾列出所有的排队病人的病历号，并退出运行。
5）下班 —— 退出运行，提示未就诊的病人明天再来。
'''

list = []
while True:
	print ("\n"+"西 开 国 际 医 院".center (50,"*")+"\n")
	print ("1.  就诊排队".center (50," "))
	print ("2.  顺序就诊".center (50," "))
	print ("3.  查看排队".center (50," "))
	print ("4.  不再排队".center (50," "))
	print ("5.  医生下班".center (50," "))
	score = int (input ("\n 请选择接下来你要做的操作："))
	if score == 1:
		number=input ("\n 请输入病人病历号：")
		list.insert (0,number)
		print ("排队成功！\n")
	elif score == 2:
		if len (list) == 0:
			print ("\n 没有病人在排队就诊了！\n")
		else:
			print ("\n 病历号为 % s 的病人开始就诊。\n" % list.pop ())
	elif score == 3:
		if len (list) == 0:
			print ("\n 没有病人在排队就诊了！\n")
		else:
			print ("\n 当前排队病人：")
		for i in list [::-1]:
			print (i,end='  ')
			print ("\n")
	elif score == 4:
		if len (list) == 0:
			print ("\n 没有病人在排队就诊了！\n")
		else:
			print ("\n 所有在排队的病人不再排队：")
		for i in list [::-1]:
			print(i, end='  ')
	elif score ==5:
		if len(list) == 0:
			print("\n没有就诊病人了，愉快下班！\n")
		else:
			print("\n医生下班，请以下未就诊的病人明日再来：")
			for i in list[::-1]:
							print(i,end='  ')
			print("\n")
			list.clear()
	exit()
