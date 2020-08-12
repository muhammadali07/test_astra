from selenium import webdriver
import time
from selenium.webdriver import Chrome
import os
# driver = Chrome()
driver = webdriver.Chrome(executable_path=os.popen('which chromedriver').read().strip())

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/usr/bin/chromium"
driver = webdriver.Chrome(chrome_options=options)
driver.get('https://astra.co.id')
