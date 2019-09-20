#os module import and uses 

'''
import os

Executing a shell command
os.system()    

Get the users environment 
os.environ()   

#Returns the current working directory.
os.getcwd()   

Return the real group id of the current process.
os.getgid()       

Return the current process’s user id.
os.getuid()    

Returns the real process ID of the current process.
os.getpid()     

Set the current numeric umask and return the previous umask.
os.umask(mask)   

Return information identifying the current operating system.
os.uname()     

Change the root directory of the current process to path.
os.chroot(path)   

Return a list of the entries in the directory given by path.
os.listdir(path) 

Create a directory named path with numeric mode mode.
os.mkdir(path)    

Recursive directory creation function.
os.makedirs(path)  

Remove (delete) the file path.
os.remove(path)    

Remove directories recursively.
os.removedirs(path) 

Rename the file or directory src to dst.
os.rename(src, dst)  

Remove (delete) the directory path.
os.rmdir(path)
'''

import os
import time
try:
	say=input('do u want to start ? \n :')
except ZeroDivisionError :
	print("say\'yes\' or \'y\'")

while True:
	if say is'yes' or say is'y':
		time.sleep(.5)
		talk=input('wanna know your file extenction ?\n:')
		if talk =='yes' or talk =='y':
			file=os.getcwd()
			time.sleep(.4)
			print(file)
		else:
			break
	


