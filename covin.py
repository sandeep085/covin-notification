import sched, time, requests, json, datetime, smtplib, ssl, email

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

s = sched.scheduler(time.time, time.sleep)
senderEmail = input("Type your email and press enter: ")
password = input("Type your password and press enter: ")
receiverEmail = input("Type receiver email and press enter: ")
bcc = input("Type Bcc email and press enter: ")
pinCode = input("Type pincode of the place you want to schedule for and press enter: ")
maxDaysThresholdDays = input("Type(must be numeric) till how many days starting from now you want to crawl for and press enter: ")
waitTime = input("Type wait time for each execution in seconds(numeric and must be greater than 1 min i.e 60 seconds) and press enter: ")

waitSeconds = int(waitTime)
print(waitSeconds)
if waitSeconds < 60:
        print("Since waitTime is less then 60 seconds , resetting it to 60 secs ")
        waitSeconds = 60


def sendMail(mailContent):
        port = 465  # For SSL
        message = MIMEMultipart()
        message["From"] = senderEmail
        message["To"] = receiverEmail
        message["Subject"] = "CoWin Availablity"
        message["Bcc"] = bcc  # Recommended for mass emails
        # Add body to email
        message.attach(MIMEText(mailContent, "plain"))
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
                try:
                        server.login(senderEmail, password)
                        server.sendmail(senderEmail, receiverEmail, message.as_string())
                        print("Email Sent "+mailContent)
                except Exception as e:
                        # Print any error messages to stdout
                        print(e)
                finally:
                        server.quit()


def execute(sc):
        print("Doing stuff...")
        now = datetime.datetime.now()
        # Currently I just want to run this logic b/w 7 AM to 7 P.M, Modify accordingly
        if (now.hour <7 or now.hour >18):
                print("Not a suitable execution time, Please try this script b/w & A.M to & P.M else modify the limits")
                return

        currDate = datetime.datetime.today().strftime('%d-%m-%Y')
        maxDaysThreshold = datetime.timedelta(int(maxDaysThresholdDays))
        maxDate = datetime.datetime.today() + maxDaysThreshold
        delta = datetime.timedelta(days=1)
        startDate = datetime.datetime.strptime(currDate, '%d-%m-%Y')
        while startDate <= maxDate:
                dateString = startDate.strftime('%d-%m-%Y')
                URL = "https://www.cowin.gov.in/api/v2/appointment/sessions/public/calendarByPin?pincode="+pinCode+"&date=" + dateString
                print(URL)
                startDate += delta
                # For Testing Only
               # f = open('test.json', )
               # data = json.load(f)
                #Real Hit
                r = requests.get(URL)
                data = r.json()
                print("Response DATA : " + str(data))
                messageContent = ""
                for key in data:
                        value = data[key]
                        # print("The key and value are ({}) = ({})".format(key, value))
                        for k2 in value:
                                # print("Address and Sessions are ({}) = ({})".format(k2["address"], k2["sessions"]))
                                for ss in k2["sessions"]:
                                        # print("Address and Sessions are ({}) = ({})".format(ss["date"], ss["available_capacity"]))
                                        if ss["available_capacity"] > 0:
                                                messageContent =  messageContent+"\n"+"Vaccine available for date : {} at Address : {}  ,Available Quota  : {}".format(
                                                                ss["date"], k2["address"], ss["available_capacity"])

                if messageContent :
                        sendMail(messageContent)
                else :
                        print("Vaccine Not Available For Date : "+ dateString)
                s.enter(waitSeconds, 1, execute, (sc,))


s.enter(waitSeconds, 1, execute, (s,))
s.run()