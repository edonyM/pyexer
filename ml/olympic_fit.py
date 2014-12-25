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
 # Last modified: 2014-12-24 21:19
 # 
 # Filename: olympic_fit.py
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
import scipy.optimize

def ls_func(p,x):
    return p[0] * x + p[1]

ls_err = lambda p,x,y:(y - ls_func(p,x))

x = np.array([1896,1900,1904,1906,1908,1912,1920,1924,1928,1932,1936,1948,1952,1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1996,2000,2004,2008])
y = np.array([12.00,11.00,11.00,11.20,10.80,10.80,10.80,10.60,10.80,10.30,10.30,10.30,10.40,10.50,10.20,10.00,9.95,10.14,10.06,10.25,9.99,9.92,9.96,9.84,9.87,9.85,9.69])
x_m = x[8:]
y_m = np.array([12.20,11.90,11.50,11.90,11.50,11.50,11.00,11.40,11.00,11.07,11.08,11.06,10.97,10.54,10.82,10.94,11.12,10.93,10.78])

out = sp.optimize.leastsq(ls_err,np.array([1.0,1.0]),args=(x,y),full_output=1)
out_m = sp.optimize.leastsq(ls_err,np.array([1.0,1.0]),args=(x_m,y_m),full_output=1)
p_res = out[0]
p_res_m = out_m[0]
print p_res
print p_res_m
plt.plot(x,y,'ro',x_m,y_m,'bx',np.arange(1890,2014,4),ls_func(p_res,np.arange(1890,2014,4)),'g',np.arange(1890,2014,4),ls_func(p_res_m,np.arange(1890,2014,4)),'y')

plt.axis([1890,2014,9.5,12.5])
plt.show()
