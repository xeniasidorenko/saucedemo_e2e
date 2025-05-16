from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_saucedemo():
    print("Запуск теста")

    # Настройки браузера
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--incognito")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-password-manager-reauthentication")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get("https://www.saucedemo.com/")
        print("Открыт сайт")

        # Авторизация
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(1)
        print("Вход выполнен")

        # Добавление товара
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        time.sleep(1)
        print("Товар добавлен")
       
        # Переход в корзину
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(1)
        # Ожидание и клик по кнопке Checkout
        checkout_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "checkout"))
        )
        checkout_button.click()
        time.sleep(1)

        # Ожидание поля имени и заполнение формы
        first_name = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )
        first_name.send_keys("Ksenia")
        driver.find_element(By.ID, "last-name").send_keys("Sidorenko")
        driver.find_element(By.ID, "postal-code").send_keys("123456")
        time.sleep(1)
        driver.find_element(By.ID, "continue").click()
        time.sleep(1)

        # Ожидание и завершение покупки
        finish_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "finish"))
        )
        time.sleep(1)
        finish_button.click()

        # Проверка успешной покупки
        success_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "complete-header"))
        )
        assert "Thank you" in success_message.text
        print("Тест завершён успешно!")

    except Exception as e:
        print("Ошибка во время теста:")
        print(e)

    finally:
        driver.quit()
        print("Браузер закрыт.")


if __name__ == "__main__":
    test_saucedemo()
