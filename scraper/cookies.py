from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# Cerrar cartel de código postal
def aceptar_cookies(driver):
    try:
        btn_confirmacion_cookies = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'p.location-confirmation-modal__modal-close'))
        )
        btn_confirmacion_cookies.click()
    except Exception as e:
        print("No se encontró el cartel o ya estaba cerrado.")