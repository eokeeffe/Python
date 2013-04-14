"""
	Operating systems modules and usage
	os.-
	-system
	-spawn
	-popen
	-popen2
	-commands
	and so on
	
	as you while see when running this that these are some good
	functions to have for directory manipulations and so on
"""

import os

OS_name = os.name

print OS_name
print os.environ
print os.getcwd()
if OS_name == 'posix':
	print ctermid()
	print getegid()
	print geteuid()
	print getgid()
	print os.getgroups()
	print os.getlogin()
	print os.getpgrp()
	print os.getppid()
	print os.getresgid()
	print os.getresuid()
	print os.getuid()

print os.getpid()
print os.sep
print os.altsep
print os.defpath
print os.urandom(10)