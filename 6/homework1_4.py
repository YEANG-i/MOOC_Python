import jieba

with open('沉默的羔羊.txt', 'r', encoding='utf-8') as fd:
    txt = fd.read()
    txt = jieba.lcut(txt)
    words = {}
    for word in txt:
        if len(word) >= 2:
            words[word] = words.get(word, 0) + 1
    ls = list(words.items())
    ls.sort(key=lambda x: x[1], reverse=True)
    print(ls[0][0])
