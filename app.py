from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from math import ceil

# Search Parameters
periodico = 'Reforma'
busqueda = "economia incertidumbre"
fecha_ini = '01-06-2020'
fecha_fin = '01-06-2020'
url = 'https://busquedas.gruporeforma.com/{}/BusquedasComs.aspx'.format(periodico)
base = 'https://busquedas.gruporeforma.com/{}/'.format(periodico)

driver = webdriver.Firefox(executable_path='/mnt/c/Users/Pablo/Projects/ws-history-news/geckodriver.exe')
driver.get(url)

# Insert search parameters in the page
driver.find_element(by=By.NAME, value = 'txtTextSearch').send_keys(busqueda)
driver.find_element(by=By.NAME, value = 'txtFechaIni').send_keys(fecha_ini)
driver.find_element(by=By.NAME, value = 'txtFechaFin').send_keys(fecha_fin)
driver.find_element(by=By.ID, value = 'rb_orden_2').click()

# Get total number of pages for iteration
soup = BeautifulSoup(driver.page_source, 'html.parser')
P = soup.find('span', class_='totalRegistros').text
P = P.replace(",", "")
P = int(P)
P = ceil(P/20)  # 20 es el número de articulos por página

### parse the page
soup = BeautifulSoup(driver.page_source, 'html.parser')

### scrapping dates
soup_fechas = soup.find_all('p', class_='fecha')
fechas = []
for i in range(len(soup_fechas)):
    fechas.append(soup_fechas[i].text)

### scrapping titles
soup_titulos = soup.find_all('a', class_='hoverC')
titulos = []
for i in range(len(soup_titulos)):
    titulos.append(soup_titulos[i].text)

### scrapping links
links = []
for i in range(len(soup_titulos)):
    links.append(soup_titulos[i]['href'])


## Falta ver tema de acceso a los articulos
# articulos = []
# for l in range(len(links)):
#     driver.get(base+links[l])
#     soup_texto = BeautifulSoup(driver.page_source, 'html.parser')
#     art = str(soup_texto.find('div', class_='Scroll').find_all('div', class_='texto'))
#     articulos.append(art)


print(fechas)
print(titulos)
print(links)


driver.quit()


#driver.quit()