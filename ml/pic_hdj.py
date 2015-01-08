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
 # Last modified: 2015-01-08 15:04
 # 
 # Filename: pic_hdj.py
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
 
# x(0,280).y(0,220)
#
import random as r
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
 
# Initial the data of the olympics 100m time and its year
oly_data = open('pic_hdj.txt','r')
x = np.array([])
t = np.array([])
noise = 0.001
for line in oly_data.readlines():
    tmp = line.split('\t')
    x = np.append(x,int(tmp[0]))
    t = np.append(t,18*(float(tmp[1].replace('\r\n',''))))
    for i in range(7):
        if i < 5:
            r_tmp = 18*(float(tmp[1].replace('\r\n','')))+r.random()
        t = np.append(t,r_tmp-r.random()*2)
    noise +=0.0001
k_tail = 0
while k_tail< 9:
    t = np.append(t,173) + r.random()/50
    k_tail +=1
oly_data.close()

for ele in range(t.size):
    t[ele]=(-0.98*ele+100+t[ele])/2
    t[ele]=t[ele]-r.random()*2
    if ele %4 ==0 and ele !=0:
        t[ele] = t[ele]-1.5*r.random()
for kk_tmp in range(200,10):
    iiiii = kk_tmp
    jjjjj = kk_tmp+10
    for kk in range(iiiii,jjjjj):
        if kk < 60:
            t[kk]=t[kk]-r.random()-7
        else:
            t[kk]=t[kk]-r.random()-2
for qqq in range(10,30):
    t[qqq]=t[qqq]-r.random()-39.7
for qqq in range(30,60):
    t[qqq]=t[qqq]-r.random()-47.9
for aaa in range(60,90):
    t[aaa]=t[aaa]-r.random()-43.7
for zzz in range(90,120):
    t[zzz]=t[zzz]-r.random()-47.3
for sss in range(120,220):
    t[sss]=0.99*t[sss]-37+r.random()*1.5
for kkk in range(200,225):
    t[kkk] = 23+r.random()*1.9-17

    
new_t = np.array([])
for ele in t:
    new_t = 0.5*t-13
for ele in range(new_t.size):
    new_t[ele]=new_t[ele]+0.9*r.random()
for ele in range(new_t.size):
    new_t[ele]=new_t[ele]+r.random()+7

print new_t.shape

new_tt = np.array([])
kq = 0.1
for ele in t:
    new_tt = np.append(new_tt,13+r.random()*1.9+kq)
    kq +=0.02
print new_tt.shape

w_file = open('out_y.txt','r+')
k_counter = 0
for ele in t:
    w_file.write('%f %f %f'%(ele,new_t[k_counter],new_tt[k_counter]))
    w_file.write('\n')
    k_counter +=1
w_file.close()

plt.plot(range(225),t,'r-',range(225),new_t,'g:',range(225),new_tt,'b-')
plt.show()
