import PyZenity
import subprocess

a=PyZenity.InfoMessage("BaGoMa is a tool which will backup your Gmail Emails, so that you can restore or consult them in case the worst happens. Since it may take a while, you can also decide to stop this and restart it later. It will pick up the transfers where it stopped")

login=PyZenity.GetText("First provide your full email login (including @gmail.com)")
password=PyZenity.GetText("Please provide your password",password=True)

proceed=PyZenity.Question("Ok to proceed right now?")

if proceed==True:
  cmd="python bagoma.py -e {0} -p {1}".format(login,password)
  print cmd
  process = subprocess.Popen(cmd, shell=False,
                           stdout=subprocess.PIPE, 
                           stderr=subprocess.PIPE)
  while process.stdout<>"":
    print stdout

else:
  exit
  
  

