import nltk
import re



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
        if re.search('VB|VB.',text[1][1]):
            sentence_p.append('V')
            if re.search('NN|JJ',text[2][1]):
                sentence_p.append('C')
            elif re.search('NN.|',text[2][1]):
                sentence_p.append('O')

    #2語の場合
    elif re.search('(PRP$|DT)',text[0][1])and re.search('(NN.|JJ.)',text[1][1]):
        sentence_p.append('S')
        if re.search('VB|VB.',text[2][1]):
            sentence_p.append('V')
    elif re.search('To',text[0][1])and re.search('VB|VB.',text[1][1]):
        sentence_p.append('S')
        if re.search('VB|VB.',text[2][1]):
            sentence_p.append('V')
            if re.search('NN.|JJ',text[3][1]):
                sentence_p.append('C')
            elif re.search('NN|PRP',text[3][1]):
                sentence_p.append('O')
    elif re.search('(VG|VN)',text[0][1])and re.search('(NN|NNP)',text[1][1]):
        sentence_p.append('S')
        if re.search('VB|VB.',text[2][1]):
            sentence_p.append('V')

    #主語が3語以上の場合
    #第一文型の出力
    if len(sentence_p)>=2:
        if re.search('S',sentence_p[0]) and re.search('V',sentence_p[1]):
            sentence ='第一文型'
            return sentence
        elif re.search('S',sentence_p[0]) and re.search('V',sentence_p[1]) and re.search('C',sentence_p[2]):
            sentence ='第二文型'
            return sentence
        elif re.search('S',sentence_p[0]) and re.search('V',sentence_p[1]) and re.search('O',sentence_p[2]):
            sentence ='第三文型'
            return sentence
        elif re.search('S',sentence_p[0]) and re.search('V',sentence_p[1]) and re.search('O',sentence_p[2]) and re.search('O',sentence_p[3]):
            sentence ='第四文型'
            return sentence
        elif re.search('S',sentence_p[0]) and re.search('V',sentence_p[1]) and re.search('O',sentence_p[2]) and re.search('C',sentence_p[3]):
            sentence ='第5文型'
            return sentence



f =open("test.txt",'r')
grammar =r"""
   NP: {<DT|JJ|NN.*>+}
   PP: {}
   VP:
   CLAUSE:
"""
for line in f:
    input_text =line
    text =nltk.word_tokenize(str(input_text))
    print(text)
    tag_text =nltk.pos_tag(text)
    sentence =''
    sentence =judgemnt(tag_text)
    print('トークン化した文章:',nltk.pos_tag(text))
    print('文型:',sentence)
