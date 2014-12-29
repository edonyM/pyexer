#! /usr/bin/python
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
 # Last modified: 2014-12-25 23:28
 # 
 # Filename: non_linear_fit.py
 # 
 # Description: All Rights Are Reserved                 
class pcolor:
    ''' This class is for colored print in the python interpreter!
    "py" call Addpy() function to add this class which is defined
    in the .vimrc for vim Editor.
    '''
    WARNING = '\033[0;32;43m'
    ENDC = '\033[0m'
    def disable(self):
        self.ENDC = ''
        self.WARNING = ''
 
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

x = np.array([1896,1900,1904,1906,1908,1912,1920,1924,1928,1932,1936,1948,1952,1956,1960,1964,1968    ,1972,1976,1980,1984,1988,1992,1996,2000,2004,2008])
y = np.array([12.00,11.00,11.00,11.20,10.80,10.80,10.80,10.60,10.80,10.30,10.30,10.30,10.40,10.50,    10.20,10.00,9.95,10.14,10.06,10.25,9.99,9.92,9.96,9.84,9.87,9.85,9.69])
one = np.ones(27)
X = np.matrix([one,x,x**2,x**3]).getT()
t = np.matrix(y).getT()
X_Trans = X.getT()
tmp = X_Trans * X
tmp_inve = tmp.getI()
out = tmp_inve * X_Trans * t
func = lambda x,y:(x[0] + x[1] * y + x[2] * y**2 + x[3] * y**3)
res = np.array(out)
x = np.array(X[:,1])
y = np.array(y)
plt.plot(x,y,'ro',np.arange(1890,2060,4),func(res,np.arange(1890,2060,4)))
plt.show()

