#GOOGLE CALENDAR
from __future__ import print_function
import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

#EDUPAGE
from edupage_api import Edupage

#OTHER
from datetime import datetime, timedelta

SCOPES = ['https://www.googleapis.com/auth/calendar']

def main():    
    #AUTH STUFF
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    else:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)

    #EDUPAGE STUFF
    
    login = input("Enter your edupage login: ")
    pwd = input("Enter your edupage password: ")

    edupage = Edupage(login, pwd)
    edupage.login()

    homework = edupage.get_homework()
    times = 2
    for hw in homework:
        #Print fancy user console stuff
        print('Title: {}'.format(hw.title))
        print('Description: {}'.format(hw.description))
        print('Due Date: {}'.format(hw.due_date))

        #Do boring dev stuff for calendar
        dateSting = datetime.strptime(str(hw.due_date), "%Y-%d-%m").strftime("%Y-%m-%d")
        yest = datetime.now() - timedelta(1)
        print('\n\n\n')
        if datetime.strptime(dateSting, "%Y-%m-%d") > yest:
            event = {
                'summary': hw.title,
                'description': hw.description,
                'start': {
                    'dateTime': '{0}T09:00:00-07:00'.format(dateSting),
                    'timeZone': 'Etc/GMT',
                },
                'end': {
                    'dateTime': '{0}T09:00:00-07:00'.format(dateSting),
                    'timeZone': 'Etc/GMT',
                },
            }
            if times < 9:
                times = times + 1
            else:
                times = 2
            event = service.events().insert(calendarId='primary', body=event).execute()
            print('Event created: {}'.format(event.get('htmlLink')))
        else:
            print('Too old')

if __name__ == '__main__':
    main()