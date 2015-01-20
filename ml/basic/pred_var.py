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
 # Last modified: 2015-01-19 19:56
 # 
 # Filename: pred_var.py
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
import random as r
import math as m
 
N = 100
tmpx = np.array(10*np.random.random(N)-5)
tmpx = np.sort(tmpx)
tmpt = 5*tmpx**3 - tmpx**2 + tmpx
noise_var = 300
tmpt = tmpt + np.random.randn(tmpx.shape[0])*m.sqrt(noise_var)

x = np.array([])
t = np.array([])
for pos in range(100):
    if tmpx[pos]>0 and tmpx[pos]<2:
        continue
    else:
        x = np.append(x,tmpx[pos])
        t = np.append(t,tmpt[pos])
t = np.matrix(t)
t = t.T

# Visualize the variability of testx with w respectively
testx = np.arange(-5.0,5.0,0.1)
plotcounter = 1
for i in range(1,9):
    X = np.array([np.ones(x.shape)])
    testX = np.array([np.ones(testx.shape)])
    for k in range(1,i+1):
        X = np.concatenate((X,[x**k]),axis=0)
        testX = np.concatenate((testX,[testx**k]),axis=0)
    X = np.matrix(X.T)
    testX = np.matrix(testX.T)
    w = (X.T*X).I*X.T*t
    sigma2 = np.array((1.0/N)*(t.T*t - t.T*X*w))
    testmean = testX*w
    sigma2 = sigma2.flatten()
    # calculate the variability of testx
    # `testX*(X.T*X).I*testX.T)` is the covariability of the testX
    # the diagonal of this matrix is the variability of the testx
    # the proving of this equation details are on the page59
    # the equation 'covar = sigma2*(testX*(X.T*X).I*testX.T)'
    # calculate the covariance and the diagnoal of the return matrix is the variability of each element
    # testvar is the variablity of each element
    testvar = sigma2*np.diagonal(np.array(testX*(X.T*X).I*testX.T))
    if (i%2)!=0:
        fig = plt.figure(plotcounter)
        ax1 = plt.subplot(2,1,1)
        ax1.plot(x,np.array(t),'k.',ms=8)
        y = np.array(testmean)
        y = y.flatten()
        ax1.errorbar(testx,y,yerr=testvar,elinewidth=0.5,errorevery=1,ecolor='k')
        ax1.set_xlabel("%i"%i)
    else:
        ax2 = plt.subplot(2,1,2)
        ax2.plot(x,np.array(t),'k.',ms=8)
        y = np.array(testmean)
        y = y.flatten()
        ax2.errorbar(testx,y,yerr=testvar,elinewidth=0.5,errorevery=1,ecolor='k')
        ax2.set_xlabel("%i"%i)
        plotcounter +=1
        fig.savefig("pred variability degree: %i and %i"%(i-1,i))

# Visualize each predicted equation
for i in range(1,9):
    X = np.array([np.ones(x.shape)])
    testX = np.array([np.ones(testx.shape)])
    for k in range(1,i+1):
        X = np.concatenate((X,[x**k]),axis=0)
        testX = np.concatenate((testX,[testx**k]),axis=0)
    X = np.matrix(X.T)
    testX = np.matrix(testX.T)
    w = (X.T*X).I*X.T*t
    sigma2 = np.array((1.0/N)*(t.T*t - t.T*X*w))
    sigma2 = sigma2.flatten()
    cov = sigma2*np.array((X.T*X).I)
    # calculate some samples value of w
    w_tmp = np.tile(w,10)
    w_sample = w_tmp + np.linalg.cholesky(cov)*np.matrix(sp.random.randn(w.shape[0],10))
    testw = testX*w_sample
    px = np.array(testx)
    fig = plt.figure(i+4)
    ax = plt.subplot(1,1,1)
    ax.plot(x,np.array(t),'ko')
    xt = np.arange(-6,6,0.1)
    ax.plot(xt,5*xt**3-xt**2+xt,'k-')
    for j in range(testw.shape[1]):
        py = np.array(testw[:,j])
        ax.plot(px,py,'k:')
    plt.axis([-1,1,-20,20])
    plt.title("Degree of the prediction: %i"%i)
    fig.savefig("w distribution degress: %i"%i)
plt.show()
