import os,requests,time,pickle
programPath = os.path.realpath(__file__)
programPath = programPath.split('initialSetup.py')[0]

# class UserInfo:
#     def __init__(self,token,chatId,uploadQuality,dataLimit = None):
#         self.token = token
#         self.chatId = chatId
#         self.uploadQuality = uploadQuality 
#         self.dataLimit = dataLimit
    
#     def display(self):
#         print(f'1. Token : {self.token}\n2. Chat ID : {self.chatId}\n3. Upload Quality : {self.uploadQuality}\n4. Data Limit : {self.dataLimit}')

def newSetup():
    try:
        os.mkdir(programPath+'config')
        os.mkdir(programPath+'logs')
    except:
        pass
    config = open(programPath+'config/config.txt','w')
    welcomeText = 'Welcome to TGPhotoBot intial setup'
    welcomeText = welcomeText.center(229,'*')
    print(welcomeText)
    print()
    print('Lets get things started :)')
    print('*'*25)
    print('1.Search for BotFather in telegram')
    print('2.Send "/start" and then "/newbot" to BotFather')
    print('3.Then choose a name and username for your bot')
    print('4.You will get a message with bot token\n' )
    print('5.Now search for your bot in telegram with the username and send "\start" and a Hi')
    input('Press enter after you have have copied your bot token')
    print('6.Now copy and paste the token')
    token = input("Paste the token here\n>>>")
    url = "https://api.telegram.org/bot"+token+"/getUpdates"
    r = requests.get(url).json()
    chatId = r['result'][0]['message']['from']['id']
    print(chatId)
    uploadQuality = input('Enter the quality in which you want to upoload your photos?[H/L]\n>>>')
    if uploadQuality.lower() == 'l':
        uploadQuality = 'low'
        print('Uploads will be in low quality')
    elif uploadQuality.lower() == 'h':
        uploadQuality = 'high'
        print('Uploads will be in orginal quality')
    config.write(f'Token={token}\n')
    config.write(f'ChatId={chatId}\n')
    config.write(f'UploadQuality={uploadQuality}\n')
    print('Configured')
    print('Token =',token)
    print('ChatId =',chatId)
    print('UploadQuality =',uploadQuality)
    # dataLimit = input('Do you want to set a daily data limit?[Y/N]\n>>>')
    # if dataLimit.lower() == 'y':
    #     dailyDataLimit = input('Please enter your daily data limit')
    # elif dataLimit.lower() == 'n':
    #     print('There will be no limit to your daily uploads')
if __name__ == "__main__":
    try:
        config = open(programPath+'config/config.txt','r')
        if config.read() == "":
            os.remove(programPath+'config/config.txt')
            newSetup()
        print("It looks like you have already configured.")
        print("If you want to change something go to {}config/config.txt".format(programPath))
        print("and change the values")
    except Exception as e:
        print("Hello new user let's setup a few things")
        newSetup()