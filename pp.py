#! python3
# 计算1万以内所有素数之和

import math

primeList = []
for num in range(2, 10000):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            break
    else:
        primeList.append(num)
#print(primeList)

sum = 0
for i in primeList:
    sum += i
print('1万以内所有素数之和为：' + str(sum))

# 计算1万以内闰年
leapYearList = []
for year in range(1, 10000):
    if year % 100 == 0:
        if year % 400 == 0:
            leapYearList.append(year)
    elif year % 4 == 0:
        leapYearList.append(year)
print(leapYearList)

# 在x,y之间有m个自然数，和的取值范围在p到q之间，输出所有可能的合法排列。（大意）
# Initialization (数大了会卡死)
x = 1
y = 10
m = 5
p = 10
q = 20

numList = []
for i in range(x, y+1):
    numList.append(i)

import itertools
numList = list(itertools.combinations(numList, m))
# 元素个数为 m 的 numList 的子集

legitimateList = []
for i in numList:
    sum = 0
    for num in i:
        sum += num
    if sum >p and sum < q:
        legitimateList.append(i)
print(legitimateList)

# 大于7且小于100，000的正整数中能整除7，但又不能整除19和21的所有的数的和。
legitimateNum = []
for i in range(7, 100000):
    if (i % 7 == 0) and (i % 19 != 0) and (i % 21 != 0):
        legitimateNum.append(i)
#print(legitimateNum)

sum = 0
for i in legitimateNum:
    sum+=i
print(sum)


#输入1，则在第一行打印a，输入2，则在第一行打印a，第二行打印bb，以此类推，直至ZZ（52个）打印一个三角形出来
#要求对输入进行判断。
while 1:
    numOfLayers = input('请输入层数：\n> ')
    try:
        numOfLayers = int(numOfLayers)
        if numOfLayers >= 1 and numOfLayers <= 52:
            break
        else:
            print('请输入一个介于1和52之间的整数')
    except:
        print('请输入一个整数')

alphabet =['a','b','c','d','e','f','g','h','i','j','k','l','m',
           'n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
           'U', 'V', 'W', 'X', 'Y', 'Z']

for i in range(1, numOfLayers):
    print((numOfLayers-i)*' ' + (alphabet[i-1]+' ')*(i-1) + (alphabet[i-1]+' ') + (numOfLayers-i)*' ')


# 只能进行乘法运算
x = 2
m = 4
p = 16
#1. f1(m) = m!
def f1(m):
    fm = 1
    for i in range(1,m+1):
        fm *= i
    return fm
print(f1(4))

#2. f2(x,p) = x^p
def f2(x,p):
    fxp = 1
    for i in range(1,p+1):
        fxp *= x
    return fxp
print(f2(2,16))

#3. f3(x,m) = x + x^2/2!+ x^3/3! + x^4/4! + … + x^m/(m)!
def f3(x,m):
    sum = 0
    for i in range(1,m+1):
        sum += f2(x,i)/f1(i)
    return sum
print(f3(2,4))

#打印 n 个随机数中的奇数
import random
num = input('请输入个数：\n> ')
num = int(num)
numList = []
for i in range(num):
    numList.append(random.randint(1,100))

for i in numList:
    if i % 2 == 0:
        print(i)
