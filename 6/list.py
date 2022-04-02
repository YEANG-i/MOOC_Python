from pyinstrument import Profiler

profiler = Profiler()
profiler.start()


# code you want to profile


def main():
    ls = ["yeang", 24, "man"]
    ls2 = [1, 25, 65454]
    print(ls)
    print(type(ls[0]))
    print(type(ls[1]))
    list1 = ls[::-1]
    print(list1)
    print(len(list1))
    print(min(ls2))
    ls.pop()
    print(ls)
    tp = (24, ls, 98)
    print(tp[1][1])
    ls.append(4)
    print(ls)
    ls[2] = 6
    print(ls)


if __name__ == "__main__":
    main()

profiler.stop()
profiler.print()
