# TGPhotos
Google photos alternative using telegram.<br>
Since free use of google photos is comming to an end, i needed an alternative so i ended up using telegram and it's features to create a free cloud like environment.You can only upload and download photos now. Since i use the botapi to download files and the limit of bot api file download is 50mb i decided not to add videos upload.  
I will be also sharing an xml file which can be used in an android phone having tasker installed to upload to telegram but please note that you can only download.

## Steps
1.Run "python3 config.py" in terminal
<br>
config,logs and TGDownloads will be created in your current working directory
<br>
2.Add your api_id,api_hash,bot_username and bot_token in config.txt in config folder
<br>
3.Run "python3 TGPhotos.py --startupload" after adding folder paths in folderpaths.txt in confg folder
<br>
you will be asked to enter your phone number and otp code during the first upload
<br>

## Usage
"python3 TGPhotos.py --startupload" to start uploading all the files in the folders paths you have entered
<br>
"python3 TGPhotos.py --mupload /fullpathtofile.jpg" to quickly upload a file
<br>
"python3 TGPhotos.py --download filename.png" to download file based on it's name
<br>
"python3 TGPhotos.py --date" to download files based on date
<br>
"python3 TGPhotos.py --list" to view all the files that have been uploaded
<br>


## Features 
Unlimited orginal quality photo upload

## Dependencies
Telegram
<br>
Telethon (https://github.com/LonamiWebs/Telethon)
<br>
requests (https://github.com/requests/requests) 
<br>
Tasker App (if you want to use in android) : The tasker profile uses bot api to upload file so you need to go to your bot chat if you want to download the file.

