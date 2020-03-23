# -*- coding: utf-8 -*-
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

#设置中文黑体
plt.rcParams['font.sans-serif']="SimHei";
#设置中文后修复坐标轴负号显示
plt.rcParams["axes.unicode_minus"]=False;

mnist=tf.keras.datasets.mnist;
(train_x,train_y),(test_x,test_y)=mnist.load_data();

for i in range(16):
    num=np.random.randint(1,50000);
    plt.subplot(4,4,i+1);
    plt.axis("off");
    plt.title("标签值："+str(train_y[num]));
    plt.tight_layout(rect=[0,0,1,0.9]);
    plt.imshow(train_x[num], cmap="gray");
    plt.suptitle("MNIST测试集样本",fontsize="20",color="red");
    plt.show();

