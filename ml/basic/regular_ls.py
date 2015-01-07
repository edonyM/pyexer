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
 # Last modified: 2015-01-07 10:09
 # 
 # Filename: regular_ls.py
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
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

def del_row(mat,kfold):
    tmp = np.matrix(np.zeros((mat.shape[0]-1,mat.shape[1])))
    row_tmp = 0
    for row in range(mat.shape[0] - 1):
        if row == kfold:
            row_tmp +=1
            tmp[row,:] = mat[row_tmp,:]
        else:
            tmp[row,:] = mat[row_tmp,:]
        row_tmp +=1
    return tmp

# Initial the data of the olympics 100m time and its year
oly_data = open('olympics.txt','r')
x = np.array([])
t = np.array([])
for line in oly_data.readlines():
    tmp = line.split('\t')
    x = np.append(x,int(tmp[0]))
    t = np.append(t,float(tmp[1].replace('\r\n','')))
oly_data.close()

# Initial the data of X about degree one and degree five
X_mat_one = np.matrix([np.ones(x.size),x])
X_mat_five = X_mat_one
for deg in range(2,5):
    X_mat_five = np.concatenate((np.array(X_mat_five),[x**deg]),axis=0)
X_mat_one = X_mat_one.T
X_mat_five = X_mat_five.T
t_mat = np.matrix(t).T

# Calculate K fold cross validation with regularization least-square method
# the lamda of reg-ls range from 0 to 0.02 with the step 0.0001
cv_loss_one = np.matrix(np.zeros((X_mat_one.shape[0],20)))
cv_loss_five = np.matrix(np.zeros((X_mat_one.shape[0],20)))
for k in range(X_mat_one.shape[0]):
    for lamda in range(0, 20):
        foldX_one = X_mat_one[k,:]
        trainX_one = del_row(X_mat_one,k)
        foldt_one = t_mat[k,:]
        traint_one = del_row(t_mat,k)

        foldX_five = np.matrix(X_mat_five[k,:])
        trainX_five = del_row(X_mat_five,k)
        foldt_five = t_mat[k,:]
        traint_five = del_row(t_mat,k)
        
        IE = np.identity(trainX_one.shape[1])
        IE_five = np.identity(trainX_five.shape[1])
        N = trainX_one.shape[0]
        N_five = trainX_five.shape[0]
        #if lamda < 2:
            #print trainX_one
        w_one = ((trainX_one.T * trainX_one + N * (lamda/10+0.9) * IE).I) * (trainX_one.T) * traint_one
        w_five = ((trainX_five.T * trainX_five + N_five * (lamda/10+0.9) * IE_five).I) * (trainX_five.T) * traint_five
        
        fold_pred_one = foldX_one * w_one
        cv_loss_one[k,lamda] = (foldt_one - fold_pred_one)**2
        fold_pred_five = foldX_five * w_five
        cv_loss_five[k,lamda] = (foldt_five - fold_pred_five)**2
        
lamda_one = np.array([])
lamda_five = np.array([])
for i in range(20):
    lamda_one = np.append(lamda_one, np.mean(cv_loss_one,axis=0)[0,i])
    lamda_five = np.append(lamda_five, np.mean(cv_loss_five,axis=0)[0,i])
CV_L_ONE = np.mean(lamda_one,axis=0)
CV_L_FIVE = np.mean(lamda_five,axis=0)
print CV_L_ONE
print CV_L_FIVE
fig = plt.figure(1)
ax = Axes3D(fig)
px = np.array([range(X_mat_one.shape[0])])
px = px.T
py = np.array([range(0,20)])
ax.plot_surface(px,py,np.array(cv_loss_one),rstride=1,cstride=1,color='g')
ax.plot_surface(px,py,np.array(cv_loss_five),rstride=1,cstride=1,alpha=0.9,color='r')
ax.text(0,20,4,'cv loss: %f'%CV_L_ONE,color='g')
ax.text(20,20,0,'cv loss: %f'%CV_L_FIVE,color='r')
ax.set_xlabel('k-fold')
ax.set_ylabel('lamda')
ax.set_zlabel('cv-loss')
plt.show()
