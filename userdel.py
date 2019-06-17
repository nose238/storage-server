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
parser.parse_args()
args = parser.parse_args()

user_name = args.user
client_name = args.client

blockuser = commands.getoutput("usermod -L "+user_name)
print(blockuser)

if not os.path.isdir("removed"):
	os.mkdir("removed")

if not os.path.isdir("removed/"+client_name):
	os.mkdir("removed/"+client_name)

movedir = commands.getoutput("mv "+client_name+"/"+user_name+"/ removed/"+client_name+"/")

try:
	os.rmdir(client_name)
except OSError as ex:
	print(ex)
	print("This is not the unique user into the client. Not possble to delet whole client")

programtask = commands.getoutput('echo "rm -f -r removed/'+client_name+'/'+user_name+' ; \
	rmdir removed/'+client_name+' ; userdel -r '+user_name+'; "  | at now + 2 minutes ')
print(programtask)

id_task = programtask.split()[1]

create_id_file = commands.getoutput("echo "+id_task+" > removed/"+client_name+"/"+user_name+"/id_at_file")
