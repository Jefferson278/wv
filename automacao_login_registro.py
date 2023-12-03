import asyncio
import pyautogui
import time
from datetime import date, datetime
from playwright.sync_api import sync_playwright
import mysql.connector
#-------------------------------------------------------------------------
with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)  #para abrir o navegador instalado no pc
    #acessando
    pagina = navegador.new_page()
    pagina.goto('https://bugbank.netlify.app/')
    #login
    pagina.fill('//*[@id="__next"]/div/div[2]/div/div[1]/form/div[1]/input','esta dando certo')
    time.sleep(3)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    time.sleep(2)
    pyautogui.write('quase')
    pagina.locator('xpath=//*[@id="__next"]/div/div[2]/div/div[1]/form/div[3]/button[1]').click()
    #registrando
    pagina.locator('xpath=//*[@id="__next"]/div/div[2]/div/div[1]/form/div[3]/button[2]').click()
    pagina.fill('//*[@id="__next"]/div/div[2]/div/div[2]/form/div[2]/input','eudsak@eusei.com')
    pagina.fill('//*[@id="__next"]/div/div[2]/div/div[2]/form/div[3]/input','abcdef')
    pagina.fill('//*[@id="__next"]/div/div[2]/div/div[2]/form/div[4]/div/input','1234567')
    pagina.fill('//*[@id="__next"]/div/div[2]/div/div[2]/form/div[5]/div/input','1234567')
    pagina.locator('xpath=//*[@id="__next"]/div/div[2]/div/div[2]/form/button').click()
    pagina.locator('xpath=//*[@id="btnCloseModal"]').click()
    #login correto
    
    pagina.fill('//*[@id="__next"]/div/div[2]/div/div[1]/form/div[1]/input','eudsak@eusei.com')
    pagina.fill('//*[@id="__next"]/div/div[2]/div/div[1]/form/div[2]/div/input','1234567')
    time.sleep(2)
    pagina.locator('xpath=//*[@id="__next"]/div/div[2]/div/div[1]/form/div[3]/button[1]').click()
    time.sleep(50)