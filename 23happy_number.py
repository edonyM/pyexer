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
 # Last modified: 2014-12-20 23:20
 # 
 # Filename: 23happy_number.py
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
 
def is_primer(num):
    tmp = int(num)
    for i in range(2, (int(num / 2) + 1)):
        if num % i == 0:
            return False

    return True

def sum(cou):
    tmp = int(cou)
    a = []
    sum = 0
    while tmp != 0:
        a.append(tmp % 10)
        tmp /= 10

    for ele in a:
        sum += (int(ele) * int(ele))

    return sum

def is_happy(num):
    tmp = int(num)
    sum_num = sum(tmp)
    while sum_num >= 10:
        sum_num = sum(sum_num)

    if sum_num == 1:
        return True
    else:
        return False


happy = []
primer = []
for num in range(1,1001):
    if is_primer(num):
        primer.append(str(num))
    if is_happy(num):
        happy.append(str(num))

#print happy
#print primer
import string
with open('num_file.txt','w') as num_save_file:
    str_primer = ", ".join(primer)
    str_happy = ", ".join(happy)
    num_save_file.write('primer numbers:\n' + str_primer + '\n')
    num_save_file.write('happy numbers:\n' + str_happy + '\n')
    num_save_file.close()
