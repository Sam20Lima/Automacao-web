from playwright.sync_api import sync_playwright
import time

def clicar_se_presente(page, selector, tentativas=2):
    """Tenta clicar no botão 'Pular anúncio' até duas vezes, caso apareça."""
    for tentativa in range(1, tentativas + 1):
        try:
            # Espera até o botão ser visível, com timeout de 7 segundos
            botao = page.wait_for_selector(selector, timeout=7000)
            botao.click()
            print('Botão "Pular anúncio" clicado.')
            time.sleep(1)  # Pequena pausa para garantir que o próximo anúncio carregue
        except:
            print('Botão "Pular anúncio" não encontrado, etapa ignorada.')

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    pagina = navegador.new_page()

    # Solicita ao usuário o nome do vídeo
    pesquisa = input("Qual vídeo deseja assistir? ")

    # Acessa o YouTube
    pagina.goto("https://www.youtube.com/")

    # Insere o texto na barra de pesquisa e busca
    pagina.locator('xpath=//*[@id="center"]/yt-searchbox/div[1]/form/input').click()
    #Clica na barra de pesquisa do youtube
    pagina.fill('xpath=//*[@id="center"]/yt-searchbox/div[1]/form/input', pesquisa)
    #Preenche a barra de pesquisa com o texto inserido pelo usuário
    pagina.locator('xpath=//*[@id="center"]/yt-searchbox/button').click()
    #Clica no botão de pesquisa

    # Aguarda os resultados carregarem
    pagina.wait_for_timeout(3000)

    # Seleciona o primeiro vídeo da lista e clica nele
    try:
        primeiro_video = pagina.locator('xpath=(//ytd-video-renderer//a[@id="thumbnail"])[1]')
        #Seleciona o primeiro link de video (com base na thub do video) nos resultados de pesquisa ou recomendação do YouTube
        primeiro_video.click()
        print("Vídeo selecionado e reproduzindo...")
    except:
        print("Não foi possível encontrar um vídeo correspondente.")

    # Aguarda e tenta pular até dois anúncios
    clicar_se_presente(pagina, 'xpath=//*[@id="skip-button:2"]', tentativas=2)

    # Tempo para o vídeo rodar antes de fechar o navegador
    time.sleep(120)
    navegador.close()