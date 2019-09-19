import nltk
import re

iinput_text =input("文字を入力してください。")

text =nltk.word_tokenize(str(iinput_text))
#第一文型の判定の文
tag_text =nltk.pos_tag(text)
#主語の判定名詞と代名詞
if re.search('(NN|NNP|NNS|PRP)',tag_text[0][1]):
    print('S:主語')
print(tag_text[0][1])
#There isの文法項目を書いてみる
# if re.search('^There ' '+is|are',text) :
#     print('sucess')
print('品詞',nltk.pos_tag(text))
print('文型',)
