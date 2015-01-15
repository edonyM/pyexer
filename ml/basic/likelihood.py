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
 # Last modified: 2015-01-15 14:20
 # 
 # Filename: likelihood.py
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
 
w = np.array([36.416,-0.0133])
x = np.array([1,1980])
w = np.matrix(w.T)
x = np.matrix(x.T)
sigma2 = 0.05
sigma = m.sqrt(sigma2)
mu = w*x.T
t = np.array(np.linspace(9.5,10.8,num=500))
rm = st.norm(mu,sigma)
p = rm.pdf(t)
p = p.reshape(500) # trans the 2D-array to 1D-array to plot
plt.plot(np.linspace(9.5,10.8,num=500),p,'b-',[9.95,9.95],[0,rm.pdf(9.95)],'--k',[10.1,10.1],[0,rm.pdf(10.1)],'--k',[10.25,10.25],[0,rm.pdf(10.25)],'--k')
plt.plot([9.4,9.95],[rm.pdf(9.95).reshape(1), rm.pdf(9.95).reshape(1)],'--k')
plt.plot([9.4,10.1],[rm.pdf(10.1).reshape(1),rm.pdf(10.1).reshape(1)],'--k')
plt.plot([9.4,10.25],[rm.pdf(10.25).reshape(1),rm.pdf(10.25).reshape(1)],'--k')
plt.text(9.95,0,'A')
plt.text(10.1,0,'B')
plt.text(10.25,0,'C')
plt.text(9.95,rm.pdf(9.95),'%f'%rm.pdf(9.95))
plt.text(10.1,rm.pdf(10.1),'%f'%rm.pdf(10.1))
plt.text(10.25,rm.pdf(10.25),'%f'%rm.pdf(10.25))
plt.axis([9.4,10.9,0,2])
plt.show()
