 #!/usr/bin/python
 #encoding: utf-8
 #        .---.         .-----------  
 #       /     \  __  /    ------    
 #      / /     \(  )/    -----   (`-')  _ _(`-')              <-. (`-')_            
 #     //////    '\/ `   ---      ( OO).-/( (OO ).->     .->      \( OO) )     .->   
 #    //// / //  :   : ---      (,------. \    .'_ (`-')----. ,--./ ,--/  ,--.'  ,-.
 #   // /   /  / `\/ '--         |  .---' '`'-..__)( OO).-. ' |   \ |  | (`-')'.'  /
 #  //          //..\\          (|  '--.  |  |  ' |( _) | | | |  . '|  |)(OO \    / 
 # ============UU====UU====      |  .--'  |  |  / : \|  |)| | |  |\    |  |  /   /) 
 #             '//||\\`          |  `---. |  '-'  /  '  '-' ' |  | \   |  `-/   /`  
 #               ''``            `------' `------'    `-----' `--'  `--'    `--'    
 # ########################################################################################################
 # 
 # Author: edony - edonyzpc@gmail.com                 
 # 
 # twitter : @edonyzpc                                
 # 
 # Last modified: 2015-01-14 21:51
 # 
 # Filename: genolymp.py
 # 
 # Description: All Rights Are Reserved                 
class pcolor:
    ''' This class is for colored print in the python interpreter!
    "py" call Addpy() function to add this class which is defined
    in the .vimrc for vim Editor.
    
    格式: \033[显示方式;前景色;背景色m
    说明:
    前景色            背景色           颜色
    ---------------------------------------
    30                40              黑色
    31                41              红色
    32                42              绿色
    33                43              黃色
    34                44              蓝色
    35                45              紫红色
    36                46              青蓝色
    37                47              白色
    显示方式           意义
    -------------------------
    0                终端默认设置
    1                高亮显示
    4                使用下划线
    5                闪烁
    7                反白显示
    8                不可见
    
    例子：
    \033[1;31;40m   <!--1-高亮显示 31-前景色红色  40-背景色黑色-->
    \033[0m         <!--采用终端默认设置，即取消颜色设置-->
    '''
    WARNING = '\033[0;37;41m'
    ENDC = '\033[0m'
    def disable(self):
        self.ENDC = ''
        self.WARNING = ''
 
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D as Ax3
from scipy import stats as st
import math as m
 
f = open("olympics.txt",'r')
x = np.array([])
t = np.array([])
for line in f.readlines():
    tmp = line.split()
    x = np.append(x,float(tmp[0]))
    t = np.append(t,float(tmp[1]))
f.close()
x = x.T
t = t.T

w = np.array([[36.4165],[-0.0133]])
X = np.concatenate(([np.ones(x.size)],[x]),axis=0)
X = np.matrix(X.T)
w = np.matrix(w)
mean_t = X*w
mean_t = np.array(mean_t)

noise_var = 0.05    # vary this to change the noise level
cov = noise_var*(X.T*X).I # covariability of parameter w
print cov
# For random samples from :math:`N(\mu, \sigma^2)`, use:
#         ``sigma * np.random.randn(...) + mu``
noisy_t = mean_t + np.random.randn(mean_t.shape[0],mean_t.shape[1])*m.sqrt(noise_var)


plt.plot(x,mean_t,'k',x,noisy_t,'b+')
for i in range(x.size):
    plt.plot([x[i],x[i]],[mean_t[i],noisy_t[i]],'r--')
plt.plot(x,t,'go')
plt.show()
