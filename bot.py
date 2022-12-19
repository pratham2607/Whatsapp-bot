import os
import time
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def msg():
    message_box = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
    message = input("Enter your message: ")
    message_box.send_keys(message, Keys.ENTER)

def again():
    askUser = input("Do you want to continue(Y/N): ")
    if(askUser == 'Y' or askUser == 'y'):
        msg()
        again()
    elif(askUser == 'N' or askUser == "n"):
        print("Exit")
        askUser = input("If you want to change contact enter ""Y"" OR if you want to log out enter ""N"": ")
        if(askUser == 'Y' or askUser == 'y'):
            contact_name()
            msg()
            again()
        elif(askUser == 'N' or askUser == "n"):
            dots = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/header/div[2]/div/span/div[4]/div/span')
            dots.click()
            logout = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/header/div[2]/div/span/div[4]/span/div/ul/li[5]/div')
            logout.click()
            logout_btn = driver.find_element(By.XPATH, '/html/body/div[1]/div/span[2]/div/div/div/div/div/div/div[3]/div/div[2]/div/div')
            logout_btn.click()
    else:
        print("invalid input!")
        again()

os.environ['PATH'] += r"C:\Users\HP\Desktop\selenium"
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
driver.implicitly_wait(5)
print("scan QR press enter")
input()

def contact_name():
    search_box = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/div/div[1]/div/div/div[2]/div/div[2]')
    name = input("Enter name of contact/group to message")
    search_box.send_keys(name, Keys.ENTER)

contact_name()
time.sleep(2)
msg()
again()
time.sleep(5)