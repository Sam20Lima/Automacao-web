from selenium import webdriver
import logging
from selenium.webdriver.firefox.service import Service
from selenium import webdriver_manager
from selenium.webdriver.common.by import By

logging.basicConfig(level=logging.INFO, filename="logs", format="%(asctime)s" - "%(message)s")

driver = webdriver.Firefox()
def click_if_present()
    if driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[2]/div/div[2]/div[1]/div/div[5]/span'):
        confirm_button = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[2]/div/div[3]/div/button')
        confirm_button.click()
        logging.info("Agendamento Encontrado. Botão clicado")

    else:
        logging.info("Agenamento não encontrada. Etapa pulada!")

