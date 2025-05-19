from selenium.common import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome, ChromeOptions, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


chrome_path = ChromeDriverManager().install()
service = Service(executable_path=chrome_path)
browser = Chrome(service=service)

url = input("Select URL: ")

browser.get(url)

expected_title = "Example" 
actual_title = browser.title 

if actual_title.find(expected_title) != -1: 
    browser.find_element(By.XPATH, "//*[contains(text(), 'More information')]").click()
    if(browser.current_url == 'https://www.iana.org/help/example-domains'):
        print("Page loaded correctly.")
    else:
     print("Page verification failed!")
else: 
    print("Page verification failed!")

browser.close()
