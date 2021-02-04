import os, platform

if platform.system() == "Windows":
    folders = ["\logs","\configs","\\TGDownloads"]
    files = ["\\uploadedDocuments.txt","\config.txt","\\folderPaths.txt","\\downloadedDcouments.txt"]
else:
    folders = ["/logs","/configs","/TGDownloads"] 
    files = ["/uploadedDocuments.txt","/config.txt","/folderPaths.txt","/downloadedDcouments.txt"]
dir_path = os.path.dirname(os.path.realpath(__file__))

#creating log and downloads
try:
    os.mkdir(dir_path+folders[0])
    os.mkdir(dir_path+folders[2])
    f = open(dir_path+folders[0]+files[0],'w')
except Exception as e:
    print(e)

#creating config folder and file
try:
    os.mkdir(dir_path+folders[1])
    f = open(dir_path+folders[1]+files[1],'w')
    f.write("api_id=\napi_hash=\nbot_username=\nbot_token=")
    f1 = open(dir_path+folders[1]+files[2],'w')
except Exception as e:
    print(e)

print('Welcome to the TGPhots Setup')
print('***************************')
print('Two text files should be created in the configs folder please enter the details of following items there')
print("""
In "config.txt" 
***************
api_id=1827904   
api_hash=09h121cd072f6d144gf4gdf4g24878
bot_username=yourBotName
bot_token=1565429018:Uacu-uuicnjke121fkun1f484kd4d4o
!!!This is just a representation of how you should enter the details!!!

In the "folderPaths.txt"
************************
/home/user/Pictures/MyPhotos/
/home/user/Downloads/wallpapers/
!!!Add or remove folder paths based on your requirements!!!

For api id and api_hash 
***********************

    Go to https://my.telegram.org, under API Development

    Enter you phone number and login details

    create an app get the api id and hash


For both bot user name and bot token
****************************

    Search for BotFather in telegram

    Send "/start" and then "/newbot" to BotFather

    Then choose a name and username for your bot

    You will get a message with bot token, please copy your bot token

    Now search for your bot in telegram with the username and send "\start" and a "Hi"

        """)


