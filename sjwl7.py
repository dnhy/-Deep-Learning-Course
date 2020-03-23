# -*- coding: utf-8 -*-
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
#设置中文黑体
plt.rcParams['font.sans-serif']="SimHei";
#设置中文后修复坐标轴负号显示
plt.rcParams["axes.unicode_minus"]=False;
img=Image.open("lena.tiff");

img_r,img_g,img_b=img.split();

plt.subplot(221);
plt.axis("off");
img_small=img_r.resize((50,50));
plt.imshow(img_small,cmap="gray");#以灰度图像显示
plt.title("R-缩放",fontsize="14");

plt.subplot(222);
plt.axis("off");
img_g_f=img_g.transpose(Image.FLIP_LEFT_RIGHT);
img_g_f_x=img_g_f.transpose(Image.ROTATE_270);
plt.imshow(img_g_f_x,cmap="gray");
plt.title("G-镜像-旋转",fontsize="14");

plt.subplot(223);
plt.axis("off");
img_region=img_b.crop((0,0,150,150));
plt.imshow(img_region,cmap="gray");
plt.title("B-裁剪",fontsize="14");

img_rgb=Image.merge("RGB",(img_r,img_g,img_b));
plt.subplot(224);
plt.axis("off");
plt.imshow(img_rgb);
plt.title("RGB",fontsize="14");

plt.suptitle("图像基本操作",fontsize=20,color="blue");
img_rgb.save("test.png");
plt.show();
