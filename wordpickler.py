import pickle
fin = open('words.txt')
a = dict()
for line in fin:
    word = line.strip().lower()
    first_letter=word[0]
    if first_letter not in a:
        a[first_letter]=set()
    a[first_letter].add(word)

#print (pickle.dumps(a))
#pickle.word (open)
fout = open('output.txt', 'w')
fout.write(str(pickle.dumps(a)))
fout.close()