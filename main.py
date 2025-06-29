from scraper.driver import configurar_driver
from scraper.cookies import aceptar_cookies
from scraper.buscador import buscar_producto
from scraper.productos import cargar_productos_con_scroll
from scraper.info_productos import extraer_info
from scraper.generador_json import guardar_json
import time

def main():
    url = 'https://www.musimundo.com/'
    driver = configurar_driver()

    try:
        driver.get(url)
        time.sleep(2)
        
        aceptar_cookies(driver)

        buscar_producto(driver, "televisores")

        productos = cargar_productos_con_scroll(driver)

        info_productos = extraer_info(productos)

        guardar_json(info_productos)

        print('Productos cargados en archivo productos.json')

    except Exception as e:
        print(f'No se puedo obtener la pagina: ', e)
    
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
