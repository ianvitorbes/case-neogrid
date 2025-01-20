from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_service = Service("C:\\WebDriver\\chromedriver.exe")

driver = webdriver.Chrome(service=chrome_service)

# Acesso a página inicial do sauce demo
driver.get("https://www.saucedemo.com/")

# Inserção de dados de login (standard_user)
username = driver.find_element(By.ID, "user-name")
username.send_keys("standard_user")

# Inserção de dados de login (secret_sauce)
password = driver.find_element(By.ID, "password")
password.send_keys("secret_sauce")

# Fazendo o login (fazer login)
password.send_keys(Keys.RETURN)

# Delay para que a página possa carregar
driver.implicitly_wait(5)

# Verificação de login bem sucedido
if "Swag Labs" in driver.title:
    print("Login bem-sucedido!")
else:
    print("Falha no login!")

# Delay para esperar o botão de Adicionar o carrinho ficar disponivel 
try:
    add_to_cart = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
    )
    # Adicionando o produto ao carrinho
    add_to_cart.click()
    print("Produto adicionado ao carrinho com sucesso!")
except Exception as e:
    print(f"Erro ao tentar adicionar o produto ao carrinho: {e}")

# Fechar navegador pressionando Enter
input("Pressione Enter para fechar o navegador...")

# Fechar o navegador após o teste
driver.quit()
