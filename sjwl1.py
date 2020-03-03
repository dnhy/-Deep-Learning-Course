# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 17:52:31 2020

@author: dnhy
"""

'''
Todo:ax*x+bx+c=0
'''
a=int(input("a="));
b=int(input("b="));
c=int(input("c="));

test=b*b-4*a*c
if(test>=0):
    print("方程有解！");
    x1=(-b+test**0.5)/2*a;
    x2=(-b-test**0.5)/2*a;
    print("方程的两个根分别为：x1=%f，x2=%f"%(x1,x2));
else:
    print("方程无解！");