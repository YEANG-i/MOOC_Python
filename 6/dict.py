import jieba

d = {"China": "Beijing",
     "American": "Washtom"}
print(d.get("China"))
print(d)
print(d.pop("China"))
print(d)
str1 = "中国是一个伟大的国家"
str2 = jieba.lcut(str1)
print(str2)
