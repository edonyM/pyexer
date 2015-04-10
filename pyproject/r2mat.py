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
 # ######################################################################################
 # 
 # Author: edony - edonyzpc@gmail.com                 
 # 
 # twitter : @edonyzpc                                
 # 
 # Last modified: 2015-04-10 20:12
 # 
 # Filename: r2mat.py
 # 
 # Description: All Rights Are Reserved                 
class pcolor:
    ''' This class is for colored print in the python interpreter!
    "F2" call Addpy() function to add this class which is defined
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
 
class RIn:
    '''
    class RIn is a file reader that load the details in file into builtin type(list)
    '''
    def __init__(self,filename):
        self.filename = filename
        self.MAT = self.r2ls()

    def r2ls(self,filename=None):
        if filename==None:
            self.File = open(str(self.filename),'r')
        else:
            self.File = open(str(finename),'r')
        MAT = []
        for line in self.File.readlines():
            #line_tmp = lambda line.split():[eval(line.split()[0]),eval(line.split()[1]),eval(line.split()[2])]
            line2ls = line.split()
            MAT.extend([line2ls])
        self.File.close()
        return MAT

    @staticmethod
    def ls2float(MAT):
        #for x in MAT:
        #    x = [eval(x[0]),eval(x[1]),eval(x[2])]
        MAT = [[eval(item[0]),eval(item[1]),eval(item[2])] for item in MAT]
        return MAT
    @staticmethod
    def ind_ls2float(MAT):
        for item in MAT:
            row = MAT.index(item)
            MAT[row] = [eval(item[0]),eval(item[1]),eval(item[2])]
        return MAT


if __name__ == '__main__':
    from time import clock
    start = clock()
    test = RIn('extraPoints.txt')
    m = RIn.ls2float(test.MAT)
    end = clock()
    print m[0]
    print('read in time is: %f'%(end-start))
    print('matrix rows is: %d'%len(m))
    print('matrix colum is: %d'%len(m[0]))
    start1 = clock()
    test1 = RIn('extraPoints.txt')
    m1 = RIn.ind_ls2float(test1.MAT)
    end1 = clock()
    print('read in time is: %f'%(end1-start1))
