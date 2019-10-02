#!/usr/bin/env python
# -*- coding:utf-8 -*-
import os
import paramiko
import time
from scp import SCPClient



# Script to the server and extract it
def transRemote(ip,user,password):
    try:

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, 22, username=user, password=password, timeout=200)
        stdin, stdout, stderr=ssh.exec_command("pwd")
        #path=stdout.read().strip("\n")

        # Get road strength
        path= stdout.read().decode('utf-8').strip("\n")

        # View python version
        stdin, stdout, stderr=ssh.exec_command("python -V")
        print(stdout.read().decode('utf-8'))
        # pythonVsersion=stdout.read().strip("\n")
        pythonVsersion = stdout.read().decode('utf-8').strip("\n")
        scriptName="olilaf.tar.gz"
        if(len(pythonVsersion)==0):
            scriptName="olilaf.tar.gz"
        else:
            if(pythonVsersion.split()[1].startswith("3")):
                scriptName="olilaf.tar.gz"

        current_path=os.getcwd()
        #print current_path
        scpclient = SCPClient(ssh.get_transport(), socket_timeout=15.0)
        scpclient.put('%s\\check\\%s'%(current_path,scriptName), '%s/olilaf.tar.gz'%path)
        print("[*]Transfering the script to the remote server")

        index=0
        script_number=12
        while(index<10):
            stdin, stdout, stderr=ssh.exec_command('tar -xvf %s/olilaf.tar.gz'%path)
            time.sleep(2)
            stdin, stdout, stderr=ssh.exec_command("ls %s"%(path))
            scripts=len(stdout.read().decode('utf-8').strip("\n"))
            if(scripts==12):
                index=11
            else:
                index+=1
        print("[*]Extracting the script on the remote server")
        ssh.close()
        return True
    except Exception as e:
        print(e)
    return False

if __name__ == '__main__':
    transRemote('192.168.221.133','root','toor')
