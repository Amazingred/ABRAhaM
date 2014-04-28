#-------------------------------------------------------------------------------
# Name:        ABRAhaM_CONFIGUI
# Purpose:     Configuration Operations and CONFIG GUI
# Author:      Amazingred
# Created:     1223032414
#-------------------------------------------------------------------------------
import sys, re, os, tkMessageBox
import xml.dom.minidom as minidom
from Tkinter import *
import xml.etree.ElementTree as et
import ABRAhaM_DOC as abedocs

#These are the holders of all of the configuration data for the script
accountsdict=dict()
settingsdict=dict()

class ConfigFile:
    """Handles all operations dealing with the configuration file itself.
    Reading, loading variables from the content, and saving are all handled here."""
    def __init__(self, configfile):
        self.configfile=configfile
    def read_config_file(self):
        root=Tk()
        root.withdraw()
        if not os.path.exists(self.configfile):
            if not tkMessageBox.askyesno('ERROR',abedocs.ErrorMessages(101)):
                tkMessageBox.showerror('PROGRAM EXITING', abedocs.ErrorMessages(103))
                sys.exit(1)
        else:
            try:
                xmlroot=et.parse(self.configfile).getroot()
                xmlacnts=xmlroot.find('Accounts')
                for acnt in xmlacnts.getchildren():
                    acntname=acnt.attrib['email']
                    password=acnt.find('password').text
                    disabled=acnt.find('disabled').text
                    retries=acnt.find('retries').text
                    acttype=acnt.find('type').text
                    accountsdict[acntname]={'password':password,'disabled':disabled, 'retries':retries, 'type':acttype}
                xmlpreferences=xmlroot.find('Preferences')
                for preference in xmlpreferences.getchildren():
                    settingsdict[preference.tag]=preference.text
            except:
                if not tkMessageBox.askyesno('ERROR',abedocs.ErrorMessages(102)):
                    tkMessageBox.showerror('PROGRAM EXITING', abedocs.ErrorMessages(103))
                    sys.exit(1)

    def save_config_file(self):
        xmlroot=et.Element('Configure')
        xmlacnts=et.SubElement(xmlroot, 'Accounts')
        xmlpreferences=et.SubElement(xmlroot,'Preferences')
        for k,v in settingsdict.iteritems():
            x=et.SubElement(xmlpreferences,k)
            x.text=v
        for node in accountsdict.keys():
            x=et.SubElement(xmlacnts, 'account', {'email':node})
            for child,value in accountsdict[node].iteritems():
                head=et.SubElement(x, child)
                head.text=value
        f=open(self.configfile, 'w')
        f.write(self.prettify(xmlroot))
        f.close()

    def prettify(self,elem):
        """Return a pretty-printed XML string for the Element.  Props goes
        to Maxime from stackoverflow for this code."""
        rough_string = et.tostring(elem, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        return reparsed.toprettyxml(indent="\t")

class AddSettings:
    def __init__(self, parent):
        top=self.top=Toplevel(parent)
        Label(top, text="Add Settings Dialog").grid(column=0, row=0, columnspan=2,sticky='ew')
        self.SettingName=Entry(top,width=25)
        self.SettingValue=Entry(top, width=25)
        Label(top, text='Setting Key', background='blue', foreground='yellow').grid(column=0, row=1, sticky='ew')
        Label(top, text='Setting Value', background='blue',foreground='yellow').grid(column=1, row=1, sticky='ew')
        Label(top, text="Add A New Program Setting").grid(column=0, row=0, columnspan=2, sticky='ew')
        self.SettingName.grid(column=0, row=2, sticky='ew')
        self.SettingValue.grid(column=1, row=2, sticky='ew')
        Button(top, text='Save Setting', command=self.savesetting).grid(column=0, row=3, sticky='ew')
        Button(top, text='Cancel', command=self.top.destroy).grid(column=1, row=3, sticky='ew')

    def savesetting(self):
        settingsdict[self.SettingName.get()]=self.SettingValue.get()
        if tkMessageBox.askyesno('Create Another', 'Would you like to create another setting?'):
            self.SettingName.delete(0,END)
            self.SettingValue.delete(0,END)
            self.SettingName.focus_set()
        else:
            self.top.destroy()

class EditSettings:
    def __init__(self, parent,setting,value):
        """Edit a setting selected before calling this class."""
        top=self.top=Toplevel(parent)
        Label(top, text="Editing Selected Setting").grid(column=0, row=0, columnspan=2,sticky='ew')
        self.var=StringVar()
        self.var1=StringVar()
        self.var.set(setting)
        self.var1.set(value)
        K=Entry(top, textvariable=self.var, width=25).grid(column=0, row=2, sticky='ew')
        V=Entry(top, textvariable=self.var1, width=25).grid(column=1, row=2, sticky='ew')
        Label(top, text='Setting Key', width=25).grid(column=0, row=1, sticky='ew')
        Label(top, text='Setting Value', width=25).grid(column=1, row=1, sticky='ew')

        Button(self.top, text='Save Settings',command=self.save_changes).grid(row=3, column=0, sticky='ew')
        Button(self.top, text="Cancel Changes", command=lambda: self.top.destroy()).grid(row=3, column=1, sticky='ew')

    def save_changes(self):
        k=self.var.get()
        v=self.var1.get()
        settingsdict[k]=v
        self.top.destroy()

class SelectSettingEdit:
    def __init__(self, parent):
        top=self.top=Toplevel(parent)
        Label(top, text="Select A Setting To Edit").grid(column=0, row=0, columnspan=2)
        self.settings=Listbox(top, width=50, takefocus=True)
        for k,v in settingsdict.items():
            self.settings.insert(END, str(k)+'__'+str(v))
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
            self.settings.destroy()
            self.settings=Listbox(self.top)
            for k in settingsdict.keys():
                self.settings.insert(END, k)
            self.settings.grid(column=0, row=1, rowspan=3, columnspan=2)
            self.settings.focus_set()

    def select(self):
        setting=self.settings.get(self.settings.curselection()).split('__')
        d=EditSettings(self.top, setting[0],setting[1])
        self.top.wait_window(d.top)

class EditAccount:
    def __init__(self, parent,account):
        """Edit an account selected before calling this class
        User cannot directly edit the account type.  To change the account type
        you must delete this account and create a new one."""
        self.value_list=[]
        self.account=account
        top=self.top=Toplevel(parent)
        Label(top, text="Editing Account Information").grid(column=0, row=0, columnspan=2,sticky='ew')
        row=1
        for k,v in accountsdict[self.account].iteritems():
            self.var=StringVar()
            self.var.set(v)
            if k=='disabled':
                x=Checkbutton(self.top, text='Disabled', onvalue='True', offvalue='False',variable=self.var).grid(row=row,column=0, columnspan=2, sticky='ew')
            else:
                Label(self.top, text=k).grid(row=row, column=0,sticky='ew')
                Entry(self.top, textvariable=self.var).grid(row=row, column=1,sticky='ew')

            row+=1
            self.value_list.append((k,self.var))
        Button(self.top, text='Save Settings',command=lambda: self.save_changes()).grid(row=row+1, column=0, sticky='ew')
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
    """Manages the selection of an account to edit"""
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
        """Verifies intent and removes an account entry completely"""
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
        """Picks the highlighted entry and passes it into the editor"""
        acnt=self.accounts.get(self.accounts.curselection())
        d=EditAccount(self.top, acnt)
        self.top.wait_window(d.top)

class AddAccountWindow:
    """Manages the Add Account operations"""
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
        self.disabled=Checkbutton(top, text='Start Disabled', onvalue='True', offvalue='False', variable=self.var)
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
        """Shows the advanced settings"""
        self.rt.grid(column=0,row=5,sticky='ew')
        self.retries.grid(column=1, row=5, sticky='ew')
        self.adv.grid_remove()
        self.noadv.grid(column=1, row=6, columnspan=1, sticky='ew')

    def hideadv(self):
        """Hides the advanced settings"""
        self.rt.grid_remove()
        self.retries.grid_remove()
        self.adv.grid()
        self.noadv.grid_remove()

    def ADDLogin(self):
        """Adds entries and asks if a new record should be created"""
        self.getentries()
        result=tkMessageBox.askyesno("Create A New Record", 'Would you like to create another login?')
        if result:
            self.ADDNew()
        else:
            self.top.destroy()

    def ADDNew(self):
        """Resets the window with empty entry boxes for a new record"""
        self.username.delete(0,END)
        self.password.delete(0,END)
        self.disabled.deselect()
        self.username.focus_set()

    def getentries(self):
        """Retrieves entries from window and saves them into the dictionary"""
        pword=self.password.get()
        uname=self.username.get()
        disabled=self.var.get()
        retries=self.retries.get()
        acttype=self.acttype.get()
        accountsdict[uname]={'password':pword,'disabled':disabled, 'retries':retries, 'type':acttype}

class BingConfig:
    """Main Configuration Script Manager"""
    def __init__(self,configfile=os.path.join(os.getcwd(), 'config.xml')):
        self.configfile=configfile
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
        self.update()
        if tkMessageBox.askyesnocancel('Load Configuration Data', 'Would you like to load the data from the configuration file?'):
            self.status['text']='Reading and loading saved configuration data...'
            self.cfg=ConfigFile(self.configfile)
            self.cfg.read_config_file()
            self.update()
            self.status['text']='Configuration data loaded...waiting for input...'
        mainloop()

    def save(self):
        """Saves the configuration data to file"""
        self.status['text']='Saving Written Data to file...'
        self.cfg.save_config_file()
        self.exit()

    def exit(self):
        self.status['text']='Program Exiting'
        if tkMessageBox.askyesno("Save?", 'Would you like to save before you exit?  Any usaved data will be LOST.'):
            self.status['text']='Filesaving operations starting....'
            self.save()
        self.root.destroy()
        sys.exit()

    def addact(self):
        """Opens the add account popup for creating a new login account"""
        self.status['text']='Running Add Accounts Dialog'
        d=AddAccountWindow(self.root)
        self.root.wait_window(d.top)
        self.update()

    def editact(self):
        """Loads in the saved accounts for editing"""
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
        d=SelectSettingEdit(self.root)
        self.root.wait_window(d.top)
        self.update()
        self.status['text']='...Dialog completed...Waiting for input...'

    def addset(self):
        self.status['text']='Running ADD SETTINGS dialog...'
        d=AddSettings(self.root)
        self.root.wait_window(d.top)
        self.update()
        self.status['text']='...Dialog completed...Waiting for input...'

#This is just for testing purposes.  The actions in this script will be imported by the main script
BingConfig()