# -*- coding: utf-8 -*-
import tensorflow as tf
a=tf.range(24);
#变换维度
b=tf.reshape(a,[2,3,4]);#[4,-1]表示维度自动计算
#print(a);
#print(b);
#增加和删除维度(改变张量的视图，不改变张量的存储)
#tf.expand_dims(input,axis);
#tf.squeeze(input,axis);只能删除长度为1的维度
a=tf.range(24);
b=tf.reshape(a,[1,4,1,6]);
print(tf.shape(b));
print(tf.shape(tf.squeeze(b)));
print(tf.shape(b));
print(tf.shape(tf.squeeze(b,[0,2])));
#交换维度,perm为交换的轴的顺序（改变存储和视图）
x=tf.constant([[1,2,3],[4,5,6]]);
print(x);
print(tf.transpose(x));
print(tf.transpose(x,perm=[0,1]));
#拼接(不产生新的维度)
#tf.concat(tensors,axis);
t1=[[1,2,3],[4,5,6]];
t2=[[7,8,9],[10,11,12]];
tr=tf.concat([t1,t2],0);
print("拼接");
print(tr);
tr=tf.concat([t1,t2],1);
print(tr);
#分割
#tr.split(value,num_or_size_splits,axis=0);
#堆叠(产生新的维度)
x=tf.constant([1,2,3]);
y=tf.constant([4,5,6]);
b=tf.concat((x,y),0);
print("堆叠")
print(b);
a=tf.stack((x,y),0);
print(a);
a=tf.stack((x,y),1);
print(a);
#分解
c=tf.constant([[1,2,3],[4,5,6]]);
a,b=tf.unstack(c,axis=0);
print(a);
print(b);
#表示在0维度添加数据，使得维度增加一维
#np.expand_dims(a, axis=0)

t1 = tf.constant([[[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8]],

            [[ 9, 10, 11],[12, 13, 14],[15, 16, 17]]])

t2 = tf.expand_dims(t1, -4)
print(t2.shape)

#索引和切片
#a[1][1][1]
#a[1,1,1]
#a[m:n:k]
#起始位置：结束位置：步长
#[a,b)
a=tf.range(5);
print(a[3:0:-1]);

#部分采样
a=tf.range(5);
a=tf.gather(a,indices=[0,2,3]);#一次只对一个维度索引
print(a);
b=tf.constant([[1,2,3],[4,5,6]]);
b=tf.gather_nd(b,[[0,0],[1,1]]);#同时采样多个点
print(b);