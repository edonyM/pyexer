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
 # Last modified: 2015-03-22 16:10
 # 
 # Filename: kmeans.py
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
import math as m
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D as Ax3
from scipy import stats as st
from matplotlib import cm
 

from scipy.cluster.vq import vq, whiten, kmeans, kmeans2
from scipy import io
import ReadCPInTxt as r

#file = io.loadmat('/home/shared/ex7data2.mat')
#examples = file['X']
#whitened = whiten(examples)
#for i in range(20):
#    tmp = kmeans2(examples,3,iter=500,thresh=1e-10)

#plt.plot(examples[:,0],examples[:,1],'ro')
#plt.plot(tmp[0][:,0],tmp[0][:,1],'^g')
#plt.show()

path = raw_input('File Name: ')
X = r.ReadCPInTxt(path)
for i in range(20):
    results = kmeans2(X,1,iter=500,thresh=1e-10)
tmp = results[0]
print tmp[0,0]
print tmp[0,1]
print tmp[0,2]
fig = plt.figure()
ax = fig.gca(projection='3d')
px = np.array([X[:,0]])
py = np.array([X[:,1]])
pz = np.array([X[:,2]])
print px.shape
ax.scatter(px,py,pz,c='r',marker='+')
ax.scatter(tmp[0,0],tmp[0,1],tmp[0,2],s=200,c='g',marker='^')
plt.show()
