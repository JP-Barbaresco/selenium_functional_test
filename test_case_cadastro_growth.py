from faker import Faker
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import secrets
import string


import time

def test_case_casdastro_growth(logger):
    # Inicializando o Faker
    fake = Faker('pt_BR')

    # Caminho do seu ChromeDriver (adicione o caminho do seu driver local)
    driver_path = "./chromedriver-win64/chromedriver.exe"

    # Inicializa o serviço do ChromeDriver
    service = webdriver.ChromeService(driver_path)

    # Inicializa o driver do Chrome
    driver = webdriver.Chrome(service=service)

    try:
        # Abre o site de cadastro
        driver.get("https://www.gsuplementos.com.br/checkout/cadastro/")

        # Verifica se o título contém "Growth Supplements"
        assert "Growth Supplements" in driver.title

        # Gera dados fictícios
        nome = fake.name()
        email = fake.email()
        cpf = fake.cpf()
        data_nascimento = fake.date_of_birth(minimum_age=18, maximum_age=90).strftime("%d/%m/%Y")
        celular = fake.phone_number()
        tel_fixo = fake.phone_number()

        alphabet = string.ascii_letters + string.digits + string.punctuation
        senha = ''.join(secrets.choice(alphabet) for i in range(20)) 

        # Preenche os campos do formulário
        email_box = driver.find_element(By.ID, "email-cadastro")
        email_box.send_keys(email)
        logger.info("email inserido: " + email)

        cpf_box = driver.find_element(By.ID, "cpf-cadastro")
        cpf_box.send_keys(cpf)
        logger.info("cpf inserido: " + cpf)

        nome_box = driver.find_element(By.ID, "nome-cadastro")
        nome_box.send_keys(nome)
        logger.info("nome inserido: " + nome)

        nascimento_box = driver.find_element(By.ID, "data-nascimento-cadastro")
        nascimento_box.send_keys(data_nascimento)
        logger.info("nascimento inserido: " + data_nascimento)

        calular_box = driver.find_element(By.ID, "celular-cadastro")
        calular_box.send_keys(celular)
        logger.info("celular inserido: " + celular)

        telefone_box = driver.find_element(By.ID, "tel-fixo-cadastro")
        telefone_box.send_keys(tel_fixo)
        logger.info("telefone inserido: " + tel_fixo)

        senha_box = driver.find_element(By.ID, "senha-cadastro")
        senha_box.send_keys(senha)
        senha_box.click()
        senha_box.send_keys(Keys.ENTER)
        logger.info("senha inserida: " + senha)

        Enter_button = driver.find_element(By.CLASS_NAME, "btPadrao")
        Enter_button.send_keys(Keys.ENTER)
        logger.info("botão Cadstro acionado")

        # Aguarda alguns segundos para finalizar o cadastro
        time.sleep(10)

        # Verifica se retornou à página inicial
        assert "Suplementos: comprar suplementos alimentares é na Growth!" in driver.title

        logger.info("Teste realizado com sucesso!")
        driver.quit()
        return True

    except:
        driver.quit()
        return False
