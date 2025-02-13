import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
#dados para interagir com o teclado
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.common.keys import Keys


Service = Service(ChromeDriverManager().install())

def click_if_present(page, selector, tentativas=2):
    """Tenta clicar no botão 'pular anuncio' até duas vezes, caso apareça."""
    for tentativa in range(1, tentativas + 1):
        try:
            #Esperar o botão ficar visivel, com timeout de 10 segundos
            botão = page.wait_for_selector(selector, timeout=10000)
            botão.click()
            print('Botão "pular anuncio" clicado.')
            time.sleep(1) #pequena pausa para garantir que o próximo anuncio carregue
        except:
            print('Botão "pular anuncio" não encontrado, etapa ignorada.')

with webdriver.Chrome(service=Service) as browser:
    search = input('Qual vídeo deseja assistir? ') #solicitar ao usuário o nome do vídeo
    browser.get('https://www.youtube.com/') #abrir o navegador

    browser.find_element('xpath','//*[@id="center"]/yt-searchbox/div[1]/form/input').send_keys(search) #localizar o campo de pesquisa
    ActionChains(browser).key_down(Keys.ENTER).perform() #clica ENTER para pesquisar
    time.sleep(5) #tempo para carregar a página
    
    #seleciona o primeiro vídeo da lista e clica nele
    try:
        first_video = browser.find_element('xpath','(//ytd-video-renderer//a[@id="thumbnail"])[1]')
        first_video.click()
        print('Vídeo selecionado e reproduzindo...')
    except:
        print('Não foi possível encontrar um vídeo correspondente.')

    time.sleep(7)

    #aguarda e tenta pular os anúncios
    click_if_present(browser, 'xpath=//*[@id="skip-button:3"]', tentativas=2)

    #tempo para rodar o video antes de fechar
    time.sleep(120)
    browser.quit()