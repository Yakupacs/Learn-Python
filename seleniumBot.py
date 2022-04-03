from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "http://github.com"
driver.get(url)

time.sleep(2)
driver.maximize_window()
## tam ekran olur.
driver.save_screenshot("github.com-homepagee.png")
## ekran görüntüsü alır.

url = "http://github.com/yakupacs"
driver.get(url)

print(driver.title)

if "yakupacs" in driver.title:
    driver.save_screenshot("github-yakupacs.png")

time.sleep(2)

driver.back()
## önceki sayfaya döner.
# driver.forward()
## bir sonraki sayfaya gider.
time.sleep(2)
driver.close()