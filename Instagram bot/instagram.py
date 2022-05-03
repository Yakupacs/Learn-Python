from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

username = input("Username: ")
password = input("Password: ")

class Instagram:
    def __init__(self,username,password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)

        usernameInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
        passwordInput = self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)

    def getFollowers(self):
        time.sleep(2)
        self.browser.get(f"https://www.instagram.com/{self.username}")
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a/div").click()
        
        time.sleep(2)

        dialog = self.browser.find_element_by_css_selector("div[role=dialog] ul")
        followerCount = len(dialog.find_elements_by_css_selector("li"))

        print(f"First Count: {followerCount}")

        action = webdriver.ActionChains(self.browser)
        while True:
            dialog.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)
            newCount = len(dialog.find_elements_by_css_selector("li"))

            if followerCount != newCount:
                followerCount = newCount
                print(f"Updated Count: {newCount}")
                time.sleep(1)
            else:
                break

        followers = dialog.find_elements_by_css_selector("li")

        followerList = []
        for user in followers:
            link = user.find_element_by_css_selector("a").get_attribute("href")
            followerList.append(link)

        with open("followers.txt", "w", encoding="UTF-8") as file:
            for item in followerList:
                file.write(item + "\n")

    
    def followUser(self, username):
        time.sleep(2)
        self.browser.get("https://www.instagram.com/" + username)
        time.sleep(2)

        followButton = self.browser.find_element_by_tag_name("button")
        print(followButton.text)
        if followButton.text != "Mesaj Gönder":
            followButton.click()
            time.sleep(2)
        else:
            print("Zaten takiptesin.")

    def unFollowUser(self, username):
        self.browser.get("https://www.instagram.com/" + username)
        time.sleep(2)

        followButton = self.browser.find_element_by_tag_name("button")
        if followButton.text == "Mesaj Gönder":
            followButton.click()
            time.sleep(2)
            self.browser.find_element_by_xpath('//button[text()="Takibi Bırak"]').click()
        else:
            print("Zaten Takip Etmiyorsunuz.")

instgrm = Instagram(username, password)
instgrm.signIn()
# instgrm.getFollowers()
instgrm.followUser("besiktas")
instgrm.unFollowUser('besiktas')