import os, sys,uploader
programPath = os.path.realpath(__file__)
programPath = programPath[:programPath.rfind('/')+1]

def folderCheck(path):
    path2 = path.replace("/",'@7%!')
    grep = "* | grep -E '.jpg|.png|.gif|.mp4' >"
    command = "ls -1a -R "+path.replace(' ','\ ')+grep+programPath+"logs/"+path2+"fullList.txt"
    os.system(command)

def checkFullList(path):
    
    path2 = path.replace("/",'@7%!')
    path2 = path2.replace(' ','')
    fullList = open(programPath+'logs/'+path2+'fullList.txt','r')
    try:
        uploadedList = open(programPath+'logs/'+path2+'uploadedList.txt','r')
    except:
        uploadedList = open(programPath+'logs/'+path2+'uploadedList.txt','w')
   
    for line in fullList:
        print(line)
        uploader.upload(line.rstrip('\n'))
    print("Finished Uploading Folder",path.rstrip('/'))
    print('***********')




folderList = open(programPath+'config/folders.txt','r')
for line in folderList:
    folderCheck(line.rstrip('\n'))

folderList = open(programPath+'config/folders.txt','r')
for line in folderList:
    checkFullList(line.rstrip('\n'))
    print(line)
    


