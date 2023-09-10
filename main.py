from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.rentcars.com/es/localidades/spain/madrid-md-madrid")
seccion_pais = driver.find_element(by=By.CLASS_NAME, value="#rc-destinations > div > div > div > div:nth-child(1) > div")

seccion_pais = driver.find_element(by=By.CSS_SELECTOR, value="#formPesquisa > div.search-btn > button")
seccion_pais.click()

driver.close()