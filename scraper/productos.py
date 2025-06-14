from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Obtiene el total de productos que brinda la pagina
def obtener_total_productos(driver):
    total = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'span.total'))
    )
    return int(total.text.strip("()"))

# Obtiene los productos cargados en el HTML
def obtener_productos(driver):
    return driver.find_elements(By.CSS_SELECTOR, 'div.product-card')

# Maneja el scroll 
def scroll_hasta_elemento(driver, elemento):
    driver.execute_script("arguments[0].scrollIntoView();", elemento)
    time.sleep(4)

# Controla logica del scroll para obtener productos
def cargar_productos_con_scroll(driver, min_productos=40):
    total = obtener_total_productos(driver)
    productos = obtener_productos(driver)

    while len(productos) < min_productos and total >= min_productos:
        scroll_hasta_elemento(driver, productos[-1])
        productos = obtener_productos(driver)

    return productos[:min_productos]
