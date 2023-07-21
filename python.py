import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

firefox_options = Options()
firefox_options.add_argument("--profile=C:\\Users\\Dell\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\6vyqky34.default-release")

service = Service('C:\geckodriver-v0.33.0-win32driver\geckodriver.exe')  

driver = webdriver.Firefox(service=service, options=firefox_options)
driver.get("https://sepoliafaucet.com/")

wait = WebDriverWait(driver, 10)
eoa = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[type="text"]')))

eoa.clear()

eoa.send_keys("0x95005C2defeae33C60432079B6b3845eC0fBfbC7")

time.sleep(15)


