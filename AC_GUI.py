#!/usr/bin/python
''' Import Statements '''
import sys
import os
import select
import time
import re
#import Xlib.support.connect as xlib_connect
from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog,tkSimpleDialog, tkMessageBox
from subprocess import PIPE,Popen
from paramiko import *
import paramiko
import glob
import shutil
import socket,errno

#################DEFINTIONS USED THROUGHOUT CODE########################
hostname = '10.241.70.36' ## robinson
username = 'selhash'
password = 'Rfin1ihe'

dirdic = {
    'title': 'Please Select Directory where TMG script results are'
}

dump_dic = {
    'title': 'Please select where to dump the files'
}

import_dic = {
    'title' : 'Please choose where to import the files'
}

Sil_data_dic = {
    'title': 'Please select where silicon data from ISE is located'
}

tmg_dic ={
    'title': 'Please select where result of timing parser is (ie. res_all_{\T}_{\V}.txt)'
}

sil_dic = {
    'title': 'Please select where CRUNCHED Silicon Data is (from parser)'
}
######################################################################

''' GUI Class Creation using Tkinter '''
class AC_GUI(Frame):

    def sysGUIInsert(self,stdout):
        self.top.insert(INSERT, stdout+"\n")

    ## SSH CONNECTION (NEEDS WORK)
    def SSHCONNECT(self,user,pwd):
        self.shell_handler = ShellHandler(hostname, user, pwd)
        paramiko.util.log_to_file("filename.log")
        connected = self.shell_handler.connect()
        return connected


    ## RUNNING OLIVIER's TIMING SCRIPTS (NEEDS WORK)
    def run_timingScript(self):
        pass
        #root = Tk(screenName=None, baseName=None, className='Tk', useTk=1, sync=0, use=None)
        script_filename = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("shell files","*.sh"),("all files","*.*")))
        self.top.insert(INSERT,"Script Chosen: %s\n"%("None" if script_filename=="" else script_filename))
        if(script_filename != ""):
            direc1= script_filename.replace("Z:","/soft/dct")
            print direc1
            conn = self.SSHCONNECT(username, password)
            print str(conn)+"\n"
            if(conn == 0): ## IF ABLE TO CONNECT
                self.top.insert(INSERT,"Correct Username %s and Password %s\n"%(username,password))
                stdin,stdout,stderr = self.shell_handler.execute("sh %s"%(direc1))
                if(stderr):
                    self.top.insert(INSERT,"Error: %s\n"%(stderr))
                self.top.insert(INSERT,"connection closed\n")
            elif(conn == 1):
                self.top.insert(INSERT,"Connection Error\n")
            elif(conn == 2):
                self.top.insert(INSERT,"Authentication error: wrong Username/Password\n")
        else:
            self.top.insert(INSERT,"Process Aborted\n")


    ## CONCATENATE TMG SCRIPT RESULTS INTO ONE FILE AND CHOOSE DUMP DIRECTORY
    def concatenate(self):

        dirname = tkFileDialog.askdirectory(**dirdic)
        self.top.insert(INSERT,"Chose Directory: %s\n"%("None" if dirname=="" else dirname))
        #print dirname
        dirname1 = dirname.replace('/','\\')
        temp_prompt = tkSimpleDialog.askstring("Temp Prompt",'enter temp')
        self.top.insert(INSERT,"TEMP: %s\n"%("None" if temp_prompt=="" else temp_prompt))
        volt_prompt = tkSimpleDialog.askstring("Volt Prompt",'enter volt')
        self.top.insert(INSERT,"VOLT: %s\n"%("None" if volt_prompt=="" else volt_prompt))
        dump_dir = tkFileDialog.askdirectory(**dump_dic)
        self.dump_dir1 = dump_dir.replace('/','\\')

        #runs concatenation script in my shares all
        if(dirname != "" and temp_prompt != "" and volt_prompt != "" and self.dump_dir1 != ""):
            self.top.insert(INSERT,"...Concatenating Timing Files into 1...\n")
            os.system("python \\\sv-fs-01\Shares\All\sammy_alhashemi\AC_SCRIPTS\AC_tmg_file_concat.py %s %s %s %s"%(dirname1,temp_prompt,volt_prompt,self.dump_dir1))
            self.top.insert(INSERT,"    DONE    \n")
        else:
            self.top.insert(INSERT,"...Process aborted...\n")


    ## IMPORT SIL DATA AND CHOOSE DUMP DIR AND FOLDER NAME
    def importISE(self):
        dump_dir = tkFileDialog.askdirectory(**import_dic)
        dump_dir1 = dump_dir.replace('/','\\')
        dump_dir1 = dump_dir1.encode('ascii')
        self.top.insert(INSERT,"Chose Dump Directory: %s\n"%("None" if dump_dir=="" else dump_dir))

        if(dump_dir1 != ""):
            files_to_import_to_dump_dir = tkFileDialog.askopenfilenames(parent = root, title = 'Choose files to import to SIL_DATA')

            self.top.insert(INSERT,"...Importing ISE Files...\n")

            files = list(files_to_import_to_dump_dir) #askopenfilenames returns with unicode encoding
            #convert to ascii
            files_ascii = list(map(lambda x: x.encode('ascii'),files))
            #print(files_ascii)

            for name in files_ascii:
                self.top.insert(INSERT,name)
                k = name.rfind("/")
                name1 = name[k+1:]

                new_file = open("%s/%s"%(dump_dir,name1),"w")
                read_file = open("%s"%(name),"r")
                for line in read_file:
                    new_file.write(line)
            self.top.insert(INSERT,"    DONE    \n")
        else:
            self.top.insert(INSERT,"...Process aborted...\n")

    ## RUNS THE SILICON DATA PARSER FROM ISE AND PUTS IT INTO A FOLDER CALLED 'CRUNCHED'
    def runparser(self):
        Data_dir = tkFileDialog.askdirectory(**Sil_data_dic)
        Data_dir1 = Data_dir.replace('/','\\')
        Data_dir1 = Data_dir1.encode('ascii')

        if(Data_dir1 != ""):
            self.top.insert(INSERT,"Chose Silicon Directory: %s\n"%("None" if Data_dir1=="" else Data_dir1))
            self.CRUNCHED_dir = Data_dir1+"\..\CRUNCHED"
            self.top.insert(INSERT,"CRUNCHED Directory: %s\n"%("None" if self.CRUNCHED_dir=="" else self.CRUNCHED_dir))

            ## Run parser
            os.system("perl \\\sv-fs-01\Shares\All\sammy_alhashemi\AC_SCRIPTS\parse_ac_standby.pl %s"%(Data_dir1))
            os.system("cd %s"%(Data_dir1))
            os.system("cd ..")
            if(not os.path.isfile("CRUNCHED")):
                os.system("mkdir CRUNCHED")


            path = "%s/*.csv"%(Data_dir1)
            for fname in glob.glob(path):
                self.top.insert(INSERT,fname+"\n")
                shutil.move(fname,self.CRUNCHED_dir)
        else:
            self.top.insert(INSERT,"...Process aborted...\n")


    ## YOU GIVE THE SILICON(CRUNCHED)+TIMING DATA AND RUNS A PERL SCRIPT THAT GENERATES RATIOS TO PLOT
    def run_all(self):
        pass
        proc = Popen('C:\cygwin64\Cygwin.bat',stdin = PIPE,stdout = PIPE, bufsize=1)

        dev_prompt = tkSimpleDialog.askstring("dev Prompt",'enter space-separated devices')
        devs = dev_prompt.split(" ")
        tmg_dir = tkFileDialog.askdirectory(**tmg_dic)
        self.top.insert(INSERT,"TMG Directory: %s"%("None" if tmg_dir=="" else tmg_dir))
        sil_dir = tkFileDialog.askdirectory(**sil_dic)
        self.top.insert(INSERT,"Silicon Directory: %s"%("None" if sil_dir=="" else sil_dir))

        dump_dir = tkFileDialog.askdirectory(**dump_dic)
        self.top.insert(INSERT,"Chose Dump Directory: %s"%("None" if dump_dir=="" else dump_dir))
        stdout,stderr = proc.communicate("sh /cygdrive/a/AC_SCRIPTS/run_all.sh %s %s %s"%(tmg_dir,sil_dir,dev_prompt))
        self.top.insert(INSERT,"...Generating Ratios of SIL and TMG Data...\n")
        self.sysGUIInsert(stdout+"\n")

        if(stdout):
            self.top.insert(INSERT,"    DONE    \n")
            for dev in devs:
                shutil.move("C:/Users/selhash/%s"%(dev),dump_dir)
               #os.system("rmdir C:/Users/selhash/%s"%(dev))
        elif(stderr):
            self.top.insert(INSERT,"...ERROR...\n")


    ## CREATING THE GUI AND ATTACHING THE BUTTTONS TO ALL FUNCTIONS DEFINED ABOVE
    ## CAN BE MADE TO LOOK A LITTLE PRETTIER
    def createWidgets(self):

        ## LABEL
        label1 = Label(self,text="AC Data Process Flow:")
        label1.grid(row=0,column=0,sticky=W)
        ## QUIT BUTTON
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT["width"] = 30
        #self.QUIT.pack({"side": "left"})
        #self.QUIT.pack()
        self.QUIT.grid(row=4,column=4)

        ## RUN TIMING SCRIPTS BUTTON
        self.TMG = Button(self)
        self.TMG["text"] = "Run TMG"
        self.TMG["command"] = self.run_timingScript
        self.TMG["width"] = 20
        #self.TMG.pack({"side":"bottom"})
        #self.TMG.pack()
        self.TMG.grid(row=1,column=0)

        ## CONCATENATION BUTTON
        self.CONCAT = Button(self)
        self.CONCAT["text"] = "Concat TMG"
        self.CONCAT["command"] = self.concatenate
        self.CONCAT["width"] = 20
        #self.CONCAT.pack({"side":"right"})
        #self.CONCAT.pack()
        self.CONCAT.grid(row=1,column=1)

        ## IMPORT ISE FILES BUTTON
        self.ISE = Button(self)
        self.ISE["text"] = "Import SIL DATA"
        self.ISE["command"] = self.importISE
        self.ISE["width"] = 20
        #self.ISE.pack()
        self.ISE.grid(row=2,column=0)

        ## RUN 'parse_ac_standby.pl' BUTTON
        self.PARSEISE = Button(self)
        self.PARSEISE["text"] = "Parse SIL DATA"
        self.PARSEISE["command"] = self.runparser
        self.PARSEISE["width"] = 20
        #self.PARSEISE.pack()
        self.PARSEISE.grid(row=2,column=1)

        ## RUN 'run_all.sh' BUTTON
        self.COMPARE = Button(self)
        self.COMPARE['text'] = "Compare SIL and TMG"
        self.COMPARE["command"] = self.run_all
        self.COMPARE["width"] = 20
        #self.COMPARE.pack()
        self.COMPARE.grid(row=3,column=0)

        self.winfo_toplevel().title("AC DATA PROCESSING")


        ## TEXT OUTPUT LOG BOX
        self.top = Text(self,height=10,width=50,wrap=WORD)
        self.top.grid(column=4,row=1)



    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
######################################################################

class ShellHandler:

    def __init__(self, host, user, psw):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.host = host
        self.user = user
        self.psw = psw

    def connect(self):
        try:
            self.ssh.connect(self.host, username=self.user, password=self.psw, port=22)
            channel = self.ssh.invoke_shell()
            self.stdin = channel.makefile('wb')
            self.stdout = channel.makefile('r')
        except paramiko.ssh_exception.AuthenticationException as e:
            print "Incorrect Username %s and Password %s "%(self.user,self.pwd)
            self.top.insert(INSERT,"Incorrect Username %s and Password %s "%(self.user,self.pwd))
            return 2
        except socket.error as e:
            if e.errno == errno.ECONNREFUSED:
                print "Connection Error\n"
                self.top.insert(INSERT,"Connection Error\n")
                return 1
            else:
                print "Something went wrong\n"
                self.top.insert(INSERT,"Something went wrong\n")
                return 1

        print "Correct Username %s and Password %s\n"%(self.user,self.psw)

        return 0

    def __del__(self):
        self.ssh.close()

    def execute(self, cmd):
        try:
            #ssh_stdin,ssh_stdout,ssh_stderr = self.ssh.exec_command("sh %s"%(direc1))
            #ssh_stdin,ssh_stdout,ssh_stderr = self.shell_handler.execute("sh %s"%(direc1))
            stdin,stdout,stderr = self.ssh.exec_command(cmd)
            if(stderr):
                for errors in stderr.readlines():
                    print errors.encode('ascii')
            # print(stderr.readlines())
            # print_counter = 0
            # while(not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready()):
            #     print ("stdout:",stdout.channel.exit_status_ready(), stdout.channel.recv_ready())
            #     if(print_counter%100==0):
            #         print("script running\n")
            #         #AC_GUI.top.insert(INSERT,"script running\n")
            #     time.sleep(0.1)

            #     print_counter+=1

        finally:
            if self.ssh is not None:
                self.__del__()

        return stdin,stdout,stderr
        """

        :param cmd: the command to be executed on the remote computer
        :examples:  execute('ls')
                    execute('finger')
                    execute('cd folder_name')
        """
        # cmd = cmd.strip('\n')
        # print("command: ",cmd)
        # self.stdin.write(cmd + '\n')
        # print ("stdin:"self.stdin)
        # finish = 'end of stdOUT buffer. finished with exit status'
        # echo_cmd = 'echo {} $?'.format(finish)
        # self.stdin.write(echo_cmd + '\n')
        # shin = self.stdin
        # self.stdin.flush()

        # shout = []
        # sherr = []
        # exit_status = 0
        # for line in self.stdout:
        #     if str(line).startswith(cmd) or str(line).startswith(echo_cmd):
        #         # up for now filled with shell junk from stdin
        #         shout = []
        #     elif str(line).startswith(finish):
        #         # our finish command ends with the exit status
        #         exit_status = int(str(line).rsplit(None,1)[1])
        #         if exit_status:
        #             # stderr is combined with stdout.
        #             # thus, swap sherr with shout in a case of failure.
        #             sherr = shout
        #             shout = []
        #         break
        #     else:
        #         # get rid of 'coloring and formatting' special characters
        #         shout.append(re.compile(r'(\x9B|\x1B\[)[0-?]*[ -/]*[@-~]').sub('', line).
        #                      replace('\b', '').replace('\r', ''))

        # # first and last lines of shout/sherr contain a prompt
        # if shout and echo_cmd in shout[-1]:
        #     shout.pop()
        # if shout and cmd in shout[0]:
        #     shout.pop(0)
        # if sherr and echo_cmd in sherr[-1]:
        #     sherr.pop()
        # if sherr and cmd in sherr[0]:
        #     sherr.pop(0)

####################### WHERE CODE IS IMPLEMENTED NAD CLASSES INSTANTIATED #################################

root = Tk()
#device_name = tkSimpleDialog.askstring("Device Prompt", "Enter Device")
app = AC_GUI(master=root)
app.mainloop()
root.destroy()