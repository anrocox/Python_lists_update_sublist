#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 3, 2014

@author: anroco

How to change a sublist for another in python?

¿como se puede cambiar una sublista por otra en python?
'''

#create a list
lista = ['a', 'c', 'd', 'b', 'e']
print (lista)

#indicates the sublist to be updated
lista[2:4] = ['n', 'p']
print(lista)

#update a list with different data types
lista[1:4] = [1, 'b', 2, 'c', 3, 'd', 4]
print(lista)
