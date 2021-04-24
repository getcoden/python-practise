def count_words(s, n):
	dic = {}
	words = s.split(' ')
	for word in words:
		dic[word] = words.count(word)
	wordslist = sorted(dic.items(), key=lambda kv: (-kv[1], kv[0]))[:n]
	return wordslist

def tes_run():
	print(count_words("cat bat mat cat bat cat baa", 3))
	print(count_words("betty bought a bit of butter but the butter was bitter", 3))

if __name__ == '__main__':
	tes_run()