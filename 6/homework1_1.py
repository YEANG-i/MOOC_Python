def getText():
    with open("hamlet.txt", 'r') as txt:
        txt = txt.read()
        for ch in '!"#$%&()*+,-./:;<=>?@[\]^_‘{|}~':
            txt = txt.replace(ch, ' ')
            txt = txt.lower()
    return txt


# def getText():
#     txt = open("hamlet.txt", "r").read()
#     txt = txt.lower()
#     for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~':
#         txt = txt.replace(ch, " ")  # 将文本中特殊字符替换为空格
#     return txt


def main():
    hamlet = getText()
    words = hamlet.split()
    counts = {}
    for word in words:
        if counts.get(word):
            counts[word] += 1
        else:
            counts[word] = 1
        # counts[word] = counts.get(word, 0) + 1
    ls = list(counts.items())
    ls.sort(key=lambda x: x[1], reverse=True)
    for i in range(10):
        word, count = ls[i]
        print(word, count)


if __name__ == '__main__':
    main()
