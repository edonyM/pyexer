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
 # Last modified: 2016-01-02 20:21
 #
 # Filename: binsearch.py
 #
 # Description: All Rights Are Reserved
 #
"""
#import scipy as sp
#import math as m
#import matplotlib as mpl
#import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D as Ax3
#from scipy import stats as st
#from matplotlib import cm
#import numpy as np

class PyColor(object):
    """ This class is for colored print in the python interpreter!
    "F3" call Addpy() function to add this class which is defined
    in the .vimrc for vim Editor."""
    def __init__(self):
        self.self_doc = r"""
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
        e.g:
        \033[1;31;40m   <!--1-highlight;31-foreground red;40-background black-->
        \033[0m         <!--set all into default-->
        """
        self.warningcolor = '\033[0;31m'
        self.tipcolor = '\033[0;32m'
        self.endcolor = '\033[0m'
        self._newcolor = ''
    @property
    def new(self):
        """
        Customized Python Print Color.
        """
        return self._newcolor
    @new.setter
    def new(self, color_str):
        """
        New Color.
        """
        self._newcolor = color_str
    def disable(self):
        """
        Disable Color Print.
        """
        self.warningcolor = ''
        self.endcolor = ''

def bin_search(start, end, ls, item):
    """Test If Item Is In List ls
    """
    mid = (start + end)/2
    if end-start < 2:
        if ls[start] == item:
            print 'st'
            return start
        if ls[end] == item:
            print 'en'
            return end
        else:
            print 'no'
            return -1
    else:
        if item < ls[mid]:
            return bin_search(start, mid-1, ls, item) # If there is no key-word return, if will return None
                                                      # Why? I remeber it works in C without return
                                                      # Done(edony): My faliure to remeber C code
        elif item > ls[mid]:
            return bin_search(mid+1, end, ls, item)
        else:
            print 'mid'
            print mid
            return mid

def select_sort(ls):
    """
    Selection Sort
    """
    num = len(ls)
    for i in range(num):
        tmp = ls[i]
        pos = i
        for j in range(i+1, num):
            if ls[j] < tmp:
                tmp = ls[j]
                pos = j
        ls[i],ls[pos] = ls[pos], ls[i]

def bubble_sort(ls):
    """
    Bubble Sort
    """
    num = len(ls)
    for i in range(num-1, 0, -1):   # Set the flag for test if exchange or break for it is sorted
        for j in range(i):
            if ls[j] > ls[j+1]:
                ls[j], ls[j+1] = ls[j+1], ls[j]

if __name__ == '__main__':
    l = range(20)
    r1 = bin_search(0, 19, l, -1)
    r2 = bin_search(0, 19, l, 10)
    r3 = bin_search(0, 19, l, 0)
    r4 = bin_search(0, 19, l, 19)
    r5 = bin_search(0, 19, l, 9)
    print r1, r2, r3, r4, r5
    print type(bin_search(0, 19, l, 4))
    print bin_search(0, 19, l, 8)
    s = [3, 7, 9, 1, 4, 6]
    tt = select_sort(s)
    print tt
