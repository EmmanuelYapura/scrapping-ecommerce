from scraper.driver import configurar_driver

def main():
    url = 'https://www.musimundo.com/'
    driver = configurar_driver()

    try:
        driver.get(url)
        input('Presionar una tecla para cerrar navegador...')
    except Exception as e:
        print(f'No se puedo obtener la pagina: ', e)
    
    finally:
        driver.quit()

if __name__ == "__main__":
    main()