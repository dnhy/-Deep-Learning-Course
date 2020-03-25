# -*- coding: utf-8 -*-
import tensorflow as tf
import numpy as np
a=tf.constant([0,1,2]);
b=tf.constant([3,4,5]);
r=tf.add(a,b);
print(r);
tf.pow(2,3);
a=tf.constant([0,1,2]);
r=tf.square(a);#逐元素平方
print(r);
a=tf.constant([1.,4.,9.,16.]);
r=tf.sqrt(a);#逐元素求平方根（使用浮点数）
print(r);
r=tf.exp(1.);#e的指数
print(r);
r2=tf.math.log(r);#e的对数
print(r2);
#指数和对数都需要使用浮点数

#求非e为底需要使用换底公式

#重载运算符
a=tf.constant([0,1,2]);
b=2;
print(a%2);
#广播
a=tf.constant([1,2,3]);
b=tf.constant(np.arange(12).reshape(4,3));
print(a+b);

'''
a = tf.constant(np.arange(4),shape=(2,2))

b = tf.constant(np.arange(4),shape=(2,2))

c = a@b

d = tf.multiply(a,b)

print("c:",c.numpy())

print("d:",d.numpy())

a = tf.constant(np.arange(24).reshape(4,2,3))

b = tf.constant(np.arange(6).reshape(3,2))

c = a@b

print(c.shape)
'''
#张量乘法
#tf.multiply(),* 逐位乘法
#tf.matmul().@矩阵乘法
#多维向量 shape: [2,3,5]@[5,4]=[2,3,4]
#数据统计
#tf.reduce_sum(input_tensor,axis);#求和
#tf.reduce_mean(input_tensor,axis);#求平均值（创建张量最好是浮点数，或者使用tf.cast(a，tf.float32)转化）
#tf.reduce_max(input_tensor,axis);#求最大值
#tf.reduce_min(input_tensor,axis);#求最小值
#reduce为降维，运算的结果也是向量，它的维数小于原来的维数
#求最值得索引
#tf.argmax()
#tf.argmin()