from nltk.tokenize import word_tokenize
import csv

f1= open("F:/FinanceProject/code/new/filpos.csv",'rb')
f2= open("F:/FinanceProject/code/new/filneg.csv",'rb')
csv1=csv.reader(f1)
csv2=csv.reader(f2)

for line in f1.readlines():
    lin_aa=line.strip().split("\n")
    word=word_tokenize(lin_aa)
    print word

#all_words=set(word.lower)
#all_words=set(word.lower() for passage in train for word in word_tokenize(passage[0]))
