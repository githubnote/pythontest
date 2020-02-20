import numpy as np
from itertools import permutations

def input_num():
    try:
        tmp = int(input())
        return tmp
    except:
        print("请重新输入.....")
        return input_num()


def find_24():
    print("请输入第1个数字:")
    a=input_num()


    print("请输入第2个数字:")
    b=input_num()
    print("请输入第3个数字:")
    c=input_num()
    print("请输入第4个数字:")
    d=input_num()






    list1 = [a, b, c, d]





    p = [c for c in permutations(list1, 4)]

    symbols = ["+", "-", "*", "/"]

    list2 = []  // 算出24的排列组合的列表

    flag = False

    for n in p:
        one, two, three, four = n
        for s1 in symbols:
            for s2 in symbols:
                for s3 in symbols:
                    if s1+s2+s3 == "+++" or s1+s2+s3 == "***":
                        express = ["{0} {1} {2} {3} {4} {5} {6}".format(
                            one, s1, two, s2, three, s3, four)] 
                    else:
                        express = ["(({0} {1} {2}) {3} {4}) {5} {6}".format(one, s1, two, s2, three, s3, four),
                                   "({0} {1} {2}) {3} ({4} {5} {6})".format(
                            one, s1, two, s2, three, s3, four),
                            "(({0} {1} ({2} {3} {4})) {5} {6})".format(
                            one, s1, two, s2, three, s3, four),
                            "{0} {1} (({2} {3} {4}) {5} {6})".format(
                            one, s1, two, s2, three, s3, four),
                            "{0} {1} ({2} {3} ({4} {5} {6}))".format(one, s1, two, s2, three, s3, four)]

                    for e in express:
                        try:
                            if abs(eval(e)-24) < 0.01:
                                list2.append(e+" = 24")
                                flag = True
                        except ZeroDivisionError:
                            pass

    list3 = set(list2)  // 去除重复项

    if flag == False:
        print("无法算出")
        print("继续......y/n?")

        if input() == "y":
            find_24()

    for c in list3:
        print(c)
        print()
    print("ok!")


if __name__ == "__main__":
    find_24()
