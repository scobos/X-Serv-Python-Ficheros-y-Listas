#!/usr/bin/python

fich= open("/etc/passwd","r")
lineas= fich.readlines()
for linea in lineas:
	token = linea.split(':')
	print("User: " , token[0] , ". Shell que utiliza: ", token [-1])
fich.close()
