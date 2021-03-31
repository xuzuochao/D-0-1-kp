# coding=utf-8
import matplotlib.pyplot as plt
import linecache

print("文件如下")
print("idkp1-10.txt\n""wdkp1-10.txt\n""udkp1-10.txt\n""sdkp1-10.txt")
tex=input("文件名称")
n=int(input("组号"))
m=n*8
s=n*8+2
profit=linecache.getline(tex,m)
list1 = profit.split(',')
weight=linecache.getline(tex,s)
list2 = weight.split(',')
list1.pop()
list2.pop()
print("profit=",list1)
print("weight=",list2)
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
