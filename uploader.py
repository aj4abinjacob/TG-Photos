import requests,pathlib
from datetime import datetime
from telethon import TelegramClient, events, sync
from telethon.tl.types import DocumentAttributeImageSize
import requests,sys,platform,os
#reading config file
dir_path = os.path.dirname(os.path.realpath(__file__))
try:
    if platform.system() == "Windows":
        folders = ["\logs","\configs","\\TGDownloads/"]
        files = ["\\uploadedDocuments.txt","\config.txt"]
    else:
        folders = ["/logs","/configs","/TGDownloads/"] 
        files = ["/uploadedDocuments.txt","/config.txt"]
    dfolder=dir_path+folders[2]
    f = open(dir_path+folders[1]+files[1],'r')
    ls = []
    for i in f:
        i = i.rstrip('\n')
        i = i.split('=')
        i = i[1]
        ls.append(i)
    api_id=ls[0]
    api_hash=ls[1]
    bot_username=ls[2]
    bot_token=ls[3]    
except Exception as e:
    print(e)
    print("Please run the initial setup")


#Uploading files
def upload(filePath,fileName):
    client = TelegramClient('session_name', api_id, api_hash)
    client.start()  
    try:
        client.send_file(bot_username, filePath,caption=fileName,force_document=True)
    except Exception as e:
        print(e)
    else:
        r = requests.get('https://api.telegram.org/bot'+bot_token+'/getUpdates?offset=-1').json()
        file_name = r["result"][0]['message']['document']['file_name']
        file_id = r["result"][0]['message']['document']['file_id']
        ts = r["result"][0]['message']['date']
        fname = pathlib.Path(filePath)
        assert fname.exists(), f'No such file: {fname}'  # check that the file exists
        upload_date = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        created_date = datetime.utcfromtimestamp(fname.stat().st_mtime).strftime('%Y-%m-%d %H:%M:%S')
        f=open(dir_path+folders[0]+files[0],'a')
        info = f"{fileName},{created_date},{upload_date},{file_id}\n"
        f.write(info)
        print(f'Uploaded {fileName}')
        client.disconnect()
    







