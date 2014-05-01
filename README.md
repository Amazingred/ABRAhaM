ABRAhaM
=======

Automatic Bing! Rewards Accounts Manager

ABRAhaM is a script that automates BING Rewards account daily searches, mobile logins,
and other bonus tasks each day to get the max free daily bing rewards points.  These points
can be used to purchase items like Amazon.com gift cards, Pizza gift cards, music downloads, 
drawings for bigger prizes, and much more.  Getting max points on many accounts adds up VERY 
quickly to make this very profitable.  This code is meant to be a true STAND ALONE....
as in it will run even if you arent home.....

Much kredit goes out to sealmar's BingRewards method of authenticating logins using python on bing.com since bing's login code is js based rendering accessing and submitting with python very difficult.  I've used his authentication method for logging in. His BingRewards script is located  His active code is located [HERE](https://github.com/sealemar/BingRewards "Bing Rewards Repo").

I'll be updating the Version.txt file soon to show the updates, modifications, and additions I've done. 
Perhaps the most noticeable differences at first will be the handling of the program configuration and 
preferences in ABRAhaM are managed by a multi-function GUI interface.  Creating and managing logins and
preferences are much easier.  Also there are 2 different navigation modes in ABRAhaM.  one using mechanize instead of the urllib2 Opener and a second using the Selenium Webdriver.  (both have a function for being included.  Read the docs for more information).  Both of which are coded to operate when the situation calls for them or you can use a command line arg to specify using one or the other as the sole navigator.  

Check the version.txt and help docs when they become availible for a full list of changes and features.

                                    AMAZINGRED