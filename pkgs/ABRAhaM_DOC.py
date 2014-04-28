#-------------------------------------------------------------------------------
# Project Name:        A.B.R.A.(ha)M.
# File Name:           ABRAM_DOCS.py
# Purpose:             Contains all of the documentation and help texts
# Author:              Amazingred
# Version:             1.0
# Created:             1210030914
#-------------------------------------------------------------------------------
import os

website='http://dustinagee.wix.com/bastardapp'
Version='1.0'
EditDate='4/1/14'
bing_url='http://www.bing.com'
bing_headers={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-us,en;q=0.5",
    "Accept-Charset": "utf-8",
    "Accept-Encoding": "gzip, deflate",
    "Connection":"keep-alive"}

description="""
    \tDESCRIPTION

    A.B.R.A.(ha)M. - Automatic Bing Rewards Account Manager
    =======================================================

    ABRAhaM is a different approach to 'https://github.com/sealemar/BingRewards'
     which is Sergey Markelov's program that automates BING searches and other
    bonus tasks each day to get the max free daily bing rewards points.  These points
    can be used to purchase items from their store like gift cards or downloads.

    Sergey uses urllib2 to navigate and decode the complicated bing interface. Bing
    has had a history of being difficult for Python to easily interact with.  This
    version is my own adaptation of that code.  I've added/removed/changed a few
    things for my own personal comfortablility and i'm using his code mainly
    to help me get better at web page interaction with python.

    My hopes is that this will make adjusting to bing updates much easier, as well
    as making it simpler to add new features as they come along.

    We'll just have to see how well I do....\n\n\t\t\t\t\t\t\t\t\t\t\t\t\t\tAmazingred"""

usage="""
    Usage: ABE [options]

    Options:
        -c, --configure             launch the configuration editor
        -h, --help                  show this help
        -f, --configFile=file       use specific config file.  Default is config.xml
        -r, --full-report           force printing complete report at the end.
        -v, --verbose               print verbose output
        -i, --version               print version info"""

version="""
    Automatic Bing Rewards Account Manager script
    Website: %s.
    Version: %s
    Date: %s
    See 'version.txt' for the list of changes per version

    This code is published under LGPL v3 <http://www.gnu.org/licenses/lgpl-3.0.html>
    There is NO WARRANTY, to the extent permitted by law.
    USE AT YOUR OWN RISK and discretion.

    Original Code Developed by Sergey Markelov
    ABRAhaM Developed by Dustin Agee
    """%(website, Version, EditDate)

def ErrorMessages(errnum):
    """This will contain all of the error messages that the assorted parts
    of the program will display whenever something goes wrong.  Storing them here saves
    coding space and keeps the code a little less cluttered in the main script pages.
    It makes for easier viewing of the code itself if there isn't a lot of Message Text
    cluttering up the lines."""
    MessageDict={101:'Config file not found.  The filename does not appear to be valid or the path is not accessible.  Would you like to procede with an empty configuration file?',102:'There was an error reading data from the configuration file.  Either the file is corrupted or is saved in an unknown format.  Would you like to procede with an empty configuration file?',103:'Program cannot run until configuration data is read or new configuration data is created.  Program will now exit.'}
    return MessageDict[errnum]