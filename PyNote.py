#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
 # ##########################################################################################
 # 
 # Author: edony - edonyzpc@gmail.com                 
 # 
 # twitter : @edonyzpc                                
 # 
 # Last modified: 2015-04-01 15:32
 # 
 # Filename: PyNote.py
 # 
 # Description: All Rights Are Reserved                 
class pcolor:
    ''' This class is for colored print in the python interpreter!
    "py" call Addpy() function to add this class which is defined
    in the .vimrc for vim Editor.
    
    STYLE: \033['display model';'foreground';'background'm
    DETAILS:
    FOREGROUND        BACKGOUND       COLOR
    ---------------------------------------
    30                40              black
    31                41              red
    32                42              green
    33                43              yellow
    34                44              blue
    35                45              purple
    36                46              cyan
    37                47              white
    DISPLAY MODEL    DETAILS
    -------------------------
    0                default
    1                highlight
    4                underline
    5                flicker
    7                reverse
    8                non-visiable
    
    e.g：
    \033[1;31;40m   <!--1-highlight;31-foreground red;40-background black-->
    \033[0m         <!--set all into default-->
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
 
 
def filter(ls):
    '''
    An efficient way to filter the repeat items in list
    '''
    tmp = set(ls)
    return list(tmp)

def pyIdiom_swap(a,b):
    '''
    Swap a and b
    '''
    a,b = b,a
    return a,b

def cache_mechanism():
    '''
    Reference and equal in Python Mechanism
    '''
    print('reference list ls_1 and ls_2')
    ls_1 = [1,2,3]
    ls_2 = ls_1
    print('ls_1 = [1,2,3]\nls_2 = ls_1)
    if(ls_1==ls_2):
        print('ls_1 and ls_2 have the same value, said "ls_1 == ls_2"')
    else:
        print('ls_1 and ls_2 have the different values, said "ls_1 != ls_2"')
    if(ls_2 is ls_1):
        print('ls_1 and ls_2 are referencing the same object')
    else:
        print('ls_1 and ls_2 are referencing the different objects')

    ls_1 = [1,2,3]
    ls_2 = [1,2,3]
    print('ls_1 = [1,2,3]\nls_2 = [1,2,3])
    if(ls_1==ls_2):
        print('ls_1 and ls_2 have the same value, said "ls_1 == ls_2"')
    else:
        print('ls_1 and ls_2 have the different values, said "ls_1 != ls_2"')
    if(ls_2 is ls_1):
        print('ls_1 and ls_2 are referencing the same object')
    else:
        print('ls_1 and ls_2 are referencing the different objects')

    print('Python cache little digits and strings')
    x = 34
    y = 34
    print('x = 34\ny = 34')
    if(x==y):
        print('x and y have the same value, said "x == y"')
    else:
        print('ls_1 and ls_2 have the different values, said "x != y"')
    if(x is y):
        print('x and y are referencing the same object')
    else:
        print('x and y are referencing the different objects')

def str2FilePath():
    '''
    when we read file from a file direction, we should make sure that the type casting can not work.
    '''
    path = r'/home/edony/code/py'
    #f = open(path+'test.bat')

def slice2str():
    """
    slicing the string that has many ways:
    ...s[0:4]<--str([s[0],s[1],s[2],s[3]])
    ...s[-3:-1]<--str(s[len(s)-3],...)
    ...s[0:10:2]<--take a stride with 2

    s[:-1] help to remove the last item in the string, especially '\n','\r'
    P.S.
        for text file removing whitespace, we are recommended to use str.rstrip()
    """
    pass

def list2str():
    '''
    way to do conversion about list and string in python
    '''
    s = 'spam'
    l = list(s)
    s_again = ''.join(l)

def format2str():
    '''
    string format control way
    '''
    print('\n%s is a %d number'%('edony',24))
    print('\n{0} is a {1} number'%{'edony',24})
    print('\n{0[spam]} is a {0[age]} numbers'%{'spam':'edony','age':24})

def readintomatrix():
    '''
    use python to read file into matrix
    '''
    import numpy as np
    X = []
    f = open('/home/shared/filename')
    row = 0
    tmp = f.readline().split()
    colum = len(tmp)
    for line in f.readlines():
        X.extend(tmp)
        row += 1
        tmp = line.split()
    X = np.array(X)
    X.reshape(row,colum)
    return X

def dictionary():
    '''
    dictionary is a hash
    '''
    D = {'edony':24,'cc':25,'murpht':34}
