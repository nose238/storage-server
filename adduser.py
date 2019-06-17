#!/usr/bin/env python2
# -*- coding: utf-8 -*-

################################################################
# This Code Has Been Developed By                              #
# Eduardo Marquez -- nose238@hotmail.com                       #
################################################################
import commands
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--client", help="here you add the client")
parser.add_argument("-u", "--user", help="here you add the user")
parser.add_argument("-p", "--password", help="here you add the user's password")
parser.parse_args()
args = parser.parse_args()

user_name = args.user
client_name = args.client
user_pass = args.password

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
