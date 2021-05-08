# covin-notification

This Script notify you once the vaccination available at your place(given by you as input)

# Why I Implement This 

Since I got furstrated trying to schedule a vaccination for me and my family from past 2-3 weeks.


### Prerequisites
python-3
lil-bit technical knowledge

## Running the tests

1) Comment below lines
  r = requests.get(URL)
  data = r.json()
2) Now uncomment for testing
  f = open('test.json', )
  data = json.load(f)
  
3) now go to your shell and type "python covin.py"
    this will ask for some inputs from user, Please provide and you are good to go.
    
## For real time consumption of covin APIs 

1) unComment below lines
  r = requests.get(URL)
  data = r.json()
2) Now comment for testing
  f = open('test.json', )
  data = json.load(f)
  
3) now go to your shell and type "python covin.py"
    this will ask for some inputs from user, Please provide and you are good to go.

## If something breaks:

If you are getting an error like " (535, b'5.7.8 Username and Password not accepte
d. Learn more at\n5.7.8 http://support.google.com/mail/bin/answer.py?answer=1425
7\n5.7.8 {BADCREDENTIALS} s10sm9426107qam.7 - gsmtp')"

go to https://www.google.com/settings/security/lesssecureapps and allow less secure account{better if we can use a separate account for security purpose}
