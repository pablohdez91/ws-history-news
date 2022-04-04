from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

url = "https://www.reforma.com"

driver = webdriver.Firefox(executable_path='./geckodriver.exe')
driver.get(url)

url_base = 'https://busquedas.gruporeforma.com/reforma/'
url_new =  url_base + 'Documento/Web.aspx?id=4148351|ArticulosCMS&url=https://img.gruporeforma.com/imagenes/ElementoRelacionado/9/711/8710657.jpg&text=economia+incertidumbre&tit='


driver.find_element(by = By.ID, value = "categoria1048").click()
time.sleep(15)
driver.find_element(by = By.NAME, value = "NE___AcsInputCuenta2").send_keys("****")
driver.find_element(by = By.NAME, value = "__AcsAceptarE").click()
time.sleep(5)
driver.find_element(by = By.NAME, value = "NE___AcsInputPassword2").send_keys("****")
driver.find_element(by = By.NAME, value = "__AcsAceptarE").click()
time.sleep(5)
driver.get(url_new)
soup_texto = BeautifulSoup(driver.page_source, 'html.parser')
art = str(soup_texto.find('div', class_='Scroll').find_all('div', class_='texto'))
print(art)
