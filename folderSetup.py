import os,requests,time,pickle,json,sys
programPath = os.path.realpath(__file__)
programPath = programPath[:programPath.rfind('/')+1]



def folderCheck(path):
    path2 = path.replace("/",'@7%!')
    path2 = path2.replace(' ','')	
    grep = "* | grep -E '.jpg|.png|.gif|.mp4' >"
    # command = "ls -1a -R "+path.replace(' ','\ ')+grep+programPath+"logs/"+path2+"fullList.txt"
    # os.system(command)
    lis = os.listdir(path)
    extensions = ['.jpg','.png','.mp4','.gif']
    data =""
    try:
        for file in lis:
            if file[-4:] in extensions:
                data = data + file+'\n'
                continue
        f = open(programPath+'logs/'+path2+'fullList.txt','w')
        f.write(data)
    except Exception:
        pass

  



try:
    open(programPath+'config/folders.txt','r')
except:
    print("Looks like you haven't added any folders")
    lis = open(programPath+'config/folders.txt','w+')
    print("Lets add some folders")
    print("Please remember that when you add a folder the sub folders will scanned too") 
    while True:
        cwd = input("Enter Folder location\n>>>")
        if cwd[-1] != '/':
            cwd = cwd+'/'
        print(cwd,"has been added")
        lis.write(cwd+'\n')
        option = input("Are you done entering folders?[Y/N]")
        if option.lower() == 'y' :
            break
    

else:
    lis = open(programPath+'config/folders.txt','r+')
    print("Folders for uploading...")
    print("************************")
    for line in lis:
        line = line.rstrip('\n')
        print(line)
    print()
    option = input('Do you want to add or remove any folders from the list?[Add/Remove]>>>')
    if 'add' in option.lower():
        while True:
            cwd = input("Enter Folder location\n>>>")
            if cwd[-1] != '/':
                cwd = cwd+'/'
            print(cwd,"has been added")
            lis.write(cwd+'\n')
            option = input("Are you done entering folders?[Y/N]")
            if option.lower() == 'y' :
                break
    elif 'remove' in option.lower():
        while True:
            lis = open(programPath+'config/folders.txt','r+')
            data = lis.read()
            cwd = input("Enter Folder location\n>>>")
            if cwd[-1] != '/':
                cwd = cwd+'/'
            data = data.replace(cwd+'\n','')
            lis = open(programPath+'config/folders.txt','w+')
            lis.write(data)
            tr = cwd.replace('/','@7%!')
            tr = tr.replace(' ','')
            os.remove(programPath+'logs/'+tr+'fulllist.txt')
            print(cwd)
            print(cwd,'has been removed')
            option = input("Are you done removing folders?[Y/N]")
            if option.lower() == 'y' :
                break
    else:
        pass


lis = open(programPath+'config/folders.txt','r')
for line in lis:
    print(line.rstrip('\n'))
    folderCheck(line.rstrip('\n'))
    
