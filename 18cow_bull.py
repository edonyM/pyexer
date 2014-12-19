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
 # Last modified: 2014-12-19 19:54
 # 
 # Filename: 18cow_bull.py
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
 
import random
def rand_num():
    return random.randint(1000,9999)

def right_dig(num, ran):
    counter = 0
    tmp = int(num)
    test = int(ran)
    for i in range(4):
        if (tmp % 10) == (test % 10):
            counter += 1
            tmp = tmp / 10
            test = test / 10
        else:
            tmp = tmp / 10
            test = test / 10

    return counter

def wrong_dig(num, ran):
    counter = 0
    n1 = num
    n2 = ran
    tmp = []
    test = []
    for i in range(4):
        tmp.append(n1 % 10)
        n1 = n1 / 10
        test.append(n2 % 10)
        n2 = n2 / 10

    for i in range(4):
        if tmp[i] != test[i] and tmp[i] in test:
            counter += 1

    return counter
    
if __name__ == '__main__':
    ran = rand_num()
    num = input("Welcom to the Cows and Bulls Game!\nEnter a four digits number:\n>>> ")
    counter_of_lose = 0
    while True:
        cows = right_dig(num,ran)
        bulls = wrong_dig(num,ran)
        print "%d cow, %d bull" % (cows, bulls)
        if cows == 4 or counter_of_lose == 10:
            if counter_of_lose == 10:
                print pcolor.WARNING + "You lose!" + pcolor.ENDC
            print pcolor.WARNING + "The key is ",
            print ran,
            print pcolor.ENDC
            break
        num = input(">>> ")
        counter_of_lose += 1
