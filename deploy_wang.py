import os
import subprocess

def echoCmd(cmd):
  ps = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
  while True:
    data = ps.stdout.readline()
    if not data:
      break
    else:
      print data

os.chdir("../ansible_wang")
echoCmd('ansible-playbook -vvv wang.yml')  
