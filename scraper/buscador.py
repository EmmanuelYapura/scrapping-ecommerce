from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def buscar_producto(driver, texto):
    buscador = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='Encontrá lo que buscás']"))
    )
    buscador.send_keys(texto)
    buscador.send_keys(Keys.ENTER)
