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
 # Last modified: 2015-01-30 16:31
 # 
 # Filename: ex1_multi.py
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
 

## Machine Learning Online Class
#  Exercise 1: Linear regression with multiple variables
#
#  Instructions
#  ------------
# 
#  This file contains code that helps you get started on the
#  linear regression exercise. 
#
#  You will need to complete the following functions in this 
#  exericse:
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
#  For this part of the exercise, you will need to change some
#  parts of the code below for various experiments (e.g., changing
#  learning rates).
#

## Initialization
## ================ Part 1: Feature Normalization ================
## Clear and Close Figures

print('Loading data ...\n');

## Load Data
f = open('ex1data2.txt')
X1 = np.array([])
X2 = np.array([])
y = np.array([])
iter = 0
for tmp in f.readlines():
    tmp = tmp.split(',')
    X1 = np.append(X1,float(tmp[0].split()[0]))
    X2 = np.append(X2,float(tmp[1].split()[0]))
    y = np.append(y,float(tmp[2].split()[0]))
X1 = np.concatenate(([X1],[X2]),axis=0)
X = X1.T
m = y.shape[0]
# Print out some data points
print('First 10 examples from the dataset: \n');
for i in range(10):
    print(' x = [%.0f %.0f], y = %.0f \n'% (X[i,0],X[i,1],y[i]));

raw_input('Program paused. Press enter to continue.\n');

# Scale features and set them to zero mean
print('Normalizing Features ...\n');
from featureNormalize import featureNormalize
[X,mu,sigma] = featureNormalize(X);

# Add intercept term to X
tmp = np.array(np.ones((m, 1)));
tmp = np.concatenate((tmp,X),axis=1);
X = tmp;

## ================ Part 2: Gradient Descent ================

# ====================== YOUR CODE HERE ======================
# Instructions: We have provided you with the following starter
#               code that runs gradient descent with a particular
#               learning rate (alpha). 
#
#               Your task is to first make sure that your functions - 
#               computeCost and gradientDescent already work with 
#               this starter code and support multiple variables.
#
#               After that, try running gradient descent with 
#               different values of alpha and see which one gives
#               you the best result.
#
#               Finally, you should complete the code at the end
#               to predict the price of a 1650 sq-ft, 3 br house.
#
# Hint: By using the 'hold on' command, you can plot multiple
#       graphs on the same figure.
#
# Hint: At prediction, make sure you do the same feature normalization.
#

print('Running gradient descent ...\n');
# Choose some alpha value
alpha = 0.01;
num_iters = 400;

# Init Theta and Run Gradient Descent 
from gradientDescent import gradientDescentMulti
theta = np.zeros((3, 1));
[theta, J_history] = gradientDescentMulti(X, y, theta, alpha, num_iters);

# Plot the convergence graph
fig = plt.figure;
plt.plot(np.arange(J_history.size), J_history, '-b', linewidth=2);
plt.xlabel('Number of iterations');
plt.ylabel('Cost J');
plt.show();

# Display gradient descent's result
#fprintf('Theta computed from gradient descent: \n');
#fprintf(' %f \n', theta);
#fprintf('\n');

# Estimate the price of a 1650 sq-ft, 3 br house
# ====================== YOUR CODE HERE ======================
# Recall that the first column of X is all-ones. Thus, it does
# not need to be normalized.
#price = transpose(theta)*[1; (1650-mu(1))/sigma(1); (3-mu(2))/sigma(2)]; % You should change this


# ============================================================

#fprintf(['Predicted price of a 1650 sq-ft, 3 br house ' ...
#         '(using gradient descent):\n $%f\n'], price);

#fprintf('Program paused. Press enter to continue.\n');
#pause;

## ================ Part 3: Normal Equations ================

#fprintf('Solving with normal equations...\n');

# ====================== YOUR CODE HERE ======================
# Instructions: The following code computes the closed form 
#               solution for linear regression using the normal
#               equations. You should complete the code in 
#               normalEqn.m
#
#               After doing so, you should complete this code 
#               to predict the price of a 1650 sq-ft, 3 br house.
#

#% Load Data
#data = csvread('ex1data2.txt');
#X = data(:, 1:2);
#y = data(:, 3);
#m = length(y);

# Add intercept term to X
#X = [ones(m, 1) X];

# Calculate the parameters from the normal equation
#theta = normalEqn(X, y);

# Display normal equation's result
#fprintf('Theta computed from the normal equations: \n');
#fprintf(' %f \n', theta);
#fprintf('\n');


# Estimate the price of a 1650 sq-ft, 3 br house
# ====================== YOUR CODE HERE ======================
#tmpx = [1;1650;3];
#price = transpose(theta)*tmpx; % You should change this


# ============================================================

#fprintf(['Predicted price of a 1650 sq-ft, 3 br house ' ...
#         '(using normal equations):\n $%f\n'], price);

