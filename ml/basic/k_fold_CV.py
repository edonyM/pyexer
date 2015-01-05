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
 # Last modified: 2015-01-05 20:09
 # 
 # Filename: k_fold_CV.py
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
 
#chapter 1. leave one out cross validation(k-fold cross validation and k==N)
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

def del_col(mat,fold,N,K):
    row, col = mat.shape
    if fold*5 < col and (fold+1)*5 < col:
        for col_num in range(fold*5,(fold+1)*5):
            np.delete(mat,col_num,1)
    return mat

x = np.array([1896,1900,1904,1906,1908,1912,1920,1924,1928,1932,1936,1948,1952,1956,1960,1964,1968,1972,1976,1980])
t = np.array([12.00,11.00,11.00,11.20,10.80,10.80,10.80,10.60,10.80,10.30,10.30,10.30,10.40,10.50,10.20,10.00,9.95,10.14,10.06,10.25])
testx = np.array([1984,1988,1992,1996,2000,2004,2008])
testt = np.array([9.99,9.92,9.96,9.84,9.87,9.85,9.69])
N = x.size
K = 4 # K-fold CV
maxdegree = 7 # max degree of the model
X_mat = np.matrix(np.ones(20))
testX_mat = np.matrix(np.ones(20))
t_mat = np.matrix(t)
testt_mat = np.matrix(testt)

for k in range(1,K):
    X_mat = np.matrix([X_mat,np.matrix(x**k)])
    testX_mat = np.matrix([testX_mat,np.matrix(testx**k)])
    tmpX_mat = X_mat
    tmpt_mat = t_mat
    for fold in range(K):
        trainX = del_col(tmpX_mat,fold,N,K)
        print trainX
        foldX = X_mat[fold*5:(fold+1)*5,:]
        print foldX
        traint = del_col(tmpt_mat,fold,N,K)
        foldt = t_mat[fold*5:(fold+1)*5,:]

        w = trainX.getT()
        w = w.dot(trainX)
        w = w.getI()
        w = w.dot(trainX.getT())
        w = w.dot(traint)
        fold_pred = foldX*w
        cv_loss[fold,k+1] = mean((fold_pre - foldt)**2)
        ind_pred = testX_mat*w
        ind_loss[fold,k+1] = mean((testt_mat - ind_pred)**2)
        train_pred = trainX*w
        train_loss[fold,k+1] = mean((train_pred - traint)**2)

print cv_loss
print ind_loss
print train_loss
