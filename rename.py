import os
source = "img/empty_200909/10/"


def main():
    num = 5000
    for count, filename in enumerate(os.listdir(source)):
        dst = "fl_" + str(num) + ".jpeg"
        src = source + filename
        dst = source + dst
        num+=1

        os.rename(src, dst)


if __name__ == '__main__':

    main() 