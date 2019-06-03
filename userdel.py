#!/usr/bin/env python2
# -*- coding: utf-8 -*-

################################################################
# This Code Has Been Developed By                              #
# Eduardo Marquez -- nose238@hotmail.com                       #
################################################################
import commands
import os

with open("clientdel", "r+") as client_txt:
	client_name = client_txt.read()
	client_txt.seek(0)
	client_txt.write("")

with open("userdel", "r+") as user_txt:
	user_name = user_txt.read()
	user_txt.seek(0)
	user_txt.write("")

deleted = commands.getoutput("userdel -r "+user_name)
print(deleted)

os.chdir(client_name)
removedir = commands.getoutput("rm -f -r "+user_name)

os.chdir("..")
try:
	os.rmdir(client_name)
except OSError as ex:
	print(ex)
	print("This is not the unique user into the client. Not possble to delet whole client")
