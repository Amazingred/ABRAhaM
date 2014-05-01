#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
# Author:      Amazingred
# Created:     1352042914
#-------------------------------------------------------------------------------
import urllib, urllib2, mechanize, cookielib, re, os, sys
from selenium import webdriver
from BeautifulSoup import BeautifulSoup
import ABRAhaM_DOC as abedocs

class Bing:
    def __init__(self):
        self._LiveAuth('XXXXX','XXXXX')
        self.getAccountInformation()

    def _LiveAuth(self,username,password):
        """Logs into BingRewards with your Live Account
        using the Selenium Webbrowser."""
        self.br=webdriver.Firefox()
        self.br.implicitly_wait(30)
        self.br.get('http://www.bing.com')
        self.br.find_element_by_id('id_a').click()
        self.br.find_element_by_link_text("Connect").click()
        self.br.find_element_by_name('login').send_keys(username)
        self.br.find_element_by_name('passwd').send_keys(password)
        self.br.find_element_by_name('KMSI').click()
        self.br.find_element_by_name('SI').click()
        alert = self.br.switch_to_alert()
        alert.accept()

    def getAccountInformation(self):
        """Retrieves points history, bonus offers, point balance, and other
        rewards information about the currently selected account and saves it
        for logging and reference later on in the program."""
        self.br.get('http://www.bing.com/rewards/dashboard')
        creditsavail=self.br.find_element_by_class_name('credits-left').text
        lifetimecreds=self.br.find_element_by_class_name('credits-right').text
        level=self.br.find_element_by_class_name('level-right').text

        #The following have not been tested:
        offers=self.br.find_elements_by_class_name('li')


if __name__ == '__main__':
    b=Bing()
