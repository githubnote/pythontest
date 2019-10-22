import ctypes


import multiprocessing


def test():
    arr=[]
    for i in range(10):
        arr.append(i)

    return arr,i

if __name__ == "__main__":
    t,tt=test()

    adrss = t[1]+tt

    print(adrss)

    print(id(adrss))
    print("next")
    get_value = ctypes.cast(id(adrss), ctypes.py_object).value

    print(get_value)
