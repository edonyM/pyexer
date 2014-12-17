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
 # Last modified: 2014-12-17 20:28
 # 
 # Filename: r_p_s.py
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
import string 
def who_win(A, B):
    if(A == B):
        print 'Fair'

    if(A == 'r' and B == 's'):
        print pcolor.WARNING + 'First win' + pcolor.ENDC

    if(A == 'r' and B == 'p'):
        print pcolor.WARNING + 'Second win' + pcolor.ENDC

    if(A == 'p' and B == 'r'):
        print pcolor.WARNING + 'First win' + pcolor.ENDC

    if(A == 'p' and B == 's'):
        print pcolor.WARNING + 'Second win' + pcolor.ENDC

    if(A == 's' and B == 'r'):
        print pcolor.WARNING + 'Second win' + pcolor.ENDC

    if(A == 's' and B == 'p'):
        print pcolor.WARNING + 'First win' + pcolor.ENDC

fir = raw_input("r for Rock \np for Papr \ns for Scissor \nFirst one: ")
sec = raw_input("Second one: ")
q = "n"
tmp = ['r','p','s']
while q == 'n':
    if fir in tmp and sec in tmp:
        who_win(fir, sec)
    else:
        print 'wrong input'
    q = raw_input('"q" for quit "n" for going on : ')
    if q == 'n':
        fir = raw_input("r for Rock \np for Papr \ns for Scissor \nFirst one: ")
        sec = raw_input("Second one: ")
    else:
        break

