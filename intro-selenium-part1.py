from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=your_exec_path)

driver.get("https://www.zabukovec.com/blog/webautomation/test0")
time.sleep(3)
el = driver.find_element_by_css_selector("#title")
title = el.text
els = driver.find_elements_by_css_selector(".urls")
urls = [e.get("href") for e in els]
print(title,urls)