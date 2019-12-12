import nltk
import re
import pprint
from nltk import Tree

#チャンキングできるように改良

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
    #第二語の場合
    if re.search('DT|TO|PRP.?|CD',text[0][1]) and re.search('JJ|NN.?',text[1][1]):
        sentence_p.append('S')

        if re.search('VB.?',text[2][1]):
            sentence_p.append('V')
            if re.search('JJ.?',text[3][1]):
                sentence_p.append('C')
            elif re.search('VBG',text[3][1]) and len(text)==4:
                sentence_p.append('C')
            elif re.search('RB|DT|TO',text[3][1]) and re.search('JJ|NN|VB',text[4][1]):
                sentence_p.append('C')
        #第三文型
            elif re.search('NN.?|PRP.?|VBG',text[3][1]):
                sentence_p.append('O')
                #第四文型
                if re.search('NN.?',text[4][1]):
                    sentence_p.append('O')
            #第五文型
                elif re.search('JJ.?|VB.?',text[4][1]):
                    sentence_p.append('C')
        elif re.search('MD|VB.?',text[2][1]) and re.search('VB.?',text[3][1]):
            sentence_p.append('V')
            if re.search('JJ.?',text[4][1]):
                sentence_p.append('C')
            elif re.search('VBG',text[4][1]) and len(text)==5:
                sentence_p.append('C')
        #第三文型
            elif re.search('NN.?|PRP.?|VBG',text[4][1]) and re.search('NN',text[5][1]):
                sentence_p.append('O')
                #第四文型
                if re.search('NN?',text[6][1]):
                    sentence_p.append('O')
            #第五文型
                elif re.search('JJ.|NNP',text[6][1]):
                    sentence_p.append('C')
        #Oの判定第二語
            elif re.search('NN.?|PRP.?|VBG',text[4][1]):
                sentence_p.append('O')
                #第四文型
                if re.search('NN.?',text[5][1]):
                    sentence_p.append('O')
            #第五文型
                elif re.search('JJ.?',text[5][1]):
                    sentence_p.append('C')
    #S第一語の場合
    elif re.search('(NN.?|PRP|DT|EX)',text[0][1]):
        sentence_p.append('S')
        #第二文型
        if re.search('VB.?',text[1][1]):
            sentence_p.append('V')
            if re.search('JJ.?',text[2][1]):
                sentence_p.append('C')
            elif re.search('VBG',text[2][1]) and len(text)==3:
                sentence_p.append('C')
        #Oの判定 第二語
            elif re.search('NN.?|PRP.?|VBG',text[2][1])and re.search('NN',text[3][1]):
                sentence_p.append('O')
                #第四文型
                if re.search('NN|DT?',text[4][1])and re.search('NN.?',text[5][1]):
                    sentence_p.append('O')
            #第五文型
                elif re.search('JJ.|NN.?',text[4][1]):
                    sentence_p.append('C')
                #第四文型
                if re.search('NN',text[4][1]):
                    sentence_p.append('O')
            #第五文型
                elif re.search('JJ.|NN.?',text[4][1]):
                    sentence_p.append('C')
            #Oの判定
            elif re.search('NN.?|PRP.?|VBG',text[2][1]):
                sentence_p.append('O')
                #第四文型
                if re.search('NNS',text[3][1]):
                    sentence_p.append('O')
            #第五文型
                elif re.search('JJ.|NN.?',text[3][1]):
                    sentence_p.append('C')
        elif re.search('MD|VB.?',text[1][1]) and re.search('VB.?',text[2][1]):
            sentence_p.append('V')
            #第二文型
            if re.search('JJ.?',text[3][1]):
                sentence_p.append('C')
            elif re.search('VBG',text[3][1]) and len(text)==4:
                sentence_p.append('C')
        #第三文型
            elif re.search('NN.?|PRP.?|VBG',text[3][1]):
                sentence_p.append('O')
                #第四文型
                if re.search('NN.?',text[4][1]):
                    sentence_p.append('O')
            #第五文型
                elif re.search('JJ.?',text[4][1]):
                    sentence_p.append('C')
             #第三文型
            elif re.search('NN.?|PRP.?|VBG',text[3][1]):
                sentence_p.append('O')
                #第四文型
                if re.search('NN.?',text[4][1]):
                    sentence_p.append('O')
            #第五文型
                elif re.search('JJ.?|VB.?',text[4][1]):
                    sentence_p.append('C')

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
            sentence ='第五文型'
            return sentence


#大量のテキストを分割して、単語ごとにわけ、品詞タグ付けを行う関数
def ie_preprocess(document):
    sentences =nltk.sent_tokenize(document)
    sentence = [nltk.word_tokenize(sent) for sent in sentences]
    sentences =[nltk.pos_tag(sent) for sent in sentences]


with open('picture_judge_result.txt',mode ='w') as w:
    f =open("picture_book_test.txt",'r')
    for line in f:
        input_text =line
        text =nltk.word_tokenize(str(input_text))
        tag_text =nltk.pos_tag(text)
        sentence =''
        # cp =nltk.RegexpParser(grammar,loop=2)
        # result = cp.parse(tag_text)
        # t =nltk.Tree.fromstring(str(result))
        sentence =judgemnt(tag_text)
        print('トークン化した文章:',nltk.pos_tag(text))
        print('文型:',sentence)
        # print(sentence)
        w.write(str(nltk.pos_tag(text))+'\n')
        w.write('文型:'+str(sentence)+'\n')

w.close()
