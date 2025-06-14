from selenium.webdriver.common.by import By

def extraer_info(productos):
    lista = []
    for producto in productos:
        nombre = producto.find_element(By.CSS_SELECTOR, 'div.product-card_name').text
        marca = producto.find_element(By.CSS_SELECTOR, 'div.product-card_brand').text
        precio = producto.find_element(By.CSS_SELECTOR, "span[data-test-item-price='item_price']").text.split()[1]
        link = producto.find_element(By.TAG_NAME, 'a').get_attribute('href')

        # Descuento es un dato opcional en la pagina
        try:
            descuento = producto.find_element(By.CSS_SELECTOR, 'div.mus-pro-price_percent-discount').text
        except:
            descuento = None

        lista.append({
            'nombre': nombre,
            'marca': marca,
            'precio': precio,
            'link': link,
            'descuento': descuento
        })
        
    return lista
