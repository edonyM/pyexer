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
 # Last modified: 2015-01-09 15:06
 # 
 # Filename: pic_hdj_3.py
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
import matplotlib.pyplot as plt
import random as r
import math as m

z = np.linspace(1,8,num=50)
tmp = np.linspace(8,15,num=150)
for i in range(150):
    z = np.append(z,0.6*tmp[i])
tmp_2 = np.linspace(15,20,num=50)
for i in range(50):
    z = np.append(z,0.7*tmp_2[i])
for i in range(250):
    z[i] = -z[i]+21
tmp_3 = np.linspace(z[49],z[200],num=150)
print tmp_3.size
print z.size
for i in range(0,150):
    z[50+i]= tmp_3[i]
for i in range(250):
    z[i] = 10*z[i] + 1.5*r.random()

y = np.array(60*(np.ones(250)))
for i in range(250):
    if (i+1)%2==0:
        y[i] = y[i]+15+5*r.random()
    else:
        y[i] = y[i]-5*r.random()-15
    y[i] = y[i]*m.sin(i/m.pi)*0.2 + 70

theta = np.array(11*(np.ones(250)))
for i in range(250):
    neg_pos = r.randint(0,1)
    if neg_pos > 0:
        theta[i] = theta[i]+1.5*r.random()
    else:
        theta[i] = theta[i]-4.5*r.random()

file = open('out_3.txt','w')
for i in range(250):
    file.write('%f %f %f\n'%(z[i],y[i],theta[i]))
file.close()
plt.plot(range(250),z,'r',range(250),y,'b',range(250),theta,'g')
plt.show()
