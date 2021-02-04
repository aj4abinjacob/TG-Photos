
import requests,sys,platform,os
import uploader,downloader
args = sys.argv
dir_path = os.path.dirname(os.path.realpath(__file__))


try:
    if platform.system() == "Windows":
        x="\\"
        folders = ["\logs","\configs","\\TGDownloads/"]
        files = ["\\uploadedDocuments.txt","\config.txt","\\folderPaths.txt"]
    else:
        x="/"
        folders = ["/logs","/configs","/TGDownloads/"] 
        files = ["/uploadedDocuments.txt","/config.txt","/folderPaths.txt"]
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


def tgfupload():
    f = open(dir_path+folders[1]+files[2],"r")
    for i in f:
        i = i.rstrip('\n')
        lof = os.listdir(i)
        for fi in lof:
            if fi.endswith(".jpg") or fi.endswith('.png') or fi.endswith('.jpeg') or fi.endswith(".bmp"):
                if platform.system() == "Windows":
                    fileName = fi.split("\\")[-1]
                else:
                    fileName = fi.split('/')[-1] 
                filePath = i+x+fi
                uploadedDocuments = open(dir_path+folders[0]+files[0])
                udls = []
                for line in uploadedDocuments:
                    name = line.split(",")[0]
                    udls.append(name)
                if fileName in udls:
                    pass
                else:
                    print(f"Uploading {filePath}")
                    uploader.upload(filePath,fileName)

def tgmupload(filePath):
    fi = filePath
    if fi.endswith(".jpg") or fi.endswith('.png') or fi.endswith('.jpeg') or fi.endswith(".bmp"):
        if platform.system() == "Windows":
            fileName = fi.split("\\")[-1]
        else:
            fileName = fi.split('/')[-1] 
        uploadedDocuments = open(dir_path+folders[0]+files[0])
        udls = []
        for line in uploadedDocuments:
            name = line.split(",")[0]
            udls.append(name)
        if fileName in udls:
            pass
        else:
            print(f"Uploading {filePath}")
            uploader.upload(filePath,fileName)
    else:
        print("Unsported File")

def tgdownload(Filename):
    fileName = args[2]
    f = open(dir_path+folders[1]+files[2],"r")
    uploadedDocuments = open(dir_path+folders[0]+files[0])
    names = []
    created_dates = []
    uploaded_dates = []
    file_ids = []
    for line in uploadedDocuments:
        name = line.split(",")[0]
        created_date = line.split(",")[1]
        uploaded_date = line.split(",")[2]
        file_id = line.split(",")[3].rstrip('\n')
        names.append(name)
        created_dates.append(created_date)
        uploaded_dates.append(uploaded_date)
        file_ids.append(file_id)
        
    if fileName in names:
        index = names.index(fileName)
        file_id = file_ids[index]
        downloader.download(fileName,file_id)
    else:
        print("File hasn't been uploaded yet")

def tglist():
    f = open(dir_path+folders[1]+files[2],"r")
    uploadedDocuments = open(dir_path+folders[0]+files[0])
    names = []
    created_dates = {}
    uploaded_dates = []
    file_ids = []
    v = 1
    print("No    Name    CreatedDate UploadedDate")
    for line in uploadedDocuments:
            name = line.split(",")[0]
            created_date = line.split(",")[1]
            created_date = created_date.split(" ")[0]
            uploaded_date = line.split(",")[2]
            file_id = line.split(",")[3].rstrip('\n')
            print(f"{v}. {name} : {created_date} : {uploaded_date} ")
            v+=1

def tgdate():
    f = open(dir_path+folders[1]+files[2],"r")
    uploadedDocuments = open(dir_path+folders[0]+files[0])
    names = []
    created_dates = {}
    uploaded_dates = []
    file_ids = []
    for line in uploadedDocuments:
        name = line.split(",")[0]
        created_date = line.split(",")[1]
        created_date = created_date.split(" ")[0]
        uploaded_date = line.split(",")[2]
        file_id = line.split(",")[3].rstrip('\n')
        names.append(name)
        uploaded_dates.append(uploaded_date)
        file_ids.append(file_id)
        created_dates.setdefault(created_date, [])
        created_dates[created_date].append((name,file_id))
    print("Choose a date from the following")
    di = {} 
    cou = 1
    created_dates1 = sorted(created_dates.keys())
    for i in created_dates1:
        di[cou] = i    
        print(f"{cou}. {i}")
        cou += 1
    opt = int(input("Choose a date(Enter the number)\n>>>"))
    date = di[opt]
    if date not in created_dates:
        print("You haven't uploaded anything on that date")
    else:
        dic = {}
        v = 1
        print(f"Uploaded files in {date}")
        for i in created_dates[date]:
            dic[v] = i 
            print(v,':',i[0])
            v += 1
        opt = input("which files do you want to download?[All/Enter the number of files sepreated by space]\n>>>")
        if opt.lower() == "all":
            for i in dic.items():
                print(f"Downloading {i[1][0]}")
                downloader.download(i[1][0],i[1][1])
        elif int(opt) in dic:
            fileName = dic[int(opt)][0]
            file_id = dic[int(opt)][1]
            downloader.download(fileName,file_id)
        else:
            print("not a valid file format")
            sys.exit()

def addfolder():
    li = []
    uploadedDocuments = open(dir_path+folders[1]+files[-1],"r")
    for i in uploadedDocuments:
        i = i.rstrip('\n')
        li.append(i)
    uploadedDocuments = open(dir_path+folders[1]+files[-1],"a")  
    while True:
        folderpath = input("Enter the folder path\n>>>")
        if folderpath in li:
            print("Folder has alrady been added")
            opt = input("Still want to enter another folder?[y/n]")
            if opt.lower() == "y":
                continue
            else:
                sys.exit()
        else:
            uploadedDocuments.write(folderpath+"\n")
            op = input(f'Done adding "{folderpath}", want to add more?[y/n]\n>>>')
            if op.lower() == "n":
                break
            else:
                continue

if len(args) > 1:
    if args[1].lower() == "--startupload":
        tgfupload()
        print("Finished Uploading")
    elif args[1].lower() == "--mupload":
        fullpath = args[2]
        tgmupload(fullpath) 
    elif args[1].lower() == "--download":
        tgdownload(args[1])
    
    elif args[1].lower() == "--date":
        tgdate()

    elif args[1].lower() == "--list":
        tglist()
          
            
else:
    print("Hello user, choose an option")
    opt = int(input("1. View uploaded files\n2. Start Full Upload\n3. Manual Upload\n4. Download a file\n5. Download based on date the file was created\n6. Add folders to be uploaded\n>>>"))
    if opt == 1:
        print("uploaded files")
        tglist()
    elif opt == 2:
        print("Uploading files you entered on the directory folders\nfor adding more folders please enter it in TGPhotos/configs/folderpaths.txt\n>>>")
        tgfupload()
        print("Finished Uploading")
    elif opt == 3:
        opt = input("Enter the full path of the file you want to upload\n>>>")
        tgmupload(opt)
    elif opt == 4:
        opt = input("Enter the name of the file you want to download\n>>>")
        tgdownload(opt)
    elif opt == 5:
        tgdate()                
    elif opt == 6:
        addfolder()

