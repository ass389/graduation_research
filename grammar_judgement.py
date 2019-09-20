import nltk
import re

iinput_text =input("文字を入力してください。")

text =nltk.word_tokenize(str(iinput_text))
#第一文型の判定の文
tag_text =nltk.pos_tag(text)
#主語の判定名詞と代名詞
#主語が一語の場合
#名詞と代名詞でサーチ
if re.search('(NN|NNP|NNS|PRP|DT)',tag_text[0][1]):
    print('S:主語')
    if re.search('VB|VB',tag_text[1][1]):
        print('V:動詞')
#主語が二語の場合
#所有格の代名詞+名詞or限定詞+名詞
elif re.search('PRP$',tag_text[0][1]):
    print('S:主語')

#主語が三語の場合


print('品詞',nltk.pos_tag(text))
print('文型',)
