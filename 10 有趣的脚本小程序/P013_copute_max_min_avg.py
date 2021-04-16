def comput_score():
	score = []
	with open('./student_grade_input.txt') as fin:
		for line in fin:
			line = line[:-1]
			fields = line.split(',')
			score.append(int(fields[-1]))
		max_score = max(score)
		min_score = min(score)
		avg_score = round(sum(score) / len(score), 2)
		return max_score,min_score,avg_score
			

max_score, min_score, avg_score = comput_score()
print(f'max_score={max_score},min_score={min_score},avg_score={avg_score}')

