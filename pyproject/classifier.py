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
 # Last modified: 2015-04-10 20:51
 # 
 # Filename: classifier.py
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
from scipy.cluster.vq import vq,kmeans2
from r2mat import RIn

class classifier(RIn):
    '''
    classifier is cluster the readed in data by features
    '''
    def __init__(self,filename,centroid):
        RIn.__init__(self,filename)
        self.data = RIn.ls2float(self.MAT)
        self.centroid = int(centroid)

    def cluster(self):
        '''
        FUNCTION kmeans2 return two patameters:
        ... The first one is centroids of the clustering
        ... The second one is label of the dataset that flag the cluster
        This function takes the label and the dataset as patameters and divide the dataset
        into different sets by clustering center. Write them into different files.
        '''
        X = np.array(self.data)
        print(X[0])
        k = int(self.centroid)
        self.clus = kmeans2(X,k,iter=500,thresh=1e-10)
    
    def seq(self):
        '''
        This function takes the label and the dataset as patameters and divide the dataset
        into different sets by clustering center.
        '''
        label = zip(self.clus[1],self.data)
        self.seq = []
        for i in range(self.centroid):
            self.seq.append(list())
        for item in label:
            self.seq[item[0]].extend([item[1]])

    def rec(self):
        self.cluster()
        self.seq()
        for i in range(self.centroid):
            name = './Cache/'+str(i)+'extraSeqPoints.sp'
            File = open(name,'w')
            for line in self.seq[i]:
                File.write(str(line[0]) +
                        ' ' +
                        str(line[1]) +
                        ' ' +
                        str(line[2]) +
                        '\n')
            File.close()

if __name__ == '__main__':
    from time import clock
    start = clock()
    test = classifier('extraPoints.txt',4)
    print len(test.data)
    print type(test.data)
    test.rec()
    end = clock()
    print('taken time is: %f'%(end-start))

