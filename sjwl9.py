# -*- coding: utf-8 -*-
import tensorflow as tf
a=tf.constant([64.3,99.6,145.45,63.75,135.46,92.85,86.97,144.76,59.3,116.03]);
b=tf.constant([62.55,82.42,132.62,73.31,131.05,86.57,85.49,127.44,55.25,104.84]);
ap=tf.reduce_mean(a,0);
bp=tf.reduce_mean(b,0);

apc=a-ap;
bpc=b-bp;

up=tf.reduce_sum(apc*bpc);
down=tf.reduce_sum(apc*apc);

w=up/down;
b=bp-w*ap;

print(w);
print(b);


