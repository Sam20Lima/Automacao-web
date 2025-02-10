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