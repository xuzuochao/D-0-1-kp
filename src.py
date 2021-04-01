# coding=utf-8
import matplotlib.pyplot as plt
import linecache
import datetime
import numpy as np

print("文件如下")
print("idkp1-10.txt\n""wdkp1-10.txt\n""udkp1-10.txt\n""sdkp1-10.txt")
tex=input("文件名称")
n=int(input("组号"))
m=n*8
s=n*8+2
t=n*8-2
profit=linecache.getline(tex,m)
list1 = profit.split(',')
weight=linecache.getline(tex,s)
list2 = weight.split(',')
list1.pop()
list2.pop()
#print("profit=",list1)
#print("weight=",list2)

numb=linecache.getline(tex,t)


list3=[]
list4=[]
lit=[]
list3=[int(x) for x in list1]
list4=[int(i) for i in list2]

weight=list4 
profit=list3 
plt.figure(figsize=(10, 10), dpi=100)
plt.scatter(weight,profit)
plt.show()

for (a,b) in zip(list3,list4):
    num=a/b
    lit.append(num)
lit= [round(i,3) for i in lit]
#print(lit)
lit1=sorted(lit,reverse=True)


print("降序",lit1)
print("\n",numb)



starttime = datetime.datetime.now()


def bag_01(weights, values, capicity):
 
    n = len(values)
    f = [[0 for j in range(capicity+1)] for i in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, capicity+1):
            f[i][j] = f[i-1][j]
            if j >= weights[i-1] and f[i][j] < f[i-1][j-weights[i-1]] + values[i-1]:
                f[i][j] = f[i-1][j-weights[i-1]] + values[i-1]
    return f
 
def show(capicity, weights, f):
    n = len(weights)
    print("最大价值:", f[n][capicity])
    x = [False for i in range(n)]
    j = capicity
    for i in range(n, 0, -1):
        if f[i][j] > f[i-1][j]:
            x[i-1] = True
            j -= weights[i-1]
    print("背包中所装物品为:")
    for i in range(n):
        if x[i]:
            print("第{}个,".format(i+1),end='')
if __name__=='__main__':
  n=int(input("数量"))
  capicity=int(input("容量"))
  weights=list4
  values=list3
  m = bag_01(weights, values, capicity)
  show(capicity, weights, m)
endtime = datetime.datetime.now()
print ("\n\n\n\n                                运行时间",(endtime - starttime).seconds,"s")

