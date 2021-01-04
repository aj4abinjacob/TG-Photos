import requests,datetime,os
programPath = os.path.realpath(__file__)
programPath = programPath[:programPath.rfind('/')+1]
try:
    config = open(programPath+'config/config.txt','r')
    for line in config:
        line = line.rstrip('\n')
        line = line.split('=')
        if line[0] == "Token":
            token = line[-1]   
        elif line[0] == "ChatId":
            chat_id = line[-1]
        elif line[0] == "UploadQuality":
            uploadQuality = line[-1]
    
except Exception as e:
    print('It seems like you haven\'t run the initial setup')
    print('Please run it and comeback')    

def upload(path):
    
    cwd = path[0:path.rfind('/')]
    cwd = path.replace("/",'@7%!')
    cwd = cwd.replace(' ','')
    extension = path[-4:]
    if extension == '.jpg' or '.png':
        if uploadQuality == 'low':
            try:
                imageUpload(path)
            except Exception as e:
                print('Sorry',e)
            else:
                pass
        else:
            try:
                documentUpload(path)
            except Exception as e:
                print('Sorry',e)
            else:
                pass
    else:
        if uploadQuality == 'low':
            try:
                videoUpload(path)
            except Exception as e:
                print('Sorry',e)
            else:
                pass
        else:
            try:
                documentUpload(path)
            except Exception as e:
                print('Sorry',e)
            else:
                pass
        



def videoUpload(abs_path):
    fullUpVideos = open(programPath+'logs/uploadedVideos.txt','a')
    cwd = abs_path[0:abs_path.rfind('/')]
    cwd = cwd.replace("/",'@7%!')
    cwd = cwd.replace(' ','')
    file = programPath+'logs/'+cwd+'@7%!uploadedList.txt'
    uploadList = open(file,'r+')
    if abs_path.rstrip('\n') in uploadList.read():
        # print(abs_path,'has already been Uploaded')
        pass
    else:
        print('Uploading :',abs_path)
        files = {'vidoe':open(abs_path,'rb')}
        try:
            caption = abs_path.split('/')[-1]
            res = requests.post('https://api.telegram.org/bot{}/sendVideo?chat_id={}&caption={}'.format(token,
                      chat_id,caption), files=files,timeout=60)
        except Exception as e:
            print('Sorry',e)
        else:
            if res.status_code == 200:
                abs_path = abs_path+'\n'
                uploadList.write(abs_path)
                res = res.json()
                fileId = res['result']['photo'][0]['file_id']
                upDate = res['result']['date']
                name  = res['result']['caption']
                value = datetime.datetime.fromtimestamp(upDate)
                timestamp = value.strftime('%Y-%m-%d %H:%M:%S')
                fullinfo = f'{name},{fileId},{timestamp}'
                fullUpVideos.write(fullinfo)
                print('Done Uploading :',abs_path.rstrip('\n'))


def imageUpload(abs_path):
    fullUpImage = open(programPath+'logs/uploadedImages.txt','a')
    cwd = abs_path[0:abs_path.rfind('/')]
    cwd = cwd.replace("/",'@7%!')
    cwd = cwd.replace(' ','')
    file = programPath+'logs/'+cwd+'@7%!uploadedList.txt'
    uploadList = open(file,'r+')
    if abs_path.rstrip('\n') in uploadList.read():
        # print(abs_path,'has already been Uploaded')
        pass
    else:
        print('Uploading :',abs_path)
        files = {'photo':open(abs_path,'rb')}
        try:
            caption = abs_path.split('/')[-1]
            res = requests.post('https://api.telegram.org/bot{}/sendPhoto?chat_id={}&caption={}'.format(token,
                      chat_id,caption), files=files,timeout=60)
        except Exception as e:
            print('Sorry',e)
        else:
            if res.status_code == 200:
                abs_path = abs_path+'\n'
                uploadList.write(abs_path)
                res = res.json()
                fileId = res['result']['photo'][0]['file_id']
                upDate = res['result']['date']
                name  = res['result']['caption']
                value = datetime.datetime.fromtimestamp(upDate)
                timestamp = value.strftime('%Y-%m-%d %H:%M:%S')
                fullinfo = f'{name},{fileId},{timestamp}'
                fullUpImage.write(fullinfo)
                print('Done Uploading :',abs_path.rstrip('\n'))


def documentUpload(abs_path):
    fullUpDocs = open('/home/abin/MyPythonScripts/TGPhotoBot/logs/uploadedDocuments.txt','a')
    cwd = abs_path[0:abs_path.rfind('/')]
    cwd = cwd.replace("/",'@7%!')
    print(cwd)
    file = programPath+'logs/'+cwd+'@7%!uploadedList.txt'
    uploadList = open(file,'r+')
    if abs_path.rstrip('\n') in uploadList.read():
        # print(abs_path, 'has already been Uploaded')
        pass
    else:
        try:
            print("Uploading :",abs_path.rstrip('\n'))
            files = {'document':open(abs_path,'rb')}
            caption = abs_path.split('/')[-1]
            res = requests.post('https://api.telegram.org/bot{}/sendDocument?chat_id={}&caption={}'.format(token,
                            chat_id,caption), files=files, timeout=60)
        except Exception as e:
            print('Sorry could not upload',abs_path.rstrip('\n'))
        else:
            if res.status_code == 200:
                abs_path = abs_path + '\n'
                uploadList.write(abs_path)
                res = res.json()
                fileId = res['result']['document']['thumb']['file_id']
                upDate = res['result']['date']
                name  = res['result']['caption']
                value = datetime.datetime.fromtimestamp(upDate)
                timestamp = value.strftime('%Y-%m-%d %H:%M:%S')
                fullinfo = f'{name},{fileId},{timestamp}'
                fullUpDocs.write(fullinfo)
                print('Done Uploading :', abs_path.rstrip('\n'))





