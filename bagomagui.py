import PyZenity
import subprocess
from threading import Thread
import re

found=0

def Run(command):
    proc = subprocess.Popen(command, bufsize=1,
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        universal_newlines=True)
    return proc

def Exiting(message):
    if message=="":
    	a=PyZenity.InfoMessage("You decided not to proceed at this point. Exiting Now")
    else:
    	a=PyZenity.InfoMessage("{0}".format(message))
    exit

def Trace(proc):
    global found
	
    while proc.poll() is None:
        line = proc.stdout.readline()
        if line:
            # Process output here
            print 'Read line', line
            
            if "Invalid credentials" in line:
            	PyZenity.InfoMessage("The credentials you provided do not match. Exiting now.")
		exit
            
            m = re.search('Retrieving (.+?) message', line)
            if m:
            	found = m.group(1)
            	print found
				
            if found!=0:
            	n=re.search(' (.+?)/{0}'.format(found), line)
            	if n:
			messagedl=n.group(1)
			print messagedl
			progress=100*(float(messagedl)/float(found))
			print progress
			proczenity.stdin.write("{0}\n".format(progress))
			proczenity.stdin.write("# Downloading Message {0} out of {1}\n".format(messagedl,found))
					
a=PyZenity.InfoMessage("BaGoMa is a tool which will backup your Gmail Emails, so that you can restore or consult them in case the worst happens. Since it may take a while, you can also decide to stop this and restart it later. It will pick up the transfers where it stopped. Note that the IMAP mode must be ON in your GMail settings for this application to work.")

login=PyZenity.GetText("First provide your full email login (including @gmail.com)")
if login=="None":
    Exiting("")

password=PyZenity.GetText("Please provide your password",password=True)
if password=="None":
    Exiting("You failed to provide any password. Exiting Now.")

directory=PyZenity.GetDirectory(multiple=False,"Select directory to download your emails")
if directory=="None":
    a=PyZenity.InfoMessage("You dit not select any directory. BaGoMa will use the working folder as default")
    

proceed=PyZenity.Question("Ok to proceed right now?")

if proceed==True:
    cmd="./bagoma.py -e {0} -p {1}".format(login,password)
    print cmd
    if directory!="None":
    	command=["python","bagoma.py","-e",login,"-p",password,"-d",directory]
    else:
    	command=["python","bagoma.py","-e",login,"-p",password]
else:
    Exiting("You decided not to proceed at this point. Exiting Now")
    

proc = Run(command)
cmd = 'zenity --progress --text="Backing Up Emails" --auto-close'
proczenity = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
Trace(proc)

message=PyZenity.InfoMessage("The Backup Operation is Now Complete")


