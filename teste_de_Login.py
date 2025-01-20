from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

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

# Fazendo o login
password.send_keys(Keys.RETURN)

# Delay para que a página possa carregar
driver.implicitly_wait(5)

# Verificação de login bem sucedido
if "Swag Labs" in driver.title:
    print("Login bem-sucedido!")
else:
    print("Falha no login!")

# Adicionando o produto ao carrinho
add_to_cart = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
add_to_cart.click()

# Verificando se o produto foi adicionado ao carrinho
cart_count = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
if cart_count.text == "1":
    print("Produto adicionado ao carrinho!")
else:
    print("Não consegui adicionar o produto.")

# Fechar naveador pressionando Enter
input("Pressione Enter para fechar o navegador...")

# Fechar o navegador após o teste
driver.quit()