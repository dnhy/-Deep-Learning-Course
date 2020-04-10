import tensorflow.compat.v1 as tf
tf.disable_v2_behavior();
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.utils import shuffle

df=pd.read_csv("boston_house_prices.csv", header=0);

df=df.values;
#只取数值部分的值
df=np.array(df[1:,:],dtype=np.float64);
#数据归一化
for i in range(12):
    df[:,i]=df[:,i]/(df[:,i].max()-df[:,i].min());
#前12列特征数据
x_data=df[:,:12];
#为最后一列标签数据
y_data=df[:,12];
#print(x_data);
#print(y_data);
x=tf.placeholder(tf.float32,[None,12],name="X");#12列，行未定
y=tf.placeholder(tf.float32,[None,1],name="Y");#1列

#定义一个命名空间
with tf.name_scope("Model"):
        #对w进行初始化，为shape[12,1]的随机值
        w=tf.Variable(tf.random_normal([12,1],stddev=0.01),name="W");
        #b初始化值为1.0
        b=tf.Variable(1.0,name="b");
        #w和x是矩阵相乘
        def model(x,w,b):
            return tf.matmul(x,w)+b;
        pred=model(x,w,b);
#定义损失函数
with tf.name_scope("LossFunction"):
    loss_function=tf.reduce_mean(tf.pow(y-pred,2));#均方误差

#迭代轮次
train_epochs=100
#学习率
learning_rate=0.01

#创建梯度下降优化器
optimizer= tf.train.GradientDescentOptimizer(learning_rate).minimize(loss_function);
sess=tf.Session();
#定义变量初始化工作
init=tf.global_variables_initializer();
#设置日志存储目录
logdir='d:/log'
#创建一个操作，记录loss
sum_loss_op=tf.summary.scalar("loss",loss_function);
#把所有需要记录摘要日志文件合并
merged=tf.summary.merge_all();
sess.run(init);

#创建摘要writer，将计算图写入摘要文件
writer=tf.summary.FileWriter(logdir,sess.graph);

loss_list=[]#用于保存loss值的列表
for epoch in range(train_epochs):
    loss_sum=0.0;
    for xs,ys in zip(x_data,y_data):
        #数据取出来是shape=(12,),需要和placeholder的shape一致
        xs=xs.reshape(1,12);
        ys=np.array(ys);
        ys=ys.reshape(1,1);
        _,summary_str,loss=sess.run([optimizer,sum_loss_op,loss_function],feed_dict={x:xs,y:ys});
        
        writer.add_summary(summary_str,epoch);
        
        #计算本来loss值的和
        loss_sum=loss_sum+loss;
#打乱数据顺序
    xvaluses,yvaluses=shuffle(x_data, y_data);
    b0temp=b.eval(session=sess);
    w0temp=b.eval(session=sess);
    loss_average=loss_sum/len(y_data);
    
    loss_list.append(loss_average);
    plt.plot(loss_list);
    print("epo=",epoch+1,"loss=",loss_average,"b=",b0temp,"w=",w0temp);
n=np.random.randint(506);
print(n);
x_test=x_data[n];
x_test=x_test.reshape(1,12);
predict=sess.run(pred,feed_dict={x:x_test});
print("预测值：%f" %predict);
target=y_data[n];
print("标签值：%f"%target);
sess.close();