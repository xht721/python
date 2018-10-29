import nltk 
import jieba
# from nltk.book import *
# file = open(r'd:/test1.txt').read()
# text = nltk.text.Text( jieba.lcut(file))
# print(text)
def segment(text,segs):
    word = []
    last = 0
    for i in range(len(segs)):
        if segs[i] == '1':
            word.append(text[last:i+1])
            last = i+1
    word.append(text[last:])
    return word
def evaluate(text,segs):
    words = segment(text,segs)
    text_size = len(words)
    print(text_size)
    lexicon_size = len(' '.join(list(set(words))))
    lexicon = ' '.join(list(set(words)))
    print(lexicon)
    return text_size+lexicon_size

text = "doyouseethekittyseethedoggydoyoulikethekittylikethedoggy"
seg1 = "0000000000000001000000000010000000000000000100000000000"
seg2 ="0100100100100001001001000010100100010010000100010010000"
seg3 ="0000100100000011001000000110000100010000001100010000001"
print(evaluate(text,seg3))