from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def buscar_producto(driver, texto):
    try:
        buscador = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Encontrá lo que buscás']")
        buscador.send_keys(texto)
        buscador.send_keys(Keys.ENTER)
    except Exception as e:
        print("Hubo un error en el input del buscador")