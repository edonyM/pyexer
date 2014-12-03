#! /usr/local/python2.7.8/bin/python2.7
num = input("Give me the times to print: ")
name = input("Give me your name: ")
nick = raw_input("Give me your nick name: ")
age = int(input("Give me your age: "))
cou = int(num)
while cou > 0:
    print "You are turned out that you will live 100 years old! %s.%s.%d!" % (name, nick, age)
    cou -=1
