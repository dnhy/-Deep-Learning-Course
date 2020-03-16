# -*- coding: utf-8 -*-
import numpy as np
x=np.array([64.3,99.6,145.45,63.75,135.46,92.85,86.97,144.76,59.3,116.03]);
y=np.array([62.55,82.42,132.62,73.31,131.05,86.57,85.49,127.44,55.25,104.84]);
xb=np.mean(x);
yb=np.mean(y);
result1=0;
result2=0;
w=0;
b=0;
for index in range(len(x)):
    result1+=(x[index]-xb)*(y[index]-yb);
    result2+=(x[index]-xb)*(x[index]-xb);
w=result1/result2;
print("W=",w);
b=yb-w*xb;
print("b=",b);