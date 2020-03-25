# -*- coding: utf-8 -*-
import tensorflow as tf
a=tf.constant([64.3,99.6,145.45,63.75,135.46,92.85,86.97,144.76,59.3,116.03]);
b=tf.constant([62.55,82.42,132.62,73.31,131.05,86.57,85.49,127.44,55.25,104.84]);

nt=tf.cast(tf.shape(a),tf.float32);
n=nt[0];

part1=tf.reduce_sum(a*b);
part2=up=tf.reduce_sum(a)*tf.reduce_sum(b);
part3=tf.reduce_sum(a*a);
part4=tf.pow(tf.reduce_sum(a),2);
w=(part1-part2)/(part3-part4);

part5=tf.reduce_sum(b);
part6=w*tf.reduce_sum(a);

b=(part5-part6)/n;
print(w);
print(b);