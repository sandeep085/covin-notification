# covin-notification

This Script notify you once the vaccination available at your place(given by you as input)

# Why I Implement This 

I Just got stucked trying and trying to schedule a vaccination for me and my family from past 2-3 weeks.


### Prerequisites
python-3<br/>
lil-bit technical knowledge

## Running the tests

1) Comment below lines<br/>
  r = requests.get(URL)<br/>
  data = r.json()<br/>
2) Now uncomment for testing<br/>
  f = open('test.json', )<br/>
  data = json.load(f)<br/>
  
3) now go to your shell and type "python covin.py"<br/>
    this will ask for some inputs from user, Please provide and you are good to go.
    
## For real time consumption of covin APIs 

1) unComment below lines<br/>
  r = requests.get(URL)<br/>
  data = r.json()<br/>
2) Now comment for testing<br/>
  f = open('test.json', )<br/>
  data = json.load(f)<br/>
  
3) now go to your shell and type "python covin.py"
    this will ask for some inputs from user, Please provide and you are good to go.

## If something breaks:

If you are getting an error like<br/> " (535, b'5.7.8 Username and Password not accepte
d. Learn more at\n5.7.8 http://support.google.com/mail/bin/answer.py?answer=1425
7\n5.7.8 {BADCREDENTIALS} s10sm9426107qam.7 - gsmtp')"
<br/>
go to https://www.google.com/settings/security/lesssecureapps and allow less secure account{better if we can use a separate account for security purpose}
