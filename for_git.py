from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

# Функция для вычисления математической задачи
def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

# Открываем браузер и переходим на страницу
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

# Ждем, когда цена дома станет $100
WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)

# Нажимаем кнопку "Book"
browser.find_element(By.ID, "book").click()

# Находим значение x для задачи
x_element = browser.find_element(By.ID, "input_value")
x = x_element.text
answer = calc(x)

# Вводим ответ в текстовое поле
browser.find_element(By.ID, "answer").send_keys(answer)

# Нажимаем кнопку "Submit"
browser.find_element(By.ID, "solve").click()

# Копируем ответ из алерта
alert = browser.switch_to.alert
alert_text = alert.text
answer_value = alert_text.split(': ')[-1]
print(answer_value)

# Закрываем браузер
alert.accept()
browser.quit()
