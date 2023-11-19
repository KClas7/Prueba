import os
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.common.exceptions import NoSuchWindowException

def clear_cache():
    os.system('powershell "Get-Process MicrosoftEdge* | Stop-Process"')

def open_browser(url):
    # Crea una instancia de EdgeOptions
    options = webdriver.EdgeOptions()
    # Añade el argumento para iniciar maximizado
    options.add_argument("--start-maximized")
    # Asegúrate de tener el driver de Edge instalado y proporciona la ruta al ejecutable de Edge
    s = Service('C:\\Users\\ClasK\\3D Objects\\DriversBrowsers\\msedgedriver.exe')
    return webdriver.Edge(service=s, options=options)

def main():
    url = 'https://www.bing.com'
    browser = open_browser(url)
    browser.get(url)
    while True:
        try:
            # Intenta obtener las ventanas del navegador
            _ = browser.window_handles
        except NoSuchWindowException:  # Ahora Python sabe qué es NoSuchWindowException
            # Si falla, entonces el navegador ha sido cerrado
            print("El navegador ha sido cerrado")
            clear_cache()
            break
        time.sleep(1)  # Espera un segundo antes de verificar de nuevo

if __name__ == "__main__":
    main()