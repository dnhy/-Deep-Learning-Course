# -*- coding: utf-8 -*-
import tensorflow as tf
import matplotlib.pyplot as plt
#设置中文黑体
plt.rcParams['font.sans-serif']="SimHei";
#设置中文后修复坐标轴负号显示
plt.rcParams["axes.unicode_minus"]=False;
boston_housing=tf.keras.datasets.boston_housing;
(train_x,train_y),(test_x,test_y)=boston_housing.load_data();
(train_x,train_y),(test_x,test_y)=boston_housing.load_data(test_split=0);


titles=["CRIM","ZN","INDUS","CHAS","NOX","RM","AGE","DIS","RAD","TAX","PTRATIO","B-1000","LSTAT"];
plt.figure(figsize=(12,12));
for i in range(13):
    plt.subplot(4,4,(i+1));
    plt.scatter(train_x[:,i], train_y);
    plt.xlabel(titles[i]);
    plt.ylabel("Price($1000's)");
    plt.title(str(i+1)+"."+titles[i]+"- Price");
    
plt.tight_layout();
plt.suptitle("各个属性和房价的关系",x=0.5,y=1.02,fontsize=20);
plt.show();
for i in range(len(titles)):
    print(i+1,"--","".join(titles[i:i+1]));
choose=int(input("请选择属性："));
for i in range(13):
    if(i==choose):
        plt.scatter(train_x[:,i-1], train_y);
        plt.xlabel(titles[i-1]);
        plt.ylabel("Price($1000's)");
        plt.title(str(i)+"."+titles[i-1]+"- Price");


