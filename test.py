import os
import random




def bubble_sort3(ary):
	n = len(ary)
	k = n    #k为循环的范围，初始值n
	for i in range(n):
		flag = True
		for j in range(1, k):    #只遍历到最后交换的位置即可
			if ary[j-1] > ary[j]:
				ary[j-1], ary[j] = ary[j], ary[j-1]
				k = j     #记录最后交换的位置
				flag = False
		if flag:
			break
	return ary

if __name__ == "__main__":
    arr=[]

    for i in range(101):
        arr.append(random.random())

    os.system("pause")
    for i in arr:
        print(i)
    os.system("pause")
    arr_end=bubble_sort3(arr)
    os.system("pause")
    for i in arr_end:
        print(i)