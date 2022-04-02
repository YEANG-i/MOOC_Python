def main():
    try:
        s = input()  # {"a": 1, "b": 2}
        d = eval(s)  # eval将字符串的引号去掉，这就变成了字典
        dict2 = {}
        for key in d:
            dict2[d[key]] = key
        print(dict2)
    except:
        print("输入错误")


if __name__ == "__main__":
    main()
