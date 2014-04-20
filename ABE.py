#-------------------------------------------------------------------------------
# Project Name:        A.B.R.A.(ha)M.
# File Name:           ABE.py
# Purpose:             Automatic Bing Rewards Account Manager
# Author:              Amazingred
# Version:             1.0
# Created:             1158030914
#-------------------------------------------------------------------------------
import sys, re, os, mechanize, urllib, urllib2, cookielib,getopt
import xml.etree as et
from Tkinter import *
sys.path.append(os.path.join(os.path.dirname(__file__), "pkgs"))
import ABRAhaM_DOC as abedocs
import ABRAhaM_NAVIGATE as abenav
import ABRAhaM_CONFIGUI as configui
import ABRAhaM_CONFIG as abeconfig

if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:], "chf:rvis:", ["configure", "help", "configfile=", "full-report", "verbose","info"])
    except getopt.GetoptError, e:
        print "getopt.GetoptError: %s" % e
        print abedocs.usage
        sys.exit(1)

    for i in ['pkgs','logs','results']:
        if not os.path.exists(os.path.join(os.path.dirname(__file__),i)):
            os.makedirs(os.path.join(os.path.dirname(__file__),i))

    configFile = os.path.join(os.path.dirname(__file__), "pkgs","config.xml")
    for o, a in opts:
        if o in ("-c","--configure") or os.path.exists(os.path.join(os.path.dirname(__file__),'pkgs','config.xml'))==False:
            cfg=configui.ConfigGUI('Started from Command Line')
        if o in ("-h", "--help"):
            abedocs.usage
            sys.exit(1)
        elif o in ("-f", "--configFile"):
            configFile = a
        elif o in ("-v", "--verbose"):
            verbose = True
        elif o == "--version":
            abedocs.VERSION()
            sys.exit()
        else:
            raise NotImplementedError("option '" + o + "' is not implemented")
##    print "%s - script started" % helpers.getLoggingTime()
##    print "-" * 80
##    print

##    helpers.createResultsDir(__file__)

##    config = Config()
##
##    try:
##        config.parseFromFile(configFile)
##    except IOError, e:
##        print "IOError: %s" % e
##        sys.exit(2)
##    except ConfigError, e:
##        print "ConfigError: %s" % e
##        sys.exit(2)
##
##    try:
##        __run(config)
##    except BaseException, e:
##        EventsProcessor.onScriptFailure(config, e)

##import ABRAhaM_DOC as AbeDocs
##import re, sys, mechanize, cookielib, urllib, urllib2, os, getopt
##import ABRAhaM_CONFIG as Abeconfig
##import ABRAhaM_CONFIGUI as CONFIGUI
##import ABRAhaM_NAVIGATE as Abenav
##class Manager:
##    def __init__(self):
##        self.checksetup()
##
##    def checksetup(self):
##        master=CONFIGUI.ConfigGUI("Regular Execution")
##
##
##
##class BingAuth:
##    pass
##
##class AccountDetails:
##    pass
##
##class QueryGenerator:
##    pass
##
##class RunMonitor:
##    pass
##
##class ErrorHandling:
##    pass
##
##class LogManager:
##    pass
##
##if __name__ == '__main__':
##    m=Manager()
##    try:
##        opts, args = getopt.getopt(sys.argv[1:], "hf:rv", ["help", "configFile=", "verbose", "version"])
##    except getopt.GetoptError, e:
##        print "getopt.GetoptError: %s" % e
##        abedocs.USAGE()
##        sys.exit(1)
##
##    configFile = os.path.join(os.path.dirname(__file__), "config.xml")
##    for o, a in opts:
##        if o in ("-h", "--help"):
##            abedocs.USAGE()
##            sys.exit()
##        elif o in ("-f", "--configFile"):
##            configFile = a
##        elif o in ("-v", "--verbose"):
##            verbose = True
##        elif o == "--version":
##            abedocs.VERSION()
##            sys.exit()
##        else:
##            raise NotImplementedError("option '" + o + "' is not implemented")
##    print "%s - script started" % helpers.getLoggingTime()
##    print "-" * 80
##    print
##
##    helpers.createResultsDir(__file__)
##
##    config = Config()
##
##    try:
##        config.parseFromFile(configFile)
##    except IOError, e:
##        print "IOError: %s" % e
##        sys.exit(2)
##    except ConfigError, e:
##        print "ConfigError: %s" % e
##        sys.exit(2)
##
##    try:
##        __run(config)
##    except BaseException, e:
##        EventsProcessor.onScriptFailure(config, e)
