 #!/usr/bin/env python
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
 # Last modified: 2015-03-28 18:04
 # 
 # Filename: sequence.py
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
import math as m
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D as Ax3
from scipy import stats as st
from matplotlib import cm
 

def seq(fea_seq, X):
    '''
    After kmeans classify the dataset into different clusters, the origin dataset should
    be sequenced by clusters. For the help of scipy library, VQ function can help.
    FUNCTION SEQ(FEA_SEQ,X) take two parameters: observation and code_book from kmeans.
    '''
    num_of_features = 0
    fea = np.zeros(4)
    for i in range(4):
        if i in fea_seq:
            num_of_features += 1
            for j in fea_seq:
                if j==i:
                    fea[i] += 1

    print num_of_features
    #X = r.ReadCPInTxt('extraPoints.txt')
    row = np.size(X,axis=0)
    col = np.size(X,axis=1)
    X_seq = np.zeros((row,col))
    counter = 0
    for j in range(4):
        for i in range(65):
            if fea_seq[i]==j:
                X_seq[counter,:] = X[i,:]
                counter += 1

    print('writing file for sequence of classifier...\n......')
    File = open('extraSeqPoints.txt','w')
    for i in range(row):
        File.write(X[i,0])
        File.write(' ')
        File.write(X[i,1])
        File.write(' ')
        File.write(X[i,2])
        File.write('\n')
    print('successful sequenced...')

def label_seq(label,X):
    '''
    FUNCTION kmeans return two patameters:
    ... The first one is centroids of the clustering
    ... The second one is label of the dataset that flag the cluster
    This function takes the label and the dataset as patameters and divide the dataset into different sets by clustering center. Write them into different files.
    '''
    row = np.size(X,axis=0)
    col = np.size(X,axis=1)
    X_seq = np.zeros((row,col))
    counter = 0
    label_counter = np.zeros(4)
    for i in range(4):
        for j in range(row):
            if label[j]==i:
                X_seq[counter,:] = X[j,:]
                counter += 1
                label_counter[i] += 1
    print('writing file for sequence of classifier...\n......')
    offset = 0
    for file_num in range(4):
        name = str(file_num)+'extraSeqPoints.txt'
        File = open(name,'w')
        for i in range(int(label_counter[file_num])):
            File.write(str(X_seq[i+offset,0]))
            File.write(' ')
            File.write(str(X_seq[i+offset,1]))
            File.write(' ')
            File.write(str(X_seq[i+offset,2]))
            File.write('\n')
        File.close()
        offset += int(label_counter[file_num])
    print('successful sequenced...')
