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
parser.add_argument("-H", "--Hard", help="here you add user's hard limit")
parser.add_argument("-s", "--soft", help="here you add user's soft limit")
parser.parse_args()
args = parser.parse_args()

user_name = args.user
client_name = args.client
user_pass = args.password
hard_limit = args.Hard
soft_limit = args.soft

if int(soft_limit) > int(hard_limit):
	print("Hard limit must be greater than soft limit. Try again!")
	exit()

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
path = user_name+"/usr/bin/id"
with open(path, "w") as id:
	id.write("")
chpermises = commands.getoutput("chmod 777 "+path)
print(chpermises)
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
file.close()
quota = commands.getoutput("setquota -u "+user_name+" "+soft_limit+" "+hard_limit+" 0 0 /")
print(quota)
