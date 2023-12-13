import csv
from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация веб-драйвера (Chrome)
driver = webdriver.Chrome()

# Переход на веб-сайт 'https://www.nseindia.com/'
driver.get('https://www.nseindia.com/')

# Пауза в 3 секунды для загрузки страницы
sleep(3)

# Попытка закрыть модальное окно
try:
    modal_header = driver.find_elements(By.CLASS_NAME, 'modal-header')[1]
    close_button = modal_header.find_element(By.TAG_NAME, 'button')
    close_button.click()
except Exception as e:
    # В случае ошибки (если модальное окно не найдено), продолжаем выполнение скрипта
    pass

# Нахождение кнопки "Board Meetings" и прокрутка к ней
board_button = driver.find_element(By.LINK_TEXT, 'Board Meetings')
driver.execute_script("arguments[0].scrollIntoView(true);", board_button)

# Нахождение и клик на кнопке "View All"
view_button = driver.find_element(By.ID, 'view-all')
view_button.click()

# Пауза в 3 секунды для загрузки данных
sleep(3)

# Нахождение поля ввода и поиск событий по ключевому слову "Buy back"
input_field = driver.find_elements(By.TAG_NAME, 'input')[4]
input_field.send_keys("Buy back")
input_field.send_keys(Keys.DOWN)
input_field.send_keys(Keys.ENTER)

# Закрытие веб-драйвера
driver.close()
