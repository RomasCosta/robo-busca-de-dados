from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

#utilizar comandos usando teclas
from selenium.webdriver.common.keys import Keys

#usar para esperar entre as ações definidas
import pyautogui as tempoPausa
import pyautogui as atalhoTeclasTeclado

from selenium.webdriver.common.by import By

#instala versão atual do webdriver do navegador(no caso, chrome)
servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service = servico)


#abre o navegador
navegador.get("https://google.com/")


tempoPausa.sleep(4)

navegador.find_element(By.NAME, "q").send_keys("dolar hoje")

tempoPausa.sleep(4)

#keys.return mantém o curso no campo e dá ENTER
navegador.find_element(By.NAME, "q").send_keys(Keys.RETURN)

tempoPausa.sleep(4)

valorDolar = navegador.find_elements(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')[0].text


print(valorDolar)


#-----------------------------------

tempoPausa.sleep(2)

#volta para o campo 'q'
navegador.find_element(By.NAME, "q").send_keys("")

tempoPausa.sleep(2)

#vai para o X para limpar a tela
atalhoTeclasTeclado.press("tab")

tempoPausa.sleep(2)

#enter para limpar o campo de pesquisa
atalhoTeclasTeclado.press("enter")

tempoPausa.sleep(4)

navegador.find_element(By.NAME, "q").send_keys("euro hoje")

tempoPausa.sleep(4)

#keys.return mantém o curso no campo e dá ENTER
navegador.find_element(By.NAME, "q").send_keys(Keys.RETURN)

tempoPausa.sleep(4)

valorEuro = navegador.find_elements(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]')[0].text


print(valorEuro)



























