import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuração do WebDriver
options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors")  # Ignorar erros SSL
options.add_argument("--log-level=3")  # Reduz mensagens de erro
options.add_argument("--disable-gpu")  # Evita erros gráficos
options.add_argument("--disable-dev-shm-usage")  # Melhora desempenho

service = Service(ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=options)

def click_if_present(page, xpaths, tentativas=2):
    """Tenta clicar no botão 'Pular anúncio' se ele aparecer."""
    for tentativa in range(1, tentativas + 1):
        for xpath in xpaths:
            try:
                print(f"Tentativa {tentativa}: Verificando botão de 'Pular anúncio' ({xpath})...")
                botao = WebDriverWait(page, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="skip-button:3"]')))
                botao.click()
                print('✅ Botão "Pular anúncio" clicado com sucesso.')
                time.sleep(1)  # Pequena pausa para garantir o próximo anúncio
                return
            except:
                print(f'❌ Botão "Pular anúncio" ({xpath}) não encontrado na tentativa {tentativa}.')

# Acessar o YouTube
search = input('Qual vídeo deseja assistir? ')
browser.get('https://www.youtube.com/')

# Pesquisar o vídeo
campo_pesquisa = browser.find_element(By.XPATH, '//*[@id="center"]/yt-searchbox/div[1]/form/input')
campo_pesquisa.send_keys(search)
ActionChains(browser).key_down(Keys.ENTER).perform()
time.sleep(5)

# Selecionar o primeiro vídeo
try:
    first_video = browser.find_element(By.XPATH, '(//ytd-video-renderer//a[@id="thumbnail"])[1]')
    first_video.click()
    print('🎬 Vídeo selecionado e reproduzindo...')
except:
    print('❌ Não foi possível encontrar um vídeo correspondente.')
    browser.quit()
    exit()

time.sleep(7)  # Aguarde o carregamento do vídeo

# Lista de possíveis XPaths para o botão "Pular anúncio"
xpaths_botao_skip = [
    '//*[@id="skip-button:3"]'
]

# Verifica e pula os anúncios
click_if_present(browser, xpaths_botao_skip, tentativas=2)

# Tempo para assistir ao vídeo antes de fechar
time.sleep(120)
browser.quit()
