#!/usr/bin/env python2
# -*- coding: utf-8 -*-

################################################################
# This Code Has Been Developed By                              #
# Eduardo Marquez -- nose238@hotmail.com                       #
################################################################
import commands
import os

with open("user", "r+") as user_txt:
	user_name = user_txt.read()
	user_txt.seek(0)
	user_txt.write("")

with open("client", "r+") as client_txt:
	client_name = client_txt.read()
	client_txt.seek(0)
	client_txt.write("")

with open("passwd", "r+") as passwd:
	user_pass = passwd.read()
	passwd.seek(0)
	passwd.write("")

if os.path.isdir(client_name):
	print("Client dir already exists.")

else:
	print("Creating "+client_name+" client's folder")
	os.mkdir(client_name)
os.chdir(client_name)
print("Client created... creating user folder")
os.mkdir(user_name)
jailed = commands.getoutput("jk_init -v "+user_name+" netutils basicshell jk_lsh extendedshell editors ssh")
print("1: "+jailed)
useradded = commands.getoutput("adduser "+user_name)
print(useradded)
useradded = commands.getoutput("echo \""+user_pass+"\" | passwd "+user_name+" --stdin ")
print(useradded)
user_jailed = commands.getoutput("jk_jailuser -m -j "+user_name+" "+user_name)
fouended = False
file = open(user_name+"/etc/passwd", "r+")
position = 0
print(file)
for line in file:
	position += len(line)
	print(line)
	if "/usr/sbin/jk_lsh" in line:
		print("Fouded")
		position -= len("/usr/sbin/jk_lsh")
		fouended = True

if fouended:
	file.seek(position)
	file.write("bin/bash\n\n\n\n\n\n")
