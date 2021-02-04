import json,requests,sys,platform,os
#reading config file
dir_path = os.path.dirname(os.path.realpath(__file__))
try:
    if platform.system() == "Windows":
        folders = ["\logs","\configs","\\TGDownloads/"]
        files = ["\\uploadedDocuments.txt","\config.txt","\downloadedDocuments.txt"]
    else:
        folders = ["/logs","/configs","/TGDownloads/"] 
        files = ["/uploadedDocuments.txt","/config.txt","/downloadedDocuments.txt"]
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

def download(fileName,file_id):
    print(f"Downloading : {fileName}")
    r = requests.get('https://api.telegram.org/bot'+bot_token+'/getFile?file_id='+file_id)
    r = r.json()
    pathFile = (r['result']['file_path'])
    
    url = 'https://api.telegram.org/file/bot'+bot_token+'/'+pathFile
    try:
        r = requests.get(url).content
        with open(dfolder+fileName,'wb') as f:
            f.write(r)
    except Exception as e:
        print(e)
    else:
        print(f"Succesfuly downloaded {fileName}")
        f = open(dir_path+folders[0]+files[-1],'a')
        f.write(fileName+'\n')

