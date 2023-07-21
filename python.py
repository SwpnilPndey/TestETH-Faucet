import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = Options()
chrome_options.add_argument("--user-data-dir=C:\\Users\\Dell\\AppData\\Local\\Google\\Chrome\\User Data\\")
chrome_options.add_argument("--profile-directory=Default")  

service = Service('C:\\chromedriver_win32\\chromedriver.exe')
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://sepoliafaucet.com/")

eoa=driver.find_element(By.TAG_NAME,'input')

eoa.clear()

eoa.send_keys("0xCa83F31f9b861E878A11efFBfB1fb38553ce7b1D")

time.sleep(15)    