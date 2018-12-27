from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

username = "foo"
password = "bar"

chrome_options = Options()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=your_exec_path)
url = "https://www.zabukovec.com/blog/automation/test1.html"
driver.get(url)
time.sleep(3)


el = driver.find_element_by_css_selector("#username")
el.clear()
el.send_keys(username)

el = driver.find_element_by_css_selector("#password")
el.clear()
el.send_keys(password)

el = driver.find_element_by_css_selector("#validate")
el.click()
