word_lst = []
word_dict = {}
 
with open(r"F:\123\python-practise\Pyhon100Cases\词中文.txt","r",encoding='utf-8') as f1 ,open("词次数.txt",'w') as f2:
   for line in f1:
       word_lst.append(line.split('/'))
 
   for item in word_lst:
       for item2 in item:
           if item2.strip() not in "，！。“”" :
               if   item2 not in word_dict:
                   word_dict[item2] = 1
               else :
                   word_dict[item2] += 1
 
   for key in word_dict:
       print (key,word_dict[key])
       f2.write(key+' '+str(word_dict[key]))