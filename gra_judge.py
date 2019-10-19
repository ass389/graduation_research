import nltk
import re
import pprint


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


"""
def judgemnt(text):
    sentence_p=[]
    sentence= ''
    if re.search('(NN.|PRP|DT|EX)',text[0][1]):
        sentence_p.append('S')
        #第二文型
        if re.search('(be|keep|get|look|seem|feel|smell|taste)',text[1][0])and re.search('VB.|VB',text[1][1]):
            sentence_p.append('V')
            if re.search('NN.?|JJ.?',text[2][1]):
                sentence_p.append('C')
        #第三文型
        elif re.search('VB?',text[1][1]):
            sentence_p.append('V')
            if re.search('NN?|PRP?',text[2][1]):
                sentence_p.append('O')
                print('第三文型')
        #第四文型
        elif re.search('give|lend|buy|make|cook',text[1][0])and re.search('VB?',text[1][1]):
            sentence_p.append('V')
            if re.search('NN.?|PRP.?',text[2][1]):
                sentence_p.append('O')
                if re.search('NN.?',text[3][1]):
                    sentence_p.append('O')
        elif re.search('make|keep|paint|call|name|find',text[1][0])and re.search('VB?',text[1][1]):
            sentence_p.append('V')




    #2語の場合
    elif re.search('(PRP$|DT)',text[0][1])and re.search('(NN.|JJ.)',text[1][1]):
        sentence_p.append('S')
        #第二文型の場合
        if re.search('(be|keep|get|look|seem|feel|smell|taste)',text[2][0])and re.search('(VB.)',text[2][1]):
            sentence_p.append('V')
            if re.search('JJ',text[3][1]):
                sentence_p.append('C')
    elif re.search('To',text[0][1])and re.search('VB|VB.',text[1][1]):
        sentence_p.append('S')
        if re.search('VB|VB.',text[2][1]):
            sentence_p.append('V')
    elif re.search('(VG|VN)',text[0][1])and re.search('(NN|NNP)',text[1][1]):
        sentence_p.append('S')
        if re.search('VB|VB.',text[2][1]):
            sentence_p.append('V')

    #主語が3語以上の場合
    #第一文型の出力
    if len(sentence_p) == 2:
        if re.search('S',sentence_p[0]) and re.search('V',sentence_p[1]):
            sentence ='第一文型'
            return sentence
    elif len(sentence_p) ==3:
        if re.search('S',sentence_p[0]) and re.search('V',sentence_p[1]) and re.search('C',sentence_p[2]):
            sentence ='第二文型'
            return sentence
        elif re.search('S',sentence_p[0]) and re.search('V',sentence_p[1]) and re.search('O',sentence_p[2]):
            sentence ='第三文型'
            return sentence
    elif len(sentence_p) == 4:
        if re.search('S',sentence_p[0]) and re.search('V',sentence_p[1]) and re.search('O',sentence_p[2]) and re.search('O',sentence_p[3]):
            sentence ='第四文型'
            return sentence
        elif re.search('S',sentence_p[0]) and re.search('V',sentence_p[1]) and re.search('O',sentence_p[2]) and re.search('C',sentence_p[3]):
            sentence ='第5文型'
            return sentence


#大量のテキストを分割して、単語ごとにわけ、品詞タグ付けを行う関数
def ie_preprocess(document):
    sentences =nltk.sent_tokenize(document)
    sentence = [nltk.word_tokenize(sent) for sent in sentences]
    sentences =[nltk.pos_tag(sent) for sent in sentences]

#チャンカの作成
grammer = r"""
   NP: {<DT|JJ|NN.*>+}
   PP: {<IN><NP>}
   VP: {<VB.*><NP|PP|CLAUSE>+$}
   CLAUSE: {<NP><VP>}
"""

f =open("test2.txt",'r')

input_text =input('文字を入力')
text =nltk.word_tokenize(str(input_text))
tag_text =nltk.pos_tag(text)
sentence =''
sentence =judgemnt(tag_text)
print('トークン化した文章:',nltk.pos_tag(text))
print('文型:',sentence)
