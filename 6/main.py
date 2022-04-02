from pyinstrument import Profiler

profiler = Profiler()
profiler.start()


# code you want to profile


def main():
    print("hello")


if __name__ == "__main__":
    main()

profiler.stop()
profiler.print()
