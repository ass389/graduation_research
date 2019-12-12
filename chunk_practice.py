import nltk
import re
import pprint

with open("chuunk_result.txt",mode ='w') as w:
    f = open("test.txt")
    count =0
    for line in f:
        text =line
        text = nltk.word_tokenize(text) #文章を単語ごとに区切っている
        tag_text =nltk.pos_tag(text) #単語ごとにタグ付けをしている
        tag_text
        #チャンキングをするためのルール
        grammar = r"""
        NP: {<CD|PRP.|DT|JJ.?|NN.*>+}
        PP: {<IN><NP>}
        VP: {<VB.*><NP|PP|CLAUSE|VB.*>+$}
        CLAUSE: {<NP><VP>}
        """
        cp =nltk.RegexpParser(grammar,loop=2)
        result = cp.parse(tag_text)
        print(text)
        print(tag_text)
        print(count,result)
        w.write(str(count)+':'+str(result)+'\n')
        count+=1
    """
        PP: {<IN><NP>}
        VP: {<VB.*><NP|PP|CLAUSE>+$}
        CLAUSE: {<NP><VP>}
    """
w.close()
