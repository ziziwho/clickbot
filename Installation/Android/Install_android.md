# Android Intallation

## Watch video tutorial :    

> [![Android Installation Video](https://img.youtube.com/vi/9z4meV0BMMQ/0.jpg)](https://www.youtube.com/watch?v=9z4meV0BMMQ)    

## Read text tutorial :  
#### 1. Installing Termux
Termux is an Android terminal emulator and Linux environment app that works directly with no rooting or setup required.
A minimal base system is installed automatically - additional packages are available using the APT package manager.
Download and install [Termux](https://play.google.com/store/apps/details?id=com.termux) on your android device.

It is necessary to grant storage permission for Termux on Android 6 and higher. Use 'Settings>Apps>Termux>Permissions>Storage' and set to true.    

![termux-permission](/Images/termux-permissions.jpg)

For updating latest termux package, you need to run the following command:
```
pkg update && pkg upgrade
```
#### 2. Download Python on Termux
For for installing python in your termux, you need to run the following command:
```
pkg install python git
```   
#### 2. Extract files
Extract the ClickBot package using [File Manager](https://play.google.com/store/apps/details?id=com.alc.filemanager) from Mobile Clean System Lab at PlayStore.     
Extract the ClickBot by clicking on *vertical 3 dot* on right by *clickbot.zip* then click on **Extract**    

![extract](/Images/extract-android.jpg)

#### 3. Where is your file?  
It is important to know, where is your file directory path because we need this for the next step.       
My clickbot file is located at `/storage/emulated/0/clickbot` as shown in the picture below.

![dir](/Images/termux-dir.jpg)  

#### 4. Installing required modules
If you notice we have provided a file named **requirements.txt**, there are all the required modules.    
It has been listed in the file.    
To install all these modules, you need to run the following command on Termux to install it:    
```
cd /storage/emulated/0/clickbot/

pip install -r requirements.txt
```

![cd](/Images/termux-cd.jpg)

#### Getting Started
Getting started is super easy.

First you must /start all bot below :    
Click each of them and start each bot.    

0. [Dogecoin_click_bot](https://t.me/Dogecoin_click_bot?start=BbHI)
1. [Litecoin_click_bot](https://t.me/Litecoin_click_bot?start=2sWF)
2. [BCH_clickbot](https://t.me/BCH_clickbot?start=BGny)
3. [Zcash_click_bot](https://t.me/Zcash_click_bot?start=9io7)
4. [Bitcoinclick_bot](https://t.me/Bitcoinclick_bot?start=eBh6)

and after you start all bot, continue to next step.  
##### Usage: 
> python main.py phone_number [optional for notes]    

❗ Input number in international format (example: +1234567890)    

Open your termux terminal. Type the following command:    
```
python /storage/emulated/0/clickbot/main.py +639162995600
```
⚠️ Attention! Make sure you enter your phone number which linked with telegram. Do not enter the number listed in the example    
This is an example command.    

![cmd](/Images/termux-execute-cmd.png)

After you enter the command.    
You'll see the default home page and choices menu being displayed:    

![termux-choice](/Images/termux-choice_menu.png)

You will be given an opening welcome and given a choices of cryptocurrency.    
Here you can type the listed numbers such as 0, 1, 2, 3, and 4.    
After you make a choice. Your choice will be displayed on the screen.    
And after that, the action menu option is displayed    

![action-termux](/Images/termux-action_menu.png)    

state your choice by typing 0 or 1 or 2    

![termux-tele-code](/Images/termux-tele-code.png)    

After you make a choice. Your choice will be displayed on the screen.    
then to access your telegram, bot will request for your login code.    

![telecode](/Images/telecode.png)    

⚠️ Alert! Our script will not save or steal your login code but be careful not to share your code with anyone.    
This login code purpose is to gain access with your telegram then stored the session date within your computer.    
Once again, We are not collecting, storing any of your information.    

![termux-result](/Images/termux-result.jpg)    

After you make a choice. Your choice will be displayed on the screen.    
then the script will do his job and you just need to relax and your cryptocurrency will be running to your feets.    
