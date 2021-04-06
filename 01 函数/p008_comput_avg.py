
def print_comput_avg():
	score = []
	with open('./comput.txt') as fin:
		for line in fin:
			line = line[:-1]
			fields = line.split(',')
			score.append(int(fields[-1]))
	max_score = max(score)
	min_score = min(score)
	avg_score = round(sum(score) / len(score), 2)
	return max_score,min_score,avg_score
	
max_score, min_score, avg_score = print_comput_avg()
print(f'max_score={max_score},min_score={min_score},avg_score={avg_score}')