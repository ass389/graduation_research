import nltk
iinput_text =input("文字を入力してください。")
text =nltk.word_tokenize(str(iinput_text))
print(nltk.pos_tag(text))
