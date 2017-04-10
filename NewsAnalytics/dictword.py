import re
import csv
import nltk
import copy
from nltk import word_tokenize
#from text.classifiers import NaiveBayesClassifier

f1=open("F:/FinanceProject/code/new/harng.csv",'rb')
f2=open("F:/FinanceProject/code/new/harpos.csv",'rb')
filpos=open("F:/FinanceProject/code/new/filpos.csv",'w')
filneg=open("F:/FinanceProject/code/new/filneg.csv",'w')
reader=csv.reader(f1)
neg=[]
pos=[]
np=[]

for line in f2.readlines():
    lin_aa=line.strip().split("\n")
    print lin_aa[0]
    pos.append([lin_aa[0],'pos'])
    np.append((lin_aa[0],'pos'))

for line in f1.readlines():
    lin_aa=line.strip().split("\n")
    print lin_aa[0]
    neg.append([lin_aa[0],'neg'])
    np.append((lin_aa[0],'neg'))


    #col2=lin_aa.split('\n')


print "Ng",neg[9][0]
print lin_aa[0]


for x ,y in neg:
    print >>filneg,x,y


for x ,y in pos:
    print >>filpos,x,y
filpos.close()
filneg.close()

all_words=[]

for i in range(0,20):
    print i,pos[i][0]
    all_words.append((pos[i][0].lower(),'pos'))

for i in range(0,20):
    print i,neg[i][0]
    all_words.append((neg[i][0].lower(),'neg'))




n=np
t=[]
#print "NP 1=",n
'''
d={'this','pos'}
print d
for x in n:
    for word in all_words:
        p=(word in x[0])
        print p
        d[word]=p


print 'd=',d
'''



lt = []
lt1 = {}
for i in range(len(all_words)):
    lt1[all_words[i][0]] = False
lt.append(lt1)
lt.append('neg')
print(lt)

t  = []
tmp = []

for i in range(len(all_words)):
    tmp.append(copy.deepcopy(lt1))
    tmp[i][all_words[i][0]] = True
    t.append((tmp[i],all_words[i][1]))

    '''
        for j in range(len(all_words)):
            if j == i:
                tmp1[all_words[i][0]] = True
            else:
                tmp1[all_words[i][0]] = False
        tmp.append((tmp1,'pos'))
        t.append(tmp)
        tmp1= {}
        tmp = []
    '''


#print(t[:50])


'''    #print x[0],x[1]

t=[({word:(word.lower() in x[0])for word in all_words},x[1])for x in n]
'''
classifier = nltk.NaiveBayesClassifier.train(t)

classifier.show_most_informative_features()

#print t

#print all_words
#print "NP",np
#print "T",t[:100]
test_sentence= "he is a abnormal person"
for word in all_words:
    print "All words 1 :", word[0]
test_sent_features = {word[0]: (word[0] in word_tokenize(test_sentence.lower())) for word in all_words}

print "test sent",test_sent_features

print (classifier.classify(test_sent_features))
