from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

#instala versão atual do webdriver do navegador(no caso, chrome)
servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service = servico)


#abre o navegador
navegador.get("https://pages.hashtagtreinamentos.com/inscricao-minicurso-python-automacao-org?origemurl=hashtag_yt_org_minipython_8AMNaVt0z_M")
