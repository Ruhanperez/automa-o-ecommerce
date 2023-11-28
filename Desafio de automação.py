from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import csv
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service = servico)

#lendo csv
with open('Dados.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        #acessando os campos do csv
        Username = row['username']
        Password = row['password']
        name = row['Nome']
        sobrenome = row['Sobrenome']
        cep = row['cep']

#adicionei time.sleep para melhor visualização da automação funcionando.

#fazendo login
navegador.get("https://www.saucedemo.com/")
time.sleep(3)
navegador.find_element('xpath', '//*[@id="user-name"]').send_keys(Username)
time.sleep(3)
navegador.find_element('xpath', '//*[@id="password"]').send_keys(Password)
time.sleep(3)
navegador.find_element('xpath','//*[@id="login-button"]').click()
time.sleep(2)

# Adicionando itens ao carrinho
navegador.find_element('xpath', '//*[@id="add-to-cart-sauce-labs-backpack"]').click()
time.sleep(3)
navegador.find_element('xpath', '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]').click()
time.sleep(3)

# Visualizar o carrinho
navegador.find_element('xpath', '//*[@id="shopping_cart_container"]/a').click()
time.sleep(5)

# Finalizando a compra
navegador.find_element('xpath', '//*[@id="checkout"]').click()
time.sleep(5)

# Cadastro
navegador.find_element('xpath', '//*[@id="first-name"]').send_keys(name)
time.sleep(2)
navegador.find_element('xpath', '//*[@id="last-name"]').send_keys(sobrenome)
time.sleep(2)
navegador.find_element('xpath', '//*[@id="postal-code"]').send_keys(cep)
time.sleep(2)
navegador.find_element('xpath', '//*[@id="continue"]').click()
time.sleep(4)

# Print do valor total
total_element = navegador.find_element('xpath', '//*[@id="checkout_summary_container"]/div/div[2]/div[8]')
total_value = total_element.text
print("Valor Total:", total_value)

# Finalizando
navegador.find_element('xpath', '//*[@id="finish"]').click()
time.sleep(5)

# Voltando à página principal
navegador.find_element('xpath', '//*[@id="back-to-products"]').click()
time.sleep(10)

navegador.quit()

