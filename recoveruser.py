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

user_id_file = "removed/"+client_name+"/"+user_name+"/id_at_file"

with open(user_id_file) as user_file:
	id_task = user_file.read()[:-1]

rm_id_at_file = commands.getoutput("rm -f removed/"+client_name+"/"+user_name+"/id_at_file")

print("ID: "+id_task)
delete_at_job = commands.getoutput("at -r "+id_task)

if not os.path.isdir(client_name):
	os.mkdir(client_name)

movedir = commands.getoutput("mv  removed/"+client_name+"/"+user_name+" "+client_name+"/")

recoveruser = commands.getoutput("usermod -U "+user_name)