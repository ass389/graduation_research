import nltk
import re

iinput_text =input("文字を入力してください。")

text =nltk.word_tokenize(str(iinput_text))
tag_text =nltk.pos_tag(text)
sentence_p =[]
sentence=''
"""
    第一文型の判定
    1語の場合
    NN:名詞
    PRP:代名詞
    DT:限定詞
    There+is/are

    2語の場合
    The+形容詞
    The+名詞
    To不定詞
    動名詞

    動詞の判定

"""
if re.search('(NN|NNP|NNS|PRP|DT)',tag_text[0][1]):
    print('S:主語')
    sentence_p.append('S')
    if re.search('VB|VBN',tag_text[1][1]):
        sentence_p.append('V')
        print(sentence_p)
#2語の場合
elif re.search('(PRP$|DT)',tag_text[0][1])and re.search('(NN|JJ)'):
    sentence_p.append('S')
    if re.search('VB|VB'):
        sentence_p.append('V')
elif re.search('To',text[0][1])and re.search('VB|VBN'):
    sentence_p.append('S')
    if re.search('VB|VBN'):
        sentence_p.append('V')
elif re.search('VG|VN',tag_text[0][1])+re.search('',tag_text[1][1]):
    sentence_p.append('S')
    if re.search('VB|VBN'):
        sentence_p.append('V')

#主語が3語以上の場合


#第一文型の出力
if re.search('S',sentence_p[0]) and re.search('V',sentence_p[1]):
    sentence ='第一文型'
print('',nltk.pos_tag(text))
print('文型',sentence)
