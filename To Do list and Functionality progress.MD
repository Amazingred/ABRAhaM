PENDING TODO LIST BY SCRIPT

CONFIGUI.PY
    THIS SCRIPT IS IN THE TESTING AND DEBUGGING PHASE
    ALTHOUGH THERE ARE SEVERAL SMALLER FEATURES I WILL BE ADDING, THE MAIN FUNCTIONALITY IS DONE

	*Add a saved file checker operation that will check to see if the data has been saved to file upon attempting to exit
	*Add a configuration file archive/backup scheme so that I can automatically store previous versions of the config file whenever a new file is being saved in case of a need to rollback.
	*Change the password values from shown to hidden in the accounts editor.
	*Consider adding confirmation boxes upon changing account or preference settings.
	*ALWAYS insert self.status message updates EVERYWHERE in the script when the operation changes

ABRAhaM_DOC.py
    *Update the vital storage information (i.e version, date, url, bingpage, usage, helpmessage, etc)
    *Transfer over all of the text identifiers from the configui script and call them via the abedocs (soon to be docs) operation.  This should unclutter the configui script a lot!


PROGRAM FUNCTIONALITY CHECKLIST BY SCRIPT
note: only scripts that are complete, or those currently being coded will be included so far...

CONFIGUI.py
    a. Add Accounts Dialog --------------DONE
    b. EDIT Accounts Dialog -------------DONE
    c. Add Settings Dialog  -------------DONE
    d. Edit Settings Dialog -------------DONE
    e. Save Button Operations -----------DONE
    f. Done Button Operations -----------DONE
    g. ConfigFile read variables --------DONE
    h. ConfigFile pretty save varialbes--DONE
    i. Status Display messages evrwhr----INCOMPLETE
    j. Debugging                 -------- IN DEBUGGING PHASE!!!

ABRAhaM_DOCS.py
    a. Error Message Storeage for all scripts ------DONE
    b. Usage message to display in console----------DONE
    c. About Message to display on request----------DONE <---check this one to be sure
    d. Browser headers/Version/Editdate/website/url-DONE
    e. Storage of all Configui.py status, error, and info messages----INCOMPLETE

ABRAhaM_NAVIGATE.py
    a. Successfull interaction and valid verification with bing rewards account interface ----- PARTIALLY DONE, STILL NEED TO STUDY THE CODE TO UNDERSTAND IT BETTER
    b. remember that configuration data and preferences will be handled by the main script so by the time the code gets here most of the tweaks should already be defined and assigned.
    c. perform navigation to the initial page, login pages, search page, queries finder pages, etc
    d. perform navigation to gather informatino about the user account to save in the logs and output

ABRAhaM_QUERIES.py
    a. NO OPERATIONS DEFINED AS OF YET.  FUTURE PROJECT

ABRAhaM_MONITOR.py
    a. NO OPERATIONS DEFINED AS OF YET.  FUTURE PROJECT
    b. NOTE: this will handle the logging, verbose level, reports, filesaving, points tracking, bonus tracking, timers, etc....

ABRAhaM_Main.py
    a. NO OPERATIONS AS OF YET.  
