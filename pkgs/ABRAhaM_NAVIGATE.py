#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
# Author:      Amazingred
# Created:     1352042914
#-------------------------------------------------------------------------------
import urllib, mechanize, cookielib, re, random, HTMLParser, gzip, zlib, StringIO
import ABRAhaM_DOC as ad

def getResponseBody(response):
    """ Returns response.read(), but does gzip deflate if appropriate.
    Kredit Sergey Markelov"""
    encoding = response.info().get("Content-Encoding")
    if encoding in ("gzip", "x-gzip", "deflate"):
        page = response.read()
        if encoding == "deflate":
            return zlib.decompress(page)
        else:
            fd = StringIO.StringIO(page)
            try:
                data = gzip.GzipFile(fileobj = fd)
                try:     content = data.read()
                finally: data.close()
            finally:
                fd.close()
            return content
    else:
        return response.read()

class HTMLFormInputsParser(HTMLParser.HTMLParser):
    """Kredit Sergey Markelov"""
    def __init__(self):
        HTMLParser.HTMLParser.__init__(self)
        self.inputs = {}

    def handle_starttag(self, tag, attrs):
        if tag == 'input':
            name = value = ''
            for attr in attrs:
                if attr[0] == 'name':
                    name = attr[1]
                elif attr[0] == 'value':
                    value = attr[1]
            if name != '' and value != '':
                self.inputs[name] = value.encode("utf-8")

class Bing:
    def __init__(self, username, password, logintype, searchsalt, searchdelay,retries):
        self.br=mechanize.Browser()
        cj=cookielib.LWPCookieJar()
        self.br.set_cookiejar(cj)
        self.br.set_handle_robots(False)
        self.br.open(ad.burl)
        if logintype.lower()=='live':
            self._LiveAuth(username, password)
        elif logintype.lower()=='fb':
            self._FBAuth(username,password)

    def _LiveAuth(self,username,password):
        """Logs into BingRewards with your Live Account
        Method of bing login adapted from BingRewards Script
        created by Sergey Markelov."""

        self.br.open(re.compile('WindowsLiveId\":\"[\S]+Facebook').search(self.br.response().read()).group()[16:-11].decode('string-escape'))
        html=self.br.response().read()

        #Get Login Parameters from webpage
        ppft=re.compile(r'value="(.*)"/').search(html).group()[7:-2]#PPFT
        ppsx=re.compile(r',g:(.*),h').search(html).group()[3:-2]#PPSX parameter
        sso=re.compile(r',W:(.*),aC').search(html).group()[3:-3]#SSO
        post=re.compile(r',urlPost:\'(.*)\',html').search(html).group()[10:-6]#PostURL
        RT=int(130+random.uniform(0,100))#renderTime

        #Encoded Data
        pagedata=urllib.urlencode({"login":username,"passwd":password,"SI":"Sign in","type":"11","PPFT":ppft,"PPSX":ppsx,"idsbho":"1","LoginOptions":"3","sso":sso,"NewUser":"1","i1":"0","i2":"1","i3":str(int(20000+random.uniform(0,1000))),"i4":"0","i7":"0","i12":"1","i13":"0","i14":str(RT),"i15":str(RT+int(random.uniform(2,5))),"i16":str(int(870+random.uniform(0,250))),"i17":"0","i18":"__Login_Strings|1,__Login_Core|1,"})

        self.br.open(post, pagedata)
        html=getResponseBody(self.br.response())
        strt=re.search("<form ", html).span()[1]
        end=re.search("</form>", html[strt:]).span()[0]+strt
        parser = HTMLFormInputsParser()
        parser.feed(html[strt:end].decode('utf-8'))
        parser.close()
        postfields=urllib.urlencode(parser.inputs)
        self.br.open(ad.purl, postfields)

#This is just for testing purposes.  This script will normally be called by the main script
Bing('XXXXX','XXXXX','live','3','5','3')
