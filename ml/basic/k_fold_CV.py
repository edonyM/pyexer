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

def num_power(x,deg):
    tmp = np.array(np.zeros(x.size))
    for counter in range(x.size):
        tmp[counter] = long(int(x[0][counter])**deg)
    return tmp

x = np.array([[1896,1900,1904,1906,1908,1912,1920,1924,1928,1932,1936,1948,1952,1956,1960,1964,1968,1972,1976,1980]])
t = np.array([12.00,11.00,11.00,11.20,10.80,10.80,10.80,10.60,10.80,10.30,10.30,10.30,10.40,10.50,10.20,10.00,9.95,10.14,10.06,10.25])
testx = np.array([[1984,1988,1992,1996,2000,2004,2008]])
testt = np.array([9.99,9.92,9.96,9.84,9.87,9.85,9.69])
N = x.size
K = 4 # K-fold CV
maxdegree = 7 # max degree of the model
X_mat = np.array([np.ones(20)])
testX_mat = np.array([np.ones(7)])
t_mat = np.matrix(t)
testt_mat = np.matrix(testt)
cv_loss = np.array(np.zeros((4,7)))
ind_loss = np.array(np.zeros((4,7)))
train_loss = np.array(np.zeros((4,7)))

# LOOCV
for deg in range(1,maxdegree+1):
    x_power = num_power(x,deg)
    testx_power = num_power(testx,deg)
    X_mat = np.concatenate((X_mat,[x_power]),axis=0)
    X_mat = np.matrix(X_mat)
    testX_mat = np.concatenate((testX_mat,[testx_power]),axis=0)
    testX_mat = np.matrix(testX_mat)
    tmpX_mat = X_mat
    tmpt_mat = t_mat
    for fold in range(K):
        trainX_trans = del_col(tmpX_mat,fold,N,K)
        foldX_trans = X_mat[:,fold*5:(fold+1)*5]
        traint_trans = del_col(tmpt_mat,fold,N,K)
        foldt_trans = t_mat[:,fold*5:(fold+1)*5]

        # compute the para 'w' of fit model
        # 'w' is an array inlcuding polynomial para
        w = ((trainX_trans * trainX_trans.T).I) * trainX_trans * (traint_trans.T)

        # calculate the loss
        fold_pred = foldX_trans.T*w
        cv_loss[fold,deg-1] = np.mean((np.array(fold_pred - foldt_trans.T))**2,axis=0)
        ind_pred = testX_mat.T*w
        ind_loss[fold,deg-1] = np.mean((np.array(testt_mat - ind_pred))**2)
        train_pred = trainX_trans.T*w
        train_loss[fold,deg-1] = np.mean((np.array(train_pred - traint_trans.T))**2)

# view the results
print cv_loss
print "------"
print ind_loss
print "------"
print train_loss
print "------"
line1,=plt.plot(range(1,maxdegree+1),np.mean(cv_loss,axis=0),'r:',label='CV loss',linewidth=2)
line2,=plt.plot(range(1,maxdegree+1),np.mean(ind_loss,axis=0),'b--',label='independent loss',linewidth=2)
line3,=plt.plot(range(1,maxdegree+1),np.mean(train_loss,axis=0),'g+',label='train loss',linewidth=2)
plt.legend(loc=2,fontsize='small')
plt.show()
