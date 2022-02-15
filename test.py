from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

username = "EMUSERNAME"
password = "EMPASSWORD"


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.electromaker.io/panel/login")
name_box = driver.find_element(By.NAME, "email")
pass_box = driver.find_element(By.NAME,"password")
name_box.send_keys(username)
pass_box.send_keys(password+Keys.ENTER)
#login_button = driver.find_element(By.CLASS_NAME,"btn btn-lg btn-success btn-block")
#login_button.click()
while True:
    currentstrippedurl = ''.join([i for i in driver.current_url if not i.isdigit()])
    digitsinurl = ''.join([i for i in driver.current_url if i.isdigit()])
#    print(currentstrippedurl)
    if currentstrippedurl == "https://www.electromaker.io/panel/Blog/edit?show=":
        print("CMS Show bug detected, rfreshing in modify mode")
        newurl = 'https://www.electromaker.io/panel/Blog/edit?modify='+digitsinurl
        driver.get(newurl)
        
    time.sleep(0.1)




driver.quit()

