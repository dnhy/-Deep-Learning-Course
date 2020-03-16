import numpy as np
np.random.seed(612);
a=np.random.rand(1000);
b=int(input("请输入一个1-100之间的整数："));
count=0;
print("序号\t索引值\t随机数");
for index in range(len(a)):
   if(index%b==0):
       count+=1;
       print(count,"\t",index,"\t",a[index]);
    
