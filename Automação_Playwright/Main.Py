"""from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    pagina = navegador.new_page()
    pagina.goto('https://www.youtube.com/')
    pagina.locator('xpath=//*[@id="center"]/yt-searchbox/div[1]/form/input').click()
    pagina.fill('xpath=//*[@id="center"]/yt-searchbox/div[1]/form/input', 'não gosto de ninguém matanza')
    time.sleep(2)
    pagina.locator('xpath=//*[@id="center"]/yt-searchbox/button').click()
    time.sleep(2)
    pagina.goto('https://www.youtube.com/watch?v=kVEBesKRxEQ')
    pagina.locator('xpath=//*[@id="movie_player"]/div[9]/button').click()


    def clicar_se_presente(page, selector):
        Botão = page.query_selector(selector)
        if Botão:
            Botão.click()
            print('Botão clicado.')
        else:
            print('Botão não encontrado, etapa ignorada.')

    # Chame a função com o seletor do botão
    clicar_se_presente(pagina, 'xpath=//*[@id="skip-button:3"]')
    time.sleep(60)"""

from playwright.sync_api import sync_playwright
import time

def clicar_se_presente(page, selector):
    try:
        # Espera até o botão ser visível, com timeout de 5 segundos
        botao = page.wait_for_selector(selector, timeout=10000)
        botao.click()
        print('Botão "Pular anúncio" clicado.')
    except Exception as e:
        # Caso o botão não seja encontrado, ignora e continua
        print('Botão "Pular anúncio" não encontrado, etapa ignorada.')

def tocar_video_automaticamente(termo_de_busca):

        # Digite o termo de busca no campo de pesquisa e pressione Enter
        pagina.fill('input#search', termo_de_busca)
        pagina.keyboard.press('Enter')
        
        # Aguarde os resultados carregarem
        pagina.wait_for_selector('ytd-video-renderer')
        
        # Clique no primeiro vídeo dos resultados
        primeiro_video = pagina.query_selector('ytd-video-renderer a#video-title')
        if primeiro_video:
            primeiro_video.click()
            print('Vídeo tocando.')
        else:
            print('Nenhum vídeo encontrado.')

        # Defina o termo de busca desejado
        termo_de_busca = 'SEU_TERMO_DE_BUSCA'

        tocar_video_automaticamente(termo_de_busca)

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    pagina = navegador.new_page()

    # Acessa o YouTube
    pagina.goto('https://www.youtube.com/')

    # Realiza a busca no YouTube
    pagina.locator('xpath=//*[@id="center"]/yt-searchbox/div[1]/form/input').click()
    pagina.fill('xpath=//*[@id="center"]/yt-searchbox/div[1]/form/input', 'não gosto de ninguém matanza')
    pagina.locator('xpath=//*[@id="center"]/yt-searchbox/button').click()

    # Espera um pouco para a busca carregar
    pagina.wait_for_timeout(2000)

    # Acessa o vídeo específico
    pagina.goto('https://www.youtube.com/watch?v=kVEBesKRxEQ')

    pagina.keyboard.press('K')

    # Aguarda o player carregar e tenta clicar no botão "Pular anúncio" se aparecer
    clicar_se_presente(pagina, 'xpath=//*[@id="skip-button:2"]')

    # Espera um pouco antes de fechar o navegador
    time.sleep(120)
    navegador.close()