## Saucedemo E2E Test (Selenium + Python)

Этот проект содержит автоматический E2E тест для проверки процесса покупки товара на демонстрационном сайте [saucedemo.com](https://www.saucedemo.com).

## Что делает тест

Сценарий теста:
1. Заходит на сайт
2. Входит в тестовый аккаунт:
   - Логин: `standard_user`
   - Пароль: `secret_sauce`
3. Добавляет товар "Sauce Labs Backpack" в корзину
4. Переходит в корзину и оформляет заказ
5. Проверяет, что заказ завершён успешно

## Установка и запуск

### 1. Склонируйте репозиторий или создайте новую папку с файлами:
- `tets_e2e.py`
- `requirements.txt`
- `README.md`


### 2. (Рекомендуется) Создайте виртуальное окружение

Откройте терминал в папке проекта:

```bash
python -m venv venv
```

Активируйте окружение:

- **Windows (PowerShell):**
  ```powershell
  .\venv\Scripts\Activate.ps1
  ```
  ! Если возникает ошибка доступа — запустите PowerShell от имени администратора и выполните:
  ```powershell
  Set-ExecutionPolicy RemoteSigned
  ```

- **Windows (cmd):**
  ```cmd
  venv\Scripts\activate.bat
  ```

- **Linux/macOS:**
  ```bash
  source venv/bin/activate
  ```


### 3. Установите зависимости

```bash
pip install -r requirements.txt
```


### 4. Запустите тест

```bash
python test_e2e.py
```

Откроется браузер, и тест выполнит весь сценарий покупки автоматически.


##  Зависимости

Файл `requirements.txt` должен содержать:

```
selenium
```


##  Требования

- Python 3.7 или выше
- Google Chrome установлен
- Для корректной работы теста файл chromedriver.exe должен быть:
либо в той же папке, что и файл main.py,
либо установлен в системе и добавлен в переменную среды PATH (так, чтобы его можно было запустить из любого места).


##  Примечание

Сайт [saucedemo.com](https://www.saucedemo.com) — демонстрационный. Все данные можно вводить произвольно.



