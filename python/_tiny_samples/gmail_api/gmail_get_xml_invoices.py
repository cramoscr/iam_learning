# gmail_get_xml_invoices.py
# ----------------------
# Updated: cramos 02/ago/2023
# Reference:
#    https://www.geeksforgeeks.org/how-to-read-emails-from-gmail-using-gmail-api-in-python/

# Pre-requisites
#   + Using a Google's Dev project with Gmail_API enabled
#   + Local installation of google's api client

# How to run it
#   python3 gmail_api_read.py
#   Note:
#      Before calling this app, get a Gmail's Chrome sesion logged on
#      with the user whose emails are going to be processed

from __future__ import print_function
from cProfile import label

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

import base64
import email
from bs4 import BeautifulSoup

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def read_folders(pCreds):
    try:
        # Starts the Gmail API conection for reading mailbox contents
        service = build('gmail', 'v1', credentials=pCreds)

        # Enumerating mailbox folders
        results = service.users().labels().list(userId='me').execute()
        labels = results.get('labels', [])

        if not labels:
            print('No labels found.')
            return
        #print(f'results: {labels}')
        
        print('\n Labels_______:')
        for label in labels:
            print(f"name: {label['name']} \t id:{label['id']}")

    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f'An error occurred: {error}')

def read_messages(pCreds):
    try:
        # Starts the Gmail API conection for reading mailbox contents
        service = build('gmail', 'v1', credentials=pCreds)

        # Enumerating messages inside INBOX folder
        #result = service.users().messages().list(userId='me', labelIds=['INBOX']).execute()
        result = service.users().messages().list(userId='me', labelIds=['INBOX'], q='subject:Factura').execute()

        messages = result.get('messages')

        print(f'\n Messages......:')

        # iterate through all the messages
        for msg in messages:
            # Get the message from its id
            txt = service.users().messages().get(userId='me', id=msg['id']).execute()
    
            # Use try-except to avoid any Errors
            try:
                # Get value of 'payload' from dictionary 'txt'
                payload = txt['payload']
                headers = payload['headers']

                #print(f'headers:{headers}')
                #return

                # Look for Subject and Sender Email in the headers
                for d in headers:
                    if d['name'] == 'Subject':
                        vSubject = d['value']
                    if d['name'] == 'From':
                        vSender = d['value']
                    if d['name'] == 'Date':
                        vDate = d['value']

                # The Body of the message is in Encrypted format. So, we have to decode it.
                # Get the data and decode it with base 64 decoder.
                parts = payload.get('parts')[0]
                data = parts['body']['data']
                data = data.replace("-","+").replace("_","/")
                decoded_data = base64.b64decode(data)

                # Now, the data obtained is in lxml. So, we will parse 
                # it with BeautifulSoup library
                #soup = BeautifulSoup(decoded_data , "xml")
                #body = soup.body()

                # Printing the subject, sender's email and message
                print("Date: ", vDate)
                print("Subject: ", vSubject)
                print("From: ", vSender)
                #print("Message: ", body)
                print('\n')
            except:
                pass

    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f'An error occurred: {error}')

def main():
    """Shows basic usage of the Gmail API.
    Looks for INBOX elements that contains 'Factura Electronica' keywords
    and XML attachments.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    # Call method for mailbox's folders enumeration
    read_folders(creds)

    # Call method for mailbox's messages enumeration
    read_messages(creds)

if __name__ == '__main__':
    main()