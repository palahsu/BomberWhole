# Made by @palahsu

# Join Telegram Group for help: http://t.me/cyberclans
# Don't Copy Without Permission! Take Owner Permission!

from selenium import webdriver
import os
from webdriver_manager.chrome import ChromeDriverManager #1st changer
        
while True:
    choice = input("What Search Engine do you want to use?\n    1) WhatsApp\n    2) Telegram\n    3) Messenger\n   4)Instagram  > Answer(1 or 2 or 3 or instagram): ")
    if choice.lower() == "1" or choice.lower() == 'W':
                        break
    elif choice.lower() == "2" or choice.lower() == 'T':
                        break
    elif choice.lower() == "3" or choice.lower() == 'M':
                        break
    elif choice.lower() == "5" or choice.lower() == 'I':
                        break
    else:
        print("\n Wrong input, try again", 'red')
                        #time.sleep(3)
                        #clrscr()
        continue                    
        
def main():
    
    while True:
        ans = choice
        if ans == '1':
        
         driver = webdriver.Chrome(ChromeDriverManager().install()) #2nd change
         driver.get('https://web.whatsapp.com/')
         break
        elif ans == '2':
            driver = webdriver.Chrome(ChromeDriverManager().install()) #2nd change
            driver.get('https://web.telegram.im/#/login?p=')
        elif ans == '3':
            driver = webdriver.Chrome(ChromeDriverManager().install()) #2nd change
            driver.get('https://www.messenger.com/')
        elif ans =='4':
            driver = webdriver.Chrome(ChromeDriverManager().install()) #2nd change
            driver.get('https://www.instagram.com/')
            continue

    name = input('Enter the name of user or group: ')
    msg = input('Enter your message: ')
    i = int(input('Enter the count: ' ))
   
    input('Enter any key after scanning QR code')

    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()
	
	# The classname of message box may vary.
    msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]') 
    i = 0
    while i>=0:		
        
       for i in range(10):
        
         msg_box.send_keys(msg)
		# The classname of send button may vary.
         button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button') 
	  
         button.click() 
       print('Bombing Complete!!')

main()