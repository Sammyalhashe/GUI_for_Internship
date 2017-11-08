#!/usr/bin/python
''' Import Statements '''
import sys
import os
from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog,tkSimpleDialog, tkMessageBox
from subprocess import PIPE,Popen
from paramiko import *
import glob
import shutil

#########################################
hostname = '10.241.70.36'
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

''' GUI Class Creation using Tkinter '''
class AC_GUI(Frame):

    def sysGUIInsert(self,stdout):
        self.top.insert(INSERT, stdout+"\n")

    ## SSH CONNECTION (NEEDS WORK)
    def SSHCONNECT(self,user,pwd):
        pass
        self.ssh = SSHClient()
        self.ssh.set_missing_host_key_policy(AutoAddPolicy())
        try:
            self.ssh.connect(hostname, port=22, username=username, password=password, pkey=None, key_filename=None, timeout=10, allow_agent=True, look_for_keys=True, compress=False, sock=None, gss_auth=False, gss_kex=False, gss_deleg_creds=True, gss_host=None, banner_timeout=None, auth_timeout=None, gss_trust_dns=True)
        except SSHException.AuthenticationException as e:
            print "Incorrect Username %s and Password %s "%(username,password)
        else:
            print "Correct Username %s and Password %s"%(username,password)
        self.transport = self.ssh.get_transport()
        self.session = self.transport.open_session()
        self.session.request_x11(single_connection = True)
        self.session.exec_command('xterm')
        self.x11_chan = transport.accept(timeout=None)

    ## RUNNING OLIVIER's TIMING SCRIPTS (NEEDS WORK)
    def run_timingScript(self):
        pass
        #root = Tk(screenName=None, baseName=None, className='Tk', useTk=1, sync=0, use=None)
        root.filename = tkFileDialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("shell files","*.sh"),("all files","*.*")))

        #self.SSHCONNECT("selhash", "Rfin1ihe")
        #self.session.exec_command('cd ')
        proc = Popen('C:\cygwin64\Cygwin.bat',stdin = PIPE,stdout = PIPE, bufsize=1)
        stdout,stderr = proc.communicate('sshpass -p %s ssh -X -t robinson'%password)
        print stdout

    ## CONCATENATE TMG SCRIPT RESULTS INTO ONE FILE AND CHOOSE DUMP DIRECTORY
    def concatenate(self):
        #root = Tk(screenName=None, baseName=None, className='Tk', useTk=1, sync=0, use=None

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





root = Tk()
#device_name = tkSimpleDialog.askstring("Device Prompt", "Enter Device")
app = AC_GUI(master=root)
app.mainloop()
root.destroy()