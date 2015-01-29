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
 # Last modified: 2015-01-29 16:21
 # 
 # Filename: plotData.py
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
from mpl_toolkits.mplot3d.axes3d import Axes3D as Ax3
from scipy import stats as st
from matplotlib import cm
 
def plotData(x,y):
    x = np.array(x.flatten())
    y = np.array(y.flatten())
    x = x.reshape(x.size)
    y = y.reshape(y.size)
    fig = plt.figure(1)
    plt.plot(x,y,'rx',ms=4)
    plt.show()

def plot3d(x,y,J):
#    x = np.array(x.flatten())
#    y = np.array(y.flatten())
#    x = x.reshape(x.size)
#    y = y.reshape(y.size)
    fig = plt.figure(2)
    ax = Ax3(fig)
    ax.plot_surface(x,y,J,rstride=5,cstride=5,cmap=cm.summer_r)
    plt.show()

def plotcontour(x,y,J,theta):
    x = np.array(x.flatten())
    y = np.array(y.flatten())
    x = x.reshape(x.size)
    y = y.reshape(y.size)
    fig = plt.figure(3)
    plt.contour(x,y,J)
    xp = np.array(theta[0,0])
    yp = np.array(theta[1,0])
    plt.plot(xp,yp,'rx',ms=8)
    plt.show()
