from playwright.sync_api import sync_playwright
import time

def clicar_se_presente(page, selector):
    try:
        # Espera até o botão ser visível, com timeout de segundos
        botao = page.wait_for_selector(selector, timeout=7000)
        botao.click()
        print('Botão "Pular anúncio" clicado.')
    except Exception as e:
        # Caso o botão não seja encontrado, ignora e continua
        print('Botão "Pular anúncio" não encontrado, etapa ignorada.')

    try:
        # Espera até o segundo botão ser visível, com timeout de 7 segundos
        botao = page.wait_for_selector(selector, timeout=7000)
        botao.click()
        print('Botão "Pular segundo anúncio" clicado.')
    except Exception as e:
        # Caso o botão não seja encontrado, ignora e continua
        print('Botão "Pular segundo anúncio" não encontrado, etapa ignorada.')

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