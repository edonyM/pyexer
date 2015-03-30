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
    u''' This class is for colored print in the python interpreter!
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
import sequence as se

#file = io.loadmat('/home/shared/ex7data2.mat')
#examples = file['X']
#whitened = whiten(examples)
#for i in range(20):
#    tmp = kmeans2(examples,3,iter=500,thresh=1e-10)

#plt.plot(examples[:,0],examples[:,1],'ro')
#plt.plot(tmp[0][:,0],tmp[0][:,1],'^g')
#plt.show()

def classifier(path):
    '''
    Function classifier use k-means algorithm to cluster Cloud Points into about 4 sets.
    The parameter path is the CPs file path(or file name).
    It return a list that includes two elements.
    ...The first one is the ID of each CP which is closest to which centroid.
    ...The second one include the centroids.
    '''
    # ------ Read in the CP file
    #path = raw_input('File Name: ')
    X = r.ReadCPInTxt(path)
    
    # ------ Cluster the CP
    #for i in range(20):
    results = kmeans2(X,4,iter=500,thresh=1e-10)
    tmp = results[0]
    label = results[1]
    print 'the center of the clustering sets...'
    print tmp
    # ------ Visualization the clustering
    #fig = plt.figure(1)
    #ax = fig.gca(projection='3d')
    #px = np.array([X[:,0]])
    #py = np.array([X[:,1]])
    #pz = np.array([X[:,2]])
    #ax.scatter(px,py,pz,c='r',marker='.')
    #ax.scatter(tmp[0,0],tmp[0,1],tmp[0,2],s=200,c='g',marker='^')
    #ax.scatter(tmp[1,0],tmp[1,1],tmp[1,2],s=200,c='y',marker='o')
    #ax.scatter(tmp[2,0],tmp[2,1],tmp[2,2],s=200,c='c',marker='s')
    #ax.scatter(tmp[3,0],tmp[3,1],tmp[3,2],s=200,c='b',marker='p')

    # ------ Find the closest CP with centroid
    #obs = whiten(X)
    #features_array = vq(obs,tmp)

    # ------ Plot
    #se.seq(features_array[0],X)
    se.label(label,X)
    #plt.show()
    return tmp
