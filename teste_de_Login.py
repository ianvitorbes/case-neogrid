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

# Fazendo o login (fazer login)
password.send_keys(Keys.RETURN)

# Delay para que a página possa carregar
driver.implicitly_wait(5)

# Verificação de login bem sucedido
if "Swag Labs" in driver.title:
    print("Login bem-sucedido!")
else:
    print("Falha no login!")

# Fechar naveador pressionando Enter
input("Pressione Enter para fechar o navegador...")

# Fechar o navegador após o teste
driver.quit()
