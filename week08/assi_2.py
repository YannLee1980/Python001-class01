# 作业二：
# 自定义一个 python 函数，实现 map() 函数的功能。

#考虑接收函数可能会有多个参数的情况：
def mymap(func, *args):
    results = []
    arg_couplets = list(zip(*args))
    for arg_couplet in arg_couplets:
        results.append(func(*arg_couplet))
    return results

#测试函数：
def test1(a):
    return a**2

def test2(a, b):
    return a+b

def test3(a, b, c):
    return a+b+c
#测试：
print(mymap(test1, range(10)))
# 输出：[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(mymap(test2, range(10), range(10)))
# 输出：[0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print(mymap(test3, range(10), range(20), range(10)))
# 输出：[0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
