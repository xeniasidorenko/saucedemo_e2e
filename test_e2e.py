import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--incognito")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-password-manager-reauthentication")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

def test_saucedemo(driver):
    driver.get("https://www.saucedemo.com/")

    # Авторизация
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(1)

    # Добавление товара
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    time.sleep(1)

    # Корзина
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    time.sleep(1)

    checkout_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "checkout"))
    )
    checkout_button.click()
    time.sleep(1)

    # Заполнение данных
    first_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "first-name"))
    )
    first_name.send_keys("Ksenia")
    driver.find_element(By.ID, "last-name").send_keys("Sidorenko")
    driver.find_element(By.ID, "postal-code").send_keys("123456")
    driver.find_element(By.ID, "continue").click()
    time.sleep(1)

    # Завершение
    finish_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "finish"))
    )
    finish_button.click()

    success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))
    )
    
    assert "Thank you" in success_message.text, "Ожидаемое сообщение об успешной покупке не найдено"
