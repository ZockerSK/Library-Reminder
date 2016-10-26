# Library-Reminder
A python script to send sms to your mobile phone as a reminder when the deadline of college library book(s) submission is approached
![Library-Reminder screenshot](https://cloud.githubusercontent.com/assets/12946753/19715766/184194c8-9b75-11e6-9047-6688ebc13791.png)
This script sends the sms to Indian mobile number only using [way2sms](http://www.way2sms.com). If you are from India, create a free account and feed your username (the mobile number) and password into the script inside the ```sendsms``` method. 

## Building the executable and running the script at bootup

1. Install ```PyInstaller``` using the command ```sudo pip install PyInstaller```
2. Make the executable using the command ```pyinstaller --onefile loginSpy.py```
3. Search for ```Startup Applications``` in the unity and add the path of executable to it ( finds under ```loginSpy/dist```) 
