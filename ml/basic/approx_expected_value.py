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
 # Last modified: 2015-01-13 21:16
 # 
 # Filename: approx_expected_value.py
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
import mpl_toolkits.mplot3d as axes3d
import random as r

z_10 = np.array(np.zeros(10))
z_100 = np.array(np.zeros(100))
z_1000 = np.array(np.zeros(1000))
z_10000 = np.array(np.zeros(10000))

for i in range(10):
    z_10[i] = r.random()
for i in range(100):
    z_100[i] = r.random()
for i in range(1000):
    z_1000[i] = r.random()
for i in range(10000):
    z_10000[i] = r.random()

aver1 = np.mean(z_10**2)
aver2 = np.mean(z_100**2)
aver3 = np.mean(z_1000**2)
aver4 = np.mean(z_10000**2)

print aver1
print aver2
print aver3
print aver4

plt.plot(range(10000),np.array(np.ones(10000)/3.0),'r-',range(10),z_10,'ro',range(100),z_100,'b--',range(1000),z_1000,'g:',range(10000),z_10000,'b^')
plt.show()
