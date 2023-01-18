import pytest
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def testing_registration_button(testing):
    WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.ID, 'kc-register')))
    pytest.driver.find_element(By.ID, 'kc-register').click()
    text_registration = WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.CLASS_NAME,
                                                                                               'card-container__'
                                                                                               'title')))
    value_text_registration = text_registration.text

    assert value_text_registration == "Регистрация"


def testing_forgot_password_button(testing):
    WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.ID, 'forgot_password')))
    pytest.driver.find_element(By.ID, 'forgot_password').click()
    text_forgot_password = WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.CLASS_NAME,
                                                                                               'card-container__title')))
    value_text_forgot_password = text_forgot_password.text

    assert value_text_forgot_password == "Восстановление пароля"

# python -m pytest -v --driver Chrome --driver-path theFinalTask28\Driver\chromedriver.exe tests\link_buttons_testing.py
