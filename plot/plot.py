#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""
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
 # Last modified: 2015-08-04 11:20
 #
 # Filename: plot.py
 #
 # Description: All Rights Are Reserved
 #
"""
import scipy as sp
import math as m
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D as Ax3
from scipy import stats as st
from matplotlib import cm
import numpy as np

def plotplane(ax, a, b, c, d):
    x = np.arange(1,10,1)
    y = np.arange(1,10,1)
    x, y = np.meshgrid(x, y)
    #z = np.matrix(np.array([5 for i in range(81)]).reshape(9,9))
    z = a*x + b*y-d*np.ones((9,9))
    
    ax.plot_surface(x,y,z/c)

def plot(para):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    for item in para:
        plotplane(ax, item[0], item[1], item[2], item[3])
    plt.show()

if __name__ == "__main__":
    import random
    for u in range(4):
        print random.randint(0,4)
    para = [[0.05,0.1,-25,-1.75],[0.05,0.05,-25,-0.9995]]
    plot(para)
