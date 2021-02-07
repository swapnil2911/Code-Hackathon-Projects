from __future__ import print_function
import time
import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import os
import platform
from time import sleep
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def clearscreen():
    plt = platform.system()
    if plt == "Windows":
        os.system("cls")
    else:
        os.system("clear")


class bot:
    def __init__(self):
        # options = webdriver.ChromeOptions()
        # options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        # chrome_driver_binary = "C:\\Program Files (x86)\\chromedriver.exe"
        # self.driver = webdriver.Chrome(chrome_driver_binary, options=options)
        chrome_options = Options()
        chrome_options.add_argument("use-fake-ui-for-media-stream")
        self.driver = webdriver.Chrome(chrome_options=chrome_options)

    def login(self):
        self.driver.get('https://teams.microsoft.com/')
        sleep(2)

        loginuser = self.driver.find_element_by_id("i0116")
        loginuser.send_keys(
            "" + Keys.RETURN)  # Enter user email
        sleep(2)

        loginpass = self.driver.find_element_by_id("i0118")
        loginpass.send_keys("" + Keys.RETURN)  # Enter user password
        sleep(2)
        self.driver.find_element_by_id("idSIButton9").click()
        sleep(2)
        # self.driver.find_element_by_xpath(
        #     '/html/body/div/form/div[1]/div/div[1]/div[2]/div/div[2]/div/div[3]/div[2]/div/div/div[2]').click()

    def loadteam(self, team):
        while True:
            try:
                filterbtn = self.driver.find_element_by_xpath(
                    "//profile-picture[@title='"+team+"']")
                print("DONE LOADING, SELECTING TEAM NOW...")
                filterbtn.click()
                sleep(3)
                break
            except:
                print("TEAM STILL LOADING...")
                sleep(5)

    def checkchannel(self):
        sleep(35)

        count_of_channels = len(
            self.driver.find_elements_by_css_selector("div.name-channel-type"))
        channels = list(
            self.driver.find_elements_by_css_selector('a.channel-anchor'))
        flag = 0
        while True:
            if flag == 1:
                break
            for i in channels:
                i.click()
                try:
                    sleep(6)
                    joinbtn = self.driver.find_element_by_xpath(
                        '//*[@title="Join call with video"]')
                    joinbtn.click()
                    print("Meeting is available, joining now...")
                    sleep(5)
                    flag = 1
                    break
                except:
                    print("Checking another channel ")
                    sleep(5)
    # def waitformeeting(self):
    #     while True:
    #         try:
    #             joinbtn = self.driver.find_element_by_xpath(
    #                 '//*[@title="Join call with video"]')
    #             joinbtn.click()
    #             print("Meeting is available, joining now...")
    #             sleep(5)
    #             break
    #         except:
    #             sleep(10)
    #             print("Waiting for meeting to start...")

    def showparticipants(self):
        sleep(30)

        while True:
            try:
                participantsbtn = self.driver.find_element_by_xpath(
                    '//*[@id="roster-button"]')
                participantsbtn.click()
            except:
                actions = ActionChains(self.driver)
                actions.send_keys(Keys.TAB)
                actions.perform()
            else:
                break

    def checkparticipants(self):

        self.showparticipants()
        sleep(2)
        nbr = 0
        inmeeting = self.driver.find_element_by_xpath(
            '//*[@id="page-content-wrapper"]/div[1]/div/calling-screen/div/div[2]/meeting-panel-components/calling-roster/div/div[3]/div/div[1]/accordion/div/accordion-section[2]/div/calling-roster-section/div/div[1]/button')
        if "Currently in this meeting" in inmeeting.get_attribute('aria-label'):
            nbr = nbr + \
                int(inmeeting.get_attribute(
                    'aria-label').split("Currently in this meeting ")[1])
            return nbr
        else:
            nbr = nbr + \
                int(inmeeting.get_attribute(
                    'aria-label').split("Attendees ")[1])
            presenters = self.driver.find_element_by_xpath(
                '//*[@id="page-content-wrapper"]/div[1]/div/calling-screen/div/div[2]/meeting-panel-components/calling-roster/div/div[3]/div/div[1]/accordion/div/accordion-section[1]/div/calling-roster-section/div/div[1]/button')
            nbr = nbr + \
                int(presenters.get_attribute(
                    'aria-label').split("Presenters ")[1])
            return nbr

    def joinmeeting(self):
        count = 0
        while True:

            try:
                count += 1
                if(count >= 15):
                    break
                mic = self.driver.find_element_by_xpath(
                    '//*[@id="preJoinAudioButton"]/div/button/span[1]')
                if 'Mute microphone' in mic.get_attribute('outerHTML'):
                    mic.click()
                    print("I muted your microphone")

                cam = self.driver.find_element_by_xpath(
                    '//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[2]/toggle-button[1]/div/button/span[1]')
                if 'Turn camera off' in cam.get_attribute('outerHTML'):
                    cam.click()
                    print("I turned off your Camera")

                sleep(2)
                # joinbtn2
                self.driver.find_element_by_xpath(
                    '//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div/button').click()
                break
            except:
                print('Team Still Loading...')
                sleep(2)

        students = self.checkparticipants()
        print("Joined meeting,number of participants: "+str(students))
        sleep(5)

    def endcall(self):
        while True:
            try:

                print("Leaving the meet now!")
                end = self.driver.find_element_by_xpath(
                    '//*[@id="hangup-button"]')
                print(end)
                end.click()
                print("Meet ended")
            except:
                actions = ActionChains(self.driver)
                actions.send_keys(Keys.TAB)
                actions.perform()
            else:
                break

    def home(self):
        self.driver.get(
            'https://teams.microsoft.com/_#/school//?ctx=teamsGrid')

    def chat(self):
        while True:
            try:

                print("Leaving the meet now!")
                chat = self.driver.find_element_by_xpath(
                    '//*[@id="chat-button"]')
                print(chat)
                chat.click()
                print("Chat-box open")
            except:
                actions = ActionChains(self.driver)
                actions.send_keys(Keys.TAB)
                actions.perform()
            else:
                break

    def checkmessages(self):
        # chatpannel
        self.driver.find_element_by_xpath(
            '//*[@id="page-content-wrapper"]/div[1]/div/calling-screen/div/div[2]/meeting-panel-components')
        senders = []
        messages = []
        times = []
        # returns list of elements of names that sent messages
        msgsender = self.driver.find_elements_by_xpath(
            '//*[@data-tid="threadBodyDisplayName"]')
        for i in msgsender:
            senders.append(i.get_attribute('innerHTML').strip())

        # returns list of elements of messages content
        msgcontent = self.driver.find_elements_by_xpath(
            '//*[@data-tid="messageBodyContent"]')
        for i in msgcontent:
            res = re.findall(r'<div>(.*?)</div>',
                             str(i.get_attribute('innerHTML').strip()))
            messages.append(res)

        msgtime = self.driver.find_elements_by_xpath(
            '//*[@data-tid="messageTimeStamp"]')
        for i in msgtime:
            times.append(i.get_attribute('innerHTML').strip())
        n = len(messages)
        print(messages[1:n-1])

        return messages

    def sendmessage(self):
        x = self.commonmsg()
 #           try:
        inputmsg = self.driver.find_element_by_xpath(
            '//*[@data-tid="ckeditor-replyConversation"]')
#            inputmsg.click()
        inputmsg.send_keys(x)
        inputmsg.send_keys(Keys.ENTER)
        # sendmsg
        self.driver.find_element_by_xpath(
            '//*[@id="send-message-button"]').click()
#            except:
#                print("!  ERROR : problem sending present message   ! ")

    def commonmsg(self):
        message = self.checkmessages()

        n = len(message)

        max = 0

        for i in range(n):
            temp = message[i]
            count = 0
            for j in range(n):
                if(message[j] == temp):
                    count += 1
            if(count > max):
                max = count
                ans = temp
        print(ans)

        return ans


def TEAM():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """

    # If modifying these scopes, delete the file token.pickle.
    SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    print('Getting the upcoming event')
    calendarId = '5e42ll1vlsv91bcvptqpccf5pc@group.calendar.google.com'
    events_result = service.events().list(calendarId=calendarId, timeMin=now,
                                          maxResults=1, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(event['summary'])
        return (event['summary'])

def send(message): 
    sender_email = "anandkumarsingh.191ec104@nitk.edu.in"
    rec_email = "kumaranand07091993@gmail.com"
    password = input("enter your password")

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    print("login success")
    server.sendmail(sender_email, rec_email, message)
    print("message sent to", rec_email)

def main():
    clearscreen()
    print("Running the script!!!")
    b = bot()
    b.login()
    curr_time = datetime.datetime.now()
    while(curr_time.hour >= 9 and curr_time.hour <= 17):
        team = TEAM()
        b.loadteam('Group test')
        b.checkchannel()
        b.joinmeeting()
        b.chat()
        b.commonmsg()
        b.sendmessage()
        sleep(2)
        sleep(2)
        b.endcall()
        b.home()


main()
