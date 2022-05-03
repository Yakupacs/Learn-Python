from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

username = input("Username: ")
password = input("Password: ")

class Twitter:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://twitter.com/i/flow/login")
        time.sleep(2)

        usernameInput = self.browser.find_element_by_xpath("//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[5]/label/div/div[2]/div/input")
        usernameInput.send_keys(self.username)
        btnUsername = self.browser.find_element_by_xpath("//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[6]/div")
        btnUsername.click()
        time.sleep(2)
       
        passwordInput = self.browser.find_element_by_xpath("//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
        passwordInput.send_keys(self.password)
        btnPassword = self.browser.find_element_by_xpath("//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div")
        btnPassword.click()
        time.sleep(2)

    def search(self, hashtag):
        searchBtn = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/label/div[2]/div/input")
        searchBtn.send_keys(hashtag)
        time.sleep(2)
        searchBtn.send_keys(Keys.ENTER)
        time.sleep(2) 

        list = self.browser.find_element_by_xpath("//div[@data-testid='primaryColumn']/div[0]/div[3]")

        for item in list:
            print("************")
            print(item.text)     

twitter = Twitter(username, password)
twitter.signIn()
twitter.search("python")