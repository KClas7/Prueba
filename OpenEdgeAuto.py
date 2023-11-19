import os
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchWindowException

def clear_cache():
    os.system('powershell "Get-Process MicrosoftEdge* | Stop-Process"')

def open_browser(url):
    # Asegúrate de tener el driver de Edge instalado y proporciona la ruta al ejecutable de Edge
    return webdriver.Edge(executable_path='C:\\Users\\ClasK\\3D Objects\\DriversBrowsers\\msedgedriver.exe')

def main():
    
    url = 'https://www.bing.com'
    browser = open_browser(url)
    browser.get(url)
    while True:
        try:
            # Intenta obtener las ventanas del navegador
            _ = browser.window_handles
        except NoSuchWindowException:
            # Si falla, entonces el navegador ha sido cerrado
            print("El navegador ha sido cerrado")
            clear_cache()
            break
        time.sleep(1)  # Espera un segundo antes de verificar de nuevo

if __name__ == "__main__":
    main()
