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
 # ##########################################################################################
 # 
 # Author: edony - edonyzpc@gmail.com                 
 # 
 # twitter : @edonyzpc                                
 # 
 # Last modified: 2015-04-01 15:32
 # 
 # Filename: PyNote.py
 # 
 # Description: All Rights Are Reserved                 
class pcolor:
    ''' This class is for colored print in the python interpreter!
    "py" call Addpy() function to add this class which is defined
    in the .vimrc for vim Editor.
    
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
    
    e.g：
    \033[1;31;40m   <!--1-highlight;31-foreground red;40-background black-->
    \033[0m         <!--set all into default-->
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
 
 
def filter(ls):
    '''
    An efficient way to filter the repeat items in list
    '''
    tmp = set(ls)
    return list(tmp)

def pyIdiom_swap(a,b):
    '''
    Swap a and b
    '''
    a,b = b,a
    return a,b

def cache_mechanism():
    '''
    Reference and equal in Python Mechanism
    '''
    print('reference list ls_1 and ls_2')
    ls_1 = [1,2,3]
    ls_2 = ls_1
    print('ls_1 = [1,2,3]\nls_2 = ls_1')
    if(ls_1==ls_2):
        print('ls_1 and ls_2 have the same value, said "ls_1 == ls_2"')
    else:
        print('ls_1 and ls_2 have the different values, said "ls_1 != ls_2"')
    if(ls_2 is ls_1):
        print('ls_1 and ls_2 are referencing the same object')
    else:
        print('ls_1 and ls_2 are referencing the different objects')

    ls_1 = [1,2,3]
    ls_2 = [1,2,3]
    print('ls_1 = [1,2,3]\nls_2 = [1,2,3]')
    if(ls_1==ls_2):
        print('ls_1 and ls_2 have the same value, said "ls_1 == ls_2"')
    else:
        print('ls_1 and ls_2 have the different values, said "ls_1 != ls_2"')
    if(ls_2 is ls_1):
        print('ls_1 and ls_2 are referencing the same object')
    else:
        print('ls_1 and ls_2 are referencing the different objects')

    print('Python cache little digits and strings')
    x = 34
    y = 34
    print('x = 34\ny = 34')
    if(x==y):
        print('x and y have the same value, said "x == y"')
    else:
        print('ls_1 and ls_2 have the different values, said "x != y"')
    if(x is y):
        print('x and y are referencing the same object')
    else:
        print('x and y are referencing the different objects')

def str2FilePath():
    '''
    when we read file from a file direction, we should make sure that the type casting can not work.
    '''
    path = r'/home/edony/code/py'
    #f = open(path+'test.bat')

def slice2str():
    """
    slicing the string that has many ways:
    ...s[0:4]<--str([s[0],s[1],s[2],s[3]])
    ...s[-3:-1]<--str(s[len(s)-3],...)
    ...s[0:10:2]<--take a stride with 2

    s[:-1] help to remove the last item in the string, especially '\n','\r'
    P.S.
        for text file removing whitespace, we are recommended to use str.rstrip()
    """
    pass

def list2str():
    '''
    way to do conversion about list and string in python
    '''
    s = 'spam'
    l = list(s)
    s_again = ''.join(l)

def format2str():
    '''
    string format control way
    '''
    print('\n%s is a %d number'%('edony',24))
    print('\n{0} is a {1} number'%{'edony',24})
    print('\n{0[spam]} is a {0[age]} numbers'%{'spam':'edony','age':24})

def readintomatrix():
    '''
    use python to read file into matrix
    '''
    import numpy as np
    X = []
    f = open('/home/shared/filename')
    row = 0
    tmp = f.readline().split()
    colum = len(tmp)
    for line in f.readlines():
        X.extend(tmp)
        row += 1
        tmp = line.split()
    X = np.array(X)
    X.reshape(row,colum)
    return X

def dictionary():
    '''
    dictionary is a hash
    '''
    D = {'edony':24,'cc':25,'murpht':34}

def evalVSpickle():
    '''
    pickle is modle of python that help to save almost all of the python objects into files

    eval convet to any object in python
    '''
    import pickle
    D = {'a':1,'b':2}
    F = open('file/path','wb')
    pickle.dump(D,F)
    F.close
    #...load the file...
    ## F = open('file/path','rb')
    ## pickle.load(F)
    ## F.close()
    #........................
    X = []
    f = open('another/file/path','w')
    tmp = f.readline().split()
    for i in range(colums):
        tmp[i] = eval(tmp[i])
    X.extend(tmp)

def copyVSreference():
    '''
    understand the usage of cope and reference in python.
    '''
    import copy
    X = [1,2,3]
    L = ['a',X,'b']
    D = {'x':X,'y':2}
    X[2] = 'edony'
    # L and D are referencing X, so L and D are changed after we change X
    print(L)
    print(D)
    L_cp = L[:]
    D_cp = D.copy()
    D_deepcp = copy.deepcopy(D) # copy the inside data structure(said list X)

def equalityVSsame():
    '''
    equivalent and same object in python
    '==' test all objects in variables recursively
    'is' test if the two objects are the same object(in the same memeory)
    '''
    L1=[1,('a',3)]
    L2=[1,('a',3)]
    L1==L2 #True
    L1 is L2 #False

    S1 = 'spam'
    S2 = 'spam'
    S1==S2 #True
    S1 is S2 #True

    S3 = 'a longer string'
    S4 = 'a longer string'
    S3==S4 #True
    S3 is S4 #False(because the S3 is a long string, python cache mechenism will create an other object for S4)

def PyProgram():
    '''
    be clear about python program language
    ...indent
    ...semicolon
    ...pairs for code block
    '''
    #yield in python
    def func_yield(n):
        for i in range(int(n)):
            yield i
            print('NO. of iter: %d'%i+1)
    #in the function calling
    for i in func_yield(10):print(i+10)

def Pystdout():
    '''
    standard input stream redirection in python
    '''
    import sys
    originstream = sys.stdout # backup the origin stdout stream
    sys.stdout = open('~/tmp/log/log.txt','a')
    print('edony')
    print('...')
    #...and so on
    sys.stdout.close()
    f = open('~/tmp/log/log.txt','r')
    for line in f.readlines():
        print line
    f.close()

def Pyif():
    '''
    a better way to switch case is builtin dictionary(much more flexiable)
    if syntax:
    ... if expression:
    ...     do something
    ... elif expression2:
    ...     do something
    ... elif expression3:
    ...     do something
    ... else:
    ...     do something
    '''
    pass

def Pyloops():
    '''
    loops with 'while' and 'for'
    especially, you can add 'else' into the end of the while and for loops
    and when the loops are ended with 'break' the expression after 'else'
    will be executed
    '''
    ls = [1,2,3]
    for item in ls:
        #print(item,end=' ')# python3 syntax
        print item

    ls1=['e','d','n']
    tmp = list(zip(ls,ls1))
    for (a,b) in tmp:
        print('(%s,%s)'%(a,b))

    keys=['edony','cc']
    value=[23,24]
    d = dict(zip(keys,value))
    
    for iter in enumerate(ls): # builtin function for iterator for a iteratorable object
        print ls
        
def iterator():
    '''
    iteratorable object in python to access each member in iteratorable object
    ... file iterator:file.readline()(or file.readlines() or file.__next__())
    ... manual iterator:next() and iter()
    ... NOTE:__next__() and next() sometimes are different
    '''
    pass

def Pyfunction():
    '''
    def is a key word to define a function in python
    and if python function we might use some key words, they are:
    ... 'def' 'lambda' 'yield' 'return' 'global' 'nonlocal'(python3.x)
    '''
    pass

def PyNamespace():
    '''
    namespace control the range of variables's access space
    so called rule: LEGB(local,enclosing,global,builtin)
    ... the order of LEGB query:L-->E-->G-->B

    global variables == module attribute
    '''
    def hider():
        open='spam' # local variables hides builtin
        #...some operations
        open('data.txt') # this will not open a file in this scope

    def marker(N): #factory function
        def action(X):
            return X**N
    return action
    f = marker(2)
    f(3) # 9
    f(4) # 16
    g = marker(3)
    g(3) # 27
    f(3) # 9
    g(4) # 64
    f(4) # 16

    def lambda_func():
        lambda x:x**2
        lambda x,i=2:x**i

    def nonlocal_func():
        '''
        nonlocal variables can remember in enclosing scope and this a python3.x key word
        '''
        pass

def keyarguments():
        '''
        there are some different arguments:
        ... norm parameter % func(value) ====> def func(name)
        ... keyword parameter(default parameter) % func(name=value) ====> def func(name=value)
        ... all objects based on position % func(*sequence) ====> def func(*name)(def func(*arg,name))
        ... all keys and values base on position % func(**dict) ====> def func(**name)
        '''
        # in python3.x, we can refer help(print) to get the details of these parameter
        pass

def func_attr():
    '''
    dir(func_name) to check the attributes of function named func_name
    access the attributes of func_name. e.g. func_name.attri
    ------------------------------------------------------------------
    lambda a fast implementation of function
    improve the simplicity of your code
    ------------------------------------------------------------------
    filter,reduce,map
    ------------------------------------------------------------------
    buitin function > list comprehension > for loops
    '''
    counter = range(10)
    list(map(lambda x:x**i,counter)) #[0,1,4,9,16,25,36,49,64,81]
    list(filter(lambda x:x>0,counter)) #[1,2,3,4,5,6,7,8,9]
    reduce(lambda x,y:x+y,counter) #45

def pytime():
    '''
    to figure out which one of the techologies is the best, I can time it
    '''
    import time
    start = time.clock()
    #...
    end = time.clock()
    total = end - start

def pytrap():
    '''
    personally, better habits can help to avoid these
    '''
    pass

def pyimportmodule():
    '''
    module is the highest level of python code.
    module is a namespace which distinguish by files
    ...key words are 'import','from','imp.reload'
    ------------------------------------------------
    PYTHON FRAMEWORK 
    well, framework is a optimized way to cut the program into different sets of source code and the essential communications between sets are properly built.
    ------------------------------------------------
    schedule about 'import':
    ...1> search the file of the module
    ......(1)main direction of the program
    .........root of the program
    ......(2)PYTHONPATH direction
    .........python environment variable
    ......(3)standard link library direction
    .........the direction of standard library module($(PyDir)/Lib/site-packages)
    ......(4)the details in *.pth file
    .........a new way that use a file to realize the PYTHONPATH setting. 
    .........You can put this file into the direction of standard library
    ......(5)the type of file
    ...2> compile them into bytecode
    ......(1)optional, check the timestamp if it needs to be compiled
    ...3> run the bytecode file
    '''
    pass

def pycreatemodule():
    '''
    import module # import the whole module and a variable will reference the module object
    from module import attributes # import the specific attribute and a same named variable reference it
    form module import * # import the all the attributes and create same names for each of them
    ------------------------------------------------
    import module might tricks you on namespace.
    ------------------------------------------------
    dir()or__dic__() help to get the attributes of module
    '''
    pass

def pypackageimport():
    '''
    import the modules from a specific direction called package import
    ...import dir1.dir2.dir3.packagemodule
    ...1>dir1 must be in the python search path
    ...2>dir2 and dir3 must have a file named __init__.py which works as a hook nothing else
    ...3>if you want to import any module in dir2 or dir3, import needs whole direction
    -------------------------------------------------
    relative import and absolutely import
    ...1>from . import spam 
    ......relative to this package
    ...2>from .spam import name 
    ......from named spam module import attribute name and the spam module in the same direction of current file level
    ...3>from __future__ import absolute_import
    ......open up the absolute searching of python path
    ...4>default searching is that relative searching comes first and absolute searching comes after
    '''
    pass

def pyadvancemodule():
    '''
    1>data hiding
    ...'from *' import module and set a reference between a variable and module's attributes
    ...look out! 'from *' will override you variables silently
    ...'_X' can avoid 'from *' import the module
    2>__future__ module
    ... from __future__ import featurename
    3>__name__ variable
    ... each module has an __name__ attribute and python set it automatically to the module name or '__main__'
    ... if __name__ == '__main__': #add this to the end of the module to check it is import or execute operation
    ...     #do the execution      #__name__ attribute is a useful unit test(self test)
    4>sys.path
    ... import sys
    ... sys.path is the list of the import searching directions
    '''
    pass

def pyoop():
    '''
    oop: inheritance and combination
    ... object.attribute
        climb the class tree to find the attributes(from downside to upside and from left to right)
    ... class and instance
        class is a 'factory' to produce instance
    ... overload
        special hook of builtin operation that help to overload this operation(e.g. '+')
    '''
    class c2:pass
    class c3:pass
    class c1(c2,c3):pass #superclasses c2,c3
    I1 = c1()
    I2 = c2()
    class employee:pass # general superclass
    class engineer(employee):pass # specialize subclass(we do not change the employee class but customize it)

def pycreateinstance():
    '''
    instance to create class and object in python
    '''
    class person():
        def __init__(self,name,job,pay): #constructor
            self.name = name # self is an instance of class object
            self.job = job
            self.pay = pay

        def lastName(self):              #package the operations on class object into the class inside
            return self.name.split()[-1]

        def giveRaise(self,percent):     #packaging into class inside is a better way to maintenance that avoid
                                         #hard-coded
            self.pay = int(self.pay*(1+percent))

        def __str__(self):               #overload print()
            return 'person: %s, %s'%(self.name,self.pay)

    class manager(person): #customize class person
        def giveRaise(self,percent,bound):
            self.pay = int(self.pay*(1+percent+bound)) # not a good idea when the way to calculate pay changes
                                                       # because you will recode twice for person and manager
        def giveRaise(self,percent,bound):
            self.pay = person.giveRaise(self,percent+bound) # better idea with class reference

    #introspection tools
    #object.__class__
    #object.__name__
    #object.__dict__
    #dir(object)
    #-------------------------------------------------------------------------------------------------------#
    #finally, add the self test block
    if __name__ = '__main__':
        #testing operation
        #...

def pyclass():
    '''
    class <name>(superclass,...):
        data = value            #shared class data(class attr)
        def method(self,...):
            self.member = value #per-instance data(instance attr)
    '''
    class Super(): #mostly like abstract base class
        '''
        abstract base class work as a framework that user needs to fill in the blank(e.g. self.action())
        '''
        def delegate(self):
            self.action()
        def action(self):
            assert False,'action must be define'

    class Provider(Super):
        def action(self):
            print 'spam'

    # special syntax for abc
    from abc import ABCMeta,abstractmethod
    class Super(metaclass=ABCMeta):
        @abstractmethod #decorator
        def method(self,...):
            pass

def pyoverload():
    '''
    almost all of builtin operations can be overloaded
    '''
    def __init__():pass #constructor
    def __del__():pass #destructor
    def __add__():pass #+
    def __iadd__():pass #+=
    def __radd__():pass #right +
    def __getitem__():pass #x[2](slice() will call this operation)
    def __setitem__():pass #x[3]=value
    def __iter__():pass #iterator object on iter(copy the iterator object if mutiple iterators are needed)
    def __next__():pass #call builtin next
    def __contain__():pass #prefer in
    def __getattr__():pass #dot operation
    def __setattr__():pass #avoid limitless recursive
    def __call__(self,*pargs,**kargs):pass #collect arbitrary arguments
    #...
    
def pydesignclass():
    '''
    1> the connection betweeen classes(is-a:inheritence or multiple inheritence,has-a:enclose)
    2> delegation with __getattr__()
    3> "private attributes" with _X #not a syntax and just a notation
    4> variable's name mangling with __X(==_classname__X) #helpful for name confliction
    5> binding
        >>> class Spam:
        >>>     def doit(self,message):
        >>>         print(message)
        >>> object1 = Spam()
        >>> object1.doit('hello') #bound method object
        >>> object2 = Spam()
        >>> t = Spam.doit
        >>> t(object2,'hello,two') #unbound method object
    6> class factory
        >>> def factory(aClass, *args): #more generalized factory==>def factory(aClass,*args,**kwargs):...
        >>>     return aClass(*args)
        >>> class Spam:
        >>>     def doit(self,message):
        >>>         print(message)
        >>> class Person:
        >>>     def __init__(self,name,job):
        >>>         self.name = name
        >>>         self.job = job
        >>> object1 = factory(Spam) #make object1
        >>> object2 = factory(Person,'Guido','guru') #make object2
    '''
    pass

def pyadvanceclass():
    '''
    1> extend the builtin operation
    ... overload the builtin
    ... subclass
    2> new-style class
    ... DO NOT UNDERSTAND WHAT HE SAYS!!!
    ... class name(object): #object is a key word in python for new-style class and object is most base type
    ...     pass
    3> diamond pattern
        >>> class A:
        >>>     attr = 1
        >>> class B(A):
        >>>     pass
        >>> class C(A):
        >>>     attr = 2
        >>> class D(B,C):
        >>>     pass
        >>> x = D()
        >>> x.attr
        1
        >>> # class inheritence searching is like a binary tree searching
        >>> # so the search order is D->B->A->C
        >>> # -----------------------------------------------------------
        >>> class A(object):
        >>>     attr = 1
        >>> class B(A):
        >>>     pass
        >>> class C(A):
        >>>     attr = 2
        >>> class D(B,C):
        >>>     pass
        >>> x = D()
        >>> x.attr
        2
        >>> # new-style class inheritence searching is changed
        >>> # so the searching order is D->B->C->A
    4> static methond and class method
        >>> class Spam:
        >>>     numInstance = 0
        >>>     def __init__(self):
        >>>         Spam.numInstance = Spam.numInstance + 1
        >>>     def printNumInstance():#fails in python2.x, but works in python3.x, not a good idea
        >>>         print("Number of instances created: ",Spam.numInstance)
        >>>
        >>> class Method:
        >>>     def imeth(self,x):#instance method
        >>>         print(self,x)
        >>>     def smeth(x):#static method:no instance passed
        >>>         print(x)
        >>>     def cmeth(cls,x):#instance method:get class not instance
        >>>         print(cls,x)
        >>>     smeth = staticmethod(smeth)#make smeth a static method
        >>>     cmeth = classmethod(cmethod)#make cmeth a class method
    5> function decotator:'@ + metafunction'
        >>> class C:
        >>>     @staticmethod #decoration syntax
        >>>     def meth():
        >>>         pass
        >>> # example for function decorator
        >>> class tracer:
        >>>     def __init__(self,func):
        >>>         self.calls = 0
        >>>         self.func = func
        >>>     def __call__(self,*args):
        >>>         self.calls += 1
        >>>         print('call %s to %s'%(self.calls,self.func.__name__))
        >>>         self.func(*args)
        >>> @tracer
        >>> def spam(a,b,c):
        >>>     print(a,b,c)
        >>> spam(1,2,3)
        call 1 to spam
        1 2 3
        >>> spam('a','b','c')
        call 2 to spam
        a b c
        >>> spam(4,5,6)
        call 3 to spam
        4 5 6
    6> class decorator
        >>> def count(aClass):
        ...     aClass.numInstance = 0
        ...     return aClass
        >>> @count
        >>> class Spam:pass
        >>> @count 
        >>> class Sub(Spam):pass
        >>> @count 
        >>> class Other(Spam):pass
        >>> #meta class
        >>> class Meta(type):
        ...     def __new__(meta,classname,supers,classdict):pass
        >>> class C(metaclass=Meta):pass
    7> class trap
        >>> class X:
        ...     a=1
        ...
        >>> I = X()
        >>> I.a
        1
        >>> X.a
        1
        >>> X.a = 2
        >>> I.a
        2
        >>> J = X()
        >>> J.a
        2
        >>> #attribute trap
        >>> class C:
        ...     shared = []
        ...     def __init__(self):
        ...         self.perobj = []
        ...
        >>> x = C()
        >>> y = C()
        >>> y.shared,y.perobj
        ([],[])
        >>> x.shared.append('spam')
        >>> x.perobj.append('spam')
        >>> x.shared,x.perobj
        (['spam'],['spam'])
        >>> y.shared,y.perobj
        (['spam'],[]])
        >>> C.shared
        ['spam']
        '''
        pass

def pyexception():
    '''
    "try/except","try/finally","raise","assert","with/as"
    1> catch exception
        >>> try:
        ...     x[99999]
        ... except IndexError:
        ...     print('catch exception')
    2> raise exception
        >>> try:
        ...     raise IndexError
        ... except IndexError:
        ...     print('catch exception')
        >>> #another raise exception
        >>> assert False, 'Assert Error'
    3> user definition
        >>> class Bad(Exception):
        ...     pass
        >>> def doomed():
        ...     raise Bad()
        >>> try:
        ...     doomed()
        ... except Bad:
        ...     print('got Bad')
    4> terminate
        >>> try:
        ...     x[9999]
        ... finally:
        ...     print('after fetch')
        >>> # if there is exception, the print will not be executed
        >>> def after():
        ...     try:
        ...         x[999999]
        ...     finally:
        ...         print('after fetch')
        ...     print('after fetch?')
        >>> after()
        after fetch
        Traceback ...
        >>> after()
        after fetch
        after fetch?
    '''
    pass

def pyexcepdetail():
    '''
    details on exception in python
    1> try/except/else
        else: if the exception is not happen, the else expresion will be executed
        #e.g.
        try:
            main-action
        except Exception1:
            handler1
        except Exception2:
            handler2
        ...
        else:
            else-block
        finally:
            finally-block
    2> raise
        raise <instance>#raise IndexError
        raise <class>#raise IndexError()
        #e.g.
        class MyExc(Exception):pass
        raise MyExc('spam')
        try:
            ...
        except MyExc as X:
            print(X.args)
    3> assert
        assert <test>,<data> #optional raise
    4> with/as
        with open('/tmp/file') as myfile:
            for line in myfile.readlines():
                print(line)
                ...
    '''
    pass

def pyexcepclass():
    '''
    #builtin exception class
    class Exception
    class BaseException
    #this just help to know about your code running details, debuging
    '''
    pass

def pyadvance():



