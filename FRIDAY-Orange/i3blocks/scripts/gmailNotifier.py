#!/home/rjslater/anaconda3/bin/python
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from random import shuffle
import subprocess

SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'


def extractTuples(l):
    newList = []
    for i in range(len(l)):
        for j in range(len(l[i])):
            newList.append(l[i][j])
    return newList


def checkIfSameList(l1, l2):
    a, b = extractTuples(l1), extractTuples(l2)

    for element in a:
        if element not in b:
            return False

    for element in b:
        if element not in a:
            return False
    return True


def getUnreadMessages():
    store = file.Storage('/home/rjslater/.config/i3blocks/scripts/token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('/home/rjslater/.config/i3blocks/scripts/credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('gmail', 'v1', http=creds.authorize(Http()))

    # Call the Gmail API to fetch INBOX
    results = service.users().messages().list(userId='me', labelIds=['INBOX'], q='is:unread').execute()
    messages = results.get('messages', [])

    # This is where my code starts
    unreadMessages = []

    if messages:
        for message in messages:
            msg = service.users().messages().get(userId='me', id=message['id']).execute()

            subject, sender = '', ''
            for header in msg['payload']['headers']:
                if header['name'] == 'Subject':
                    subject = header['value']
                if header['name'] == 'From':
                    sender = header['value']
            unreadMessages.append([subject, sender[:sender.find('<') - 1]])
    return unreadMessages


if __name__ == '__main__':
    # Get latest unread messages
    unreadMessages = getUnreadMessages()

    # Get last known unread messages
    lastKnownUnread = []
    try:
        file = open('/home/rjslater/.config/i3blocks/scripts/.gmailMessages', 'r')
        for line in file:
            lastKnownUnread.append(line.strip().split('*.*.*.*'))
    except:
        pass

    # Check if new and old lists are the same
    sameList = len(unreadMessages) == len(lastKnownUnread)
    if sameList:
        sameList = checkIfSameList(unreadMessages, lastKnownUnread)

    # If new and old lists are the same, cycle the ones in the file
    if sameList:
        if len(unreadMessages) > 0:
            lastKnownUnread.append(lastKnownUnread.pop(0))

            # Overwrite the file with cycled messages
            file = open('/home/rjslater/.config/i3blocks/scripts/.gmailMessages', 'w')
            for message in lastKnownUnread:
                file.write(message[0] + '*.*.*.*' + message[1] + '\n')
            file.close()

            # Display top old message from cycled list
            outputString = '\uf0e0 {} {}: {}'.format(len(lastKnownUnread), lastKnownUnread[0][1], lastKnownUnread[0][0])
            print(outputString[:60])

    # Else overwrite the file with the updated list
    else:
        file = open('/home/rjslater/.config/i3blocks/scripts/.gmailMessages', 'w')
        for message in unreadMessages:
            file.write(message[0] + '*.*.*.*' + message[1] + '\n')
        file.close()

        # Display top new message
        if len(unreadMessages) > 0:
            # Send a notification
            newMessage = None
            for message in unreadMessages:
                if message not in lastKnownUnread:
                    newMessage = message
                    break
            subprocess.call(['notify-send', '-t', '3000', '\uf0e0 ' + newMessage[1], newMessage[0]])

            # Display
            outputString = '\uf0e0 {} {}: {}'.format(len(unreadMessages), unreadMessages[0][1], unreadMessages[0][0])
            print(outputString[:60])
