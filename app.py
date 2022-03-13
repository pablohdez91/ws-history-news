from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path='/mnt/c/Users/Pablo/Projects/ws-history-news/geckodriver.exe')
driver.get("http://selenium.dev")
time.sleep(15)

driver.quit()