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
 # Last modified: 2015-01-29 15:39
 # 
 # Filename: ex1.py
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
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D as Ax3
from scipy import stats as st
 

## Machine Learning Online Class - Exercise 1: Linear Regression

#  Instructions
#  ------------
# 
#  This file contains code that helps you get started on the
#  linear exercise. You will need to complete the following functions 
#  in this exericse:
#
#     warmUpExercise.m
#     plotData.m
#     gradientDescent.m
#     computeCost.m
#     gradientDescentMulti.m
#     computeCostMulti.m
#     featureNormalize.m
#     normalEqn.m
#
#  For this exercise, you will not need to change any code in this file,
#  or any other files other than those mentioned above.
#
# x refers to the population size in 10,000s
# y refers to the profit in $10,000s
#

## ==================== Part 1: Basic Function ====================
from warmUpExercise import warmUpExercise
print "Runing warmUpExercise.py..."
print "5x5 Indentity Matrix:"

warmUpExercise()
raw_input("Program paused.Press enter key to continue...")

## ======================= Part 2: Plotting =======================
print "Plotting Data..."
f = open('ex1data1.txt')
X = np.array(np.empty(1))
y = np.array(np.empty(1))
for tmp in f.readlines():
    tmp = tmp.split(',')
    X = np.append(X,float(tmp[0].split()[0]))
    y = np.append(y,float(tmp[1].split()[0]))
from plotData import plotData as plot
plot(X,y)
raw_input("Program paused.Press enter key to continue...")

## =================== Part 3: Gradient descent ===================
print('Running Gradient Descent ...\n')
x = np.array([np.ones(y.shape)])
x = np.concatenate((x,[X]),axis=0)
theta = np.zeros((2,1))

iteration = 1500
alpha = 0.01

# compute and display initial cost
from computeCost import computeCost as compC
x = np.matrix(x.T)
y = np.matrix(np.array([y])).T
print compC(x,y,theta)
# compute and display initial cost
from gradientDescent import gradientDescent
theta = gradientDescent(x,y,theta,alpha,iteration)
print theta
# Predict values for population sizes of 35,000 and 70,000
prex1 = 35000
prex2 = 70000
print('For population = 35,000, we predict a profit of %f\n'%([1,prex1]*theta)[0,0])
print('For population = 70,000, we predict a profit of %f\n'%([1,prex2]*theta)[0,0])
raw_input('Program paused. Press enter to continue.\n');

## ============= Part 4: Visualizing J(theta_0, theta_1) =============
print('Visualizing J(theta_0, theta_1) ...\n')
theta_0 = np.array([np.linspace(-10,10,num=100)])
theta_1 = np.array([np.linspace(-1,4,num=100)])
J_theta = np.array(np.empty((100,100)))
for i in range(100):
    for j in range(100):
        J_theta[i,j] = compC(x,y,[[theta_0[0,i]],[theta_1[0,j]]])
from plotData import plot3d
print theta_0.shape
print theta_1.shape
print J_theta.shape
plot3d(theta_0,theta_1.T,J_theta)
#f = open('test.bat','w')
#for i in range(100):
#    for j in range(100):
#        f.write('%f '%J_theta[i,j])
#    f.write('\n')
#f.close()
from plotData import plotcontour as cont
cont(theta_0.T,theta_1.T,J_theta,theta)
