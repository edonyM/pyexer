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
 # Last modified: 2015-01-16 21:34
 # 
 # Filename: olymplike.py
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
x = x-x[0]
x = x/4.0

X1 = np.concatenate((np.array([np.ones(x.size)]),[x]),axis=0)
X2 = np.concatenate((X1,[x**2]),axis=0)
X3 = np.concatenate((X2,[x**3]),axis=0)
X4 = np.concatenate((X3,[x**4]),axis=0)
X5 = np.concatenate((X4,[x**5]),axis=0)
X6 = np.concatenate((X5,[x**6]),axis=0)
X7 = np.concatenate((X6,[x**8]),axis=0)
X8 = np.concatenate((X7,[x**9]),axis=0)
X9 = np.concatenate((X8,[x**10]),axis=0)
X1 = np.matrix(X1.T)
X2 = np.matrix(X2.T)
X3 = np.matrix(X3.T)
X4 = np.matrix(X4.T)
X5 = np.matrix(X5.T)
X6 = np.matrix(X6.T)
X7 = np.matrix(X7.T)
X8 = np.matrix(X8.T)
X9 = np.matrix(X9.T)
T = np.matrix(t.reshape(t.size,1))
sigma2 = np.array(np.zeros(10))
sigma2[0] = (1/float(t.size))*(T.T*T-T.T*X1*(X1.T*X1).I*X1.T*T)
sigma2[1] = (1/float(t.size))*(T.T*T-T.T*X2*(X2.T*X2).I*X2.T*T)
sigma2[2] = (1/float(t.size))*(T.T*T-T.T*X3*(X3.T*X3).I*X3.T*T)
sigma2[3] = (1/float(t.size))*(T.T*T-T.T*X4*(X4.T*X4).I*X4.T*T)
sigma2[4] = (1/float(t.size))*(T.T*T-T.T*X5*(X5.T*X5).I*X5.T*T)
sigma2[5] = (1/float(t.size))*(T.T*T-T.T*X6*(X6.T*X6).I*X6.T*T)
sigma2[6] = (1/float(t.size))*(T.T*T-T.T*X7*(X7.T*X7).I*X7.T*T)
sigma2[7] = (1/float(t.size))*(T.T*T-T.T*X8*(X8.T*X8).I*X8.T*T)
sigma2[8] = (1/float(t.size))*(T.T*T-T.T*X9*(X9.T*X9).I*X9.T*T)

N = float(t.size)
print sigma2.shape
logL = np.empty(9)
for i in range(9):
    logL[i] = -(N/2)*m.log(2*m.pi)-N/2-(N/2)*m.log(sigma2[i])

plt.plot(range(9),logL,'k-')
plt.show()
