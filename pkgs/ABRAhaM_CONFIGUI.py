#-------------------------------------------------------------------------------
# Name:        ABRAhaM_CONFIGUI
# Purpose:     Configuration Operations and CONFIG GUI
# Author:      Amazingred
# Created:     1223032414
#-------------------------------------------------------------------------------
import sys, re, os, tkMessageBox, xml.dom.minidom
from Tkinter import *
import xml.etree.ElementTree as et
import ABRAhaM_DOC as abedocs


#TODONEXT:Check disabled account variable saving, recalling, also make disabled a tickbox in edit and password values hidden in edit

#TODO: Change the scrollbox to a listbox on account and preference selection
#TODO: Set up advanced account settings with button that spawns another screen contianing all the settings (i.e. timeouts, retries, error messages, alerts when x, etc
#TODO: Assemble classes with similar class types under class groups...i.e.Configfile, Accounts, Preferences, etc.
#TODO: insert self.status message updates EVERYWHERE in the script when the operation changes

accountsdict=dict()
settingsdict=dict()

class ConfigError(Exception):
    def __init__(self,message):
        Exception.__init__(self,message)

class ConfigFile:
    def __init__(self, configfile):
        self.root=Tk()
        self.root.withdraw()
        if os.path.exists(configfile):
            try:
                self.xmlroot=et.parse(configfile).getroot()
                self.xmlacnts=self.xmlroot.find('Accounts')
                if self.xmlacnts==None:
                    self.xmlacnts=et.SubElement(self.xmlroot, 'Accounts')
                else:
                    for acnt in xmlacnts.iter():
                        accountsdict[acnt.tag]={'password':acnt.find('password').text,'disabled':acnt.find('disabled').text, 'retries':acnt.find('retries').text, 'type':acnt.find('type').text}
                self.xmlgeneral=self.xmlroot.find('Preferences')
                if self.xmlpreferences==None:
                    self.xmlpreferences=et.SubElement(self.xmlroot, 'Preferences')
            except:
                if tkMessageBox.askyesno('ERROR',abedocs.ErrorMessages(102)):
                    self.xmlsetup()
                else:
                    tkMessageBox.showerror('PROGRAM EXITING', abedocs.ErrorMessages(103))
                    sys.exit(1)
        else:
            if tkMessageBox.askyesno('ERROR',abedocs.ErrorMessages(101)):
                self.xmlsetup()
            else:
                tkMessageBox.showerror('PROGRAM EXITING', abedocs.ErrorMessages(103))
                sys.exit(1)

    def xmlsetup(self):
        #Creates new Elements from scratch
        #Accounts, Preferences, and Rootnode
        #Accounts save in this format:
            #<configure>
                #<Accounts>
                    #<login email=abcd@gmail.com disabled=false>
                        #<type>acttype</type>
                        #<password>pword</password>
                        #<customsetting>csetting</customsetting>  <---add these as needed
                    #</login>
                #</Accounts>
                #<Preferences>
                #</Preferences>
            #</configure>
        self.xmlroot=et.Element('Configure')
        self.xmlpreferences=et.SubElement(self.xmlroot,'Preferences')
        self.xmlacnts=et.SubElement(self.xmlroot, 'Accounts')

    def readconfig(self):
        #If os.path.exists(configfilename) attempts to parse the file
        #Checks to make sure the required elements are there
        #Adds empty defaults for those that arent
        #Loads the xml variables for use with the program
        pass

    def newconfig(self):
        #Call xmlsetup to create nodes
        pass

    def saveconfig(self):
        #Write All preference settings to tree
        #Write All logins to tree
        #write any misc settings to tree
        #Write modification date to tree
        #prettify
        #save configfile
        #change status
        #close GUI
        pass

    def prettify(self,elem):
        """Return a pretty-printed XML string for the Element.  Props goes
        to Maxime from stackoverflow for this code."""
        rough_string = ElementTree.tostring(elem, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="\t")

class AddSettings:
    def __init__(self, parent):
        top=self.top=Toplevel(parent)
        Label(top, text="Add Settings Dialog").grid(column=0, row=0, columnspan=2,sticky='ew')

class EditSettings:
    def __init__(self, parent,setting):
        """Edit a setting selected before calling this class."""
        self.value_list=[]
        self.setting=setting
        top=self.top=Toplevel(parent)
        Label(top, text="Editing Selected Setting").grid(column=0, row=0, columnspan=2,sticky='ew')
        self.value_list = []
        row=1
        for k,v in settingsdict[self.setting].iteritems():
            var=StringVar()
            var.set(v)
            if k=='disabled':
                x=Checkbutton(self.top, text='Disabled', onvalue='true', offvalue='false',variable=var).grid(row=row,column=0, columnspan=2, sticky='ew')
            else:
                Label(self.top, text=k).grid(row=row, column=0,sticky='ew')
                Entry(self.top, textvariable=var).grid(row=row, column=1,sticky='ew')
            row+=1
            self.value_list.append((k,var))
        Button(self.top, text='Save Settings',command=self.save_changes).grid(row=row+1, column=0, sticky='ew')
        Button(self.top, text="Cancel Changes", command=lambda: self.top.destroy()).grid(row=row+1, column=1, sticky='ew')

    def save_changes(self):
        for i in self.value_list:
            settingsdict[self.setting][i[0]]=i[1].get()
        self.top.destroy()

class SelectSettingEdit:
    def __init__(self, parent):
        top=self.top=Toplevel(parent)
        Label(top, text="Select A Setting To Edit").grid(column=0, row=0, columnspan=2)
        self.settings=Listbox(top)
        for k in settingsdict.keys():
            self.settings.insert(END, k)
        self.ok=Button(top, text='Select',command=self.select)
        self.delete=Button(top, text='Delete Selected', command=self.deleteSetting)
        self.done=Button(top, text='Done',command=self.top.destroy)
        self.ok.grid(column=0,row=4,sticky='ew')
        self.delete.grid(column=0, row=5, columnspan=2, sticky='ew')
        self.done.grid(column=1, row=4,sticky='ew')
        self.settings.grid(column=0, row=1, columnspan=2, rowspan=3, sticky='ew')

    def deleteSetting(self):
        x=response=tkMessageBox.askokcancel("Deletion Confirmation","Are you sure you would like to delete this Setting?")
        if x:
            setting=self.settings.get(self.settings.curselection())
            settingsdict.pop(setting)
            sol=tkMessageBox.askokcancel('Continue Editing?','Would you like to continue editing?')
            if sol:
                self.settings.destroy()
                self.settings=Listbox(self.top)
                for k in settingsdictdict.keys():
                    self.settings.insert(END, k)
                self.settings.grid(column=0, row=1, rowspan=3, columnspan=2)
                self.settings.focus_set()
            else:
                self.top.destroy()

    def select(self):
        setting=self.settings.get(self.settings.curselection())
        d=EditSettings(self.top, setting)
        self.top.wait_window(d.top)

class EditAccount:#DONEDONEDONE
    def __init__(self, parent,account):
        """Edit an account selected before calling this class
        User cannot directly edit the account type.  To change the account type
        you must delete this account and create a new one."""
        self.value_list=[]
        self.account=account
        top=self.top=Toplevel(parent)
        Label(top, text="Editing Account Information").grid(column=0, row=0, columnspan=2,sticky='ew')
        self.value_list = []
        row=1
        for k,v in accountsdict[self.account].iteritems():
            var=StringVar()
            var.set(v)
            if k=='disabled':
                x=Checkbutton(self.top, text='Disabled', onvalue='true', offvalue='false',variable=var).grid(row=row,column=0, columnspan=2, sticky='ew')
            else:
                Label(self.top, text=k).grid(row=row, column=0,sticky='ew')
                if k=='type':
                    Entry(self.top, textvariable=var, state=DISABLED).grid(row=row, column=1,sticky='ew')
                elif k=='password':
                    Entry(self.top, textvariable=var, show='*').grid(row=row, column=1, sticky='ew')
                else:
                    Entry(self.top, textvariable=var).grid(row=row, column=1,sticky='ew')

            row+=1
            self.value_list.append((k,var))
        Button(self.top, text='Save Settings',command=self.save_changes).grid(row=row+1, column=0, sticky='ew')
        Button(self.top, text="Cancel Changes", command=lambda: self.top.destroy()).grid(row=row+1, column=1, sticky='ew')

    def save_changes(self):
        for i in self.value_list:
            if i[0]=='password':
                accountsdict[self.account]['password']=i[1].get()
            elif i[0]=='disabled':
                accountsdict[self.account]['disabled']=i[1].get()
            elif i[0]=='retries':
                accountsdict[self.account]['retries']=i[1].get()
            elif i[0]=='live':
                accountsdict[self.account]['type']=i[1].get()
        self.top.destroy()

class SelectAccountEdit:
    def __init__(self, parent):
        top=self.top=Toplevel(parent)
        Label(top, text="Select An Account To Edit").grid(column=0, row=0, columnspan=2)
        self.accounts=Listbox(top)
        for k in accountsdict.keys():
            self.accounts.insert(END, k)
        self.ok=Button(top, text='Select',command=self.select)
        self.delete=Button(top, text='Delete Selected', command=self.deleteAct)
        self.done=Button(top, text='Done',command=self.top.destroy)
        self.ok.grid(column=0,row=4,sticky='ew')
        self.delete.grid(column=0, row=5, columnspan=2, sticky='ew')
        self.done.grid(column=1, row=4,sticky='ew')
        self.accounts.grid(column=0, row=1, columnspan=2, rowspan=3, sticky='ew')

    def deleteAct(self):
        x=response=tkMessageBox.askokcancel("Deletion Confirmation","Are you sure you would like to delete this account?")
        if x:
            acnt=self.accounts.get(self.accounts.curselection())
            accountsdict.pop(acnt)
            sol=tkMessageBox.askokcancel('Continue Editing?','Would you like to continue editing?')
            if sol:
                self.accounts.destroy()
                self.accounts=Listbox(self.top)
                for k in accountsdict.keys():
                    self.accounts.insert(END, k)
                self.accounts.grid(column=0, row=1, rowspan=3, columnspan=2)
                self.accounts.focus_set()
            else:
                self.top.destroy()

    def select(self):
        acnt=self.accounts.get(self.accounts.curselection())
        d=EditAccount(self.top, acnt)
        self.top.wait_window(d.top)

class AddAccountWindow:
    def __init__(self, parent):
        top=self.top=Toplevel(parent)
        Label(top, text="Enter New Login Information").grid(column=0, row=0, columnspan=2)
        Label(top, text="Username", width=15).grid(column=0, row=1)
        self.username=Entry(top, width=25)
        self.username.grid(column=1, row=1)
        Label(top, text="Password", width=15).grid(column=0, row=2)
        self.password=Entry(top, width=25, show='*')
        self.password.grid(column=1, row=2)
        self.acttype=Spinbox(top, values=('live','FB'), width=23)
        self.acttype.grid(column=1, row=3)
        self.f=Label(top, text='Site', width=15).grid(column=0, row=3)
        self.var=StringVar()
        self.disabled=Checkbutton(top, text='Start Disabled', onvalue='true', offvalue='false', variable=self.var)
        self.disabled.grid(column=0, row=4, columnspan=2)
        self.retries=Spinbox(top, values=range(1,11), width=23)
        self.rt=Label(top, text='Retries', width=25)
        b = Button(top, text="Save Account", command=self.ADDLogin)
        b.grid(column=0, row=6, columnspan=1, sticky='ew')
        c=Button(top, text="Cancel",command=self.top.destroy)
        c.grid(column=2, row=6,columnspan=1,sticky='ew')
        self.adv=Button(top, text="Show Advanced",command=self.advanced)
        self.adv.grid(column=1, row=6,columnspan=1,sticky='ew')
        self.noadv=Button(top, text="Hide Advanced", command=self.hideadv)

    def advanced(self):
        self.rt.grid(column=0,row=5,sticky='ew')
        self.retries.grid(column=1, row=5, sticky='ew')
        self.adv.grid_remove()
        self.noadv.grid(column=1, row=6, columnspan=1, sticky='ew')

    def hideadv(self):
        self.rt.grid_remove()
        self.retries.grid_remove()
        self.adv.grid()
        self.noadv.grid_remove()

    def ADDLogin(self):
        self.getentries()
        result=tkMessageBox.askyesno("Create A New Record", 'Would you like to create another login?')
        if result:
            self.ADDNew()
        else:
            self.top.destroy()

    def ADDNew(self):
        self.username.delete(0,END)
        self.password.delete(0,END)
        self.disabled.deselect()
        self.username.focus_set()

    def getentries(self):
        pword=self.password.get()
        uname=self.username.get()
        disabled=self.var.get()
        retries=self.retries.get()
        acttype=self.acttype.get()
        accountsdict[uname]={'password':pword,'disabled':disabled, 'retries':retries, 'type':acttype}

class BingConfig:
    def __init__(self,configfile=os.path.join(os.getcwd(), 'config.xml')):
        self.startGUI()

    def startGUI(self):
        self.root=Tk()
        self.root.title('ABRAhaM Configuration')
        self.status=Label(self.root, text='...Waiting for input...', bg='black',fg='yellow', width=100)
        self.addactbtn=Button(self.root, text='Add Account', width=50, command=self.addact)
        self.editactbtn=Button(self.root, text='Edit Account', width=50,state=DISABLED, command=self.editact)
        self.addsetbtn=Button(self.root, text='Add Preference',width=50, command=self.addset)
        self.editsetbtn=Button(self.root, text='Edit Preferences',width=50,state=DISABLED, command=self.editset)
        self.savebtn=Button(self.root, text='Save',width=50, command=self.save)
        self.cancelbtn=Button(self.root,text="Done",width=50, command=self.exit)
        Label(self.root, text="Please Select an Action to Perform", foreground='red',background='black').grid(column=0, row=0, columnspan=2, sticky='ew')


        #Build the GUI
        self.status.grid(column=0,row=5,columnspan=2)
        self.addactbtn.grid(column=0,row=2)
        self.editactbtn.grid(column=0,row=3)
        self.editsetbtn.grid(column=1,row=3)
        self.addsetbtn.grid(column=1,row=2)
        self.savebtn.grid(column=0,row=4)
        self.cancelbtn.grid(column=1,row=4)

        mainloop()

    def save(self):
        self.status['text']='Saving Written Data to file...'
        #Save all configuration settings to config.xml (or user defined name)
        #Need to call up the configfile class here and initiate the save function
        pass

    def exit(self):
        self.status['text']='Program Exiting'
        self.root.destroy()
        sys.exit()

    def addact(self):
        """Opens the add account popup for creating a new login account"""
        self.status['text']='Running Add Accounts Dialog'
        d=AddAccountWindow(self.root)
        self.root.wait_window(d.top)
        self.update()

    def editact(self):
        self.status['text']='Running Edit Account Dialog'
        d=SelectAccountEdit(self.root)
        self.root.wait_window(d.top)
        self.update()

    def update(self):
        """Controls making buttons active/disabled during script run."""
        self.status['text']='...Updating Window...'
        if self.editactbtn['state']==DISABLED and len(accountsdict.keys())>0:
            self.editactbtn['state']=ACTIVE
        if self.editsetbtn['state']==DISABLED and len(settingsdict.keys())>0:
            self.editsetbtn['state']=ACTIVE
        self.status['text']='...Waiting for input...'

    def editset(self):
        self.status['text']='Running EDIT SETTINGS dialog...'
        d=EditSettings(self.root)
        self.root.wait_window(d.top)
        self.update()
        self.status['text']='...Waiting for input...'

    def addset(self):
        self.status['text']='Running ADD SETTINGS dialog...'
        d=AddSettings(self.root)
        self.root.wait_window(d.top)
        self.update()
        self.status['text']='...Waiting for input...'


#This is just for testing purposes.  The actions in this script will be imported by the main script
BingConfig()
