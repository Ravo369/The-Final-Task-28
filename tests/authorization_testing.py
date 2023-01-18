import pytest
import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from settings import valid_email, valid_telephon, valid_password, valid_login, nevalid_telephone, password_more_360

# Позитивные и негативные проверки авторизации в табе "телефон"


@pytest.mark.parametrize('phone', valid_telephon)
def testing_authorization_valid_telephone(phone, testing):
    WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.ID, "username")))
    pytest.driver.find_element(By.ID, 'username').send_keys(phone)
    WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.ID, "password")))
    pytest.driver.find_element(By.ID, 'password').send_keys(valid_password)
    WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.ID, "kc-login")))
    pytest.driver.find_element(By.ID, 'kc-login').click()

    assert WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.CLASS_NAME,
                                                                                  'user-name__last-name')))


@pytest.mark.parametrize('phone', nevalid_telephone)
def testing_authorization_nevalid_telephon(phone, testing):
    WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.ID, "username")))
    pytest.driver.find_element(By.ID, 'username').send_keys(phone)
    WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.ID, "password")))
    pytest.driver.find_element(By.ID, 'password').send_keys(valid_password)
    WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.ID, "kc-login")))
    pytest.driver.find_element(By.ID, 'kc-login').click()

    error_text = WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.ID, 'form-error-message')))
    value_error_text = error_text.text
    assert value_error_text == 'Неверный логин или пароль'


def testing_authorization_empty_phonenumber(testing, phonenumber=''):
    WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.ID, "username")))
    pytest.driver.find_element(By.ID, 'username').send_keys(phonenumber)
    WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.ID, "password")))
    pytest.driver.find_element(By.ID, 'password').send_keys(valid_password)
    WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.ID, "kc-login")))
    pytest.driver.find_element(By.ID, 'kc-login').click()
    time.sleep(3)
    error_text = WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.CLASS_NAME,
                                                                                        'rt-input-container__meta'
                                                                                        '--error')))
    value_error_text = error_text.text
    assert value_error_text == 'Введите номер телефона'

# Позитивная и негативная проверка авторизации по табу почта


def testing_authorization_valid_email(testing):
    WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.ID, "t-btn-tab-mail")))
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.ID, "username")))
    pytest.driver.find_element(By.ID, 'username').send_keys(valid_email)
    WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.ID, "password")))
    pytest.driver.find_element(By.ID, 'password').send_keys(valid_password)
    WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.ID, "kc-login")))
    pytest.driver.find_element(By.ID, 'kc-login').click()

    assert WebDriverWait(pytest.driver, 10).until(
        ec.presence_of_element_located((By.CLASS_NAME, 'user-name__last-name')))


def testing_authorization_empty_email(testing, email=''):
    WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.ID, "t-btn-tab-mail")))
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.ID, "username")))
    pytest.driver.find_element(By.ID, 'username').send_keys(email)
    WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.ID, "password")))
    pytest.driver.find_element(By.ID, 'password').send_keys(valid_password)
    WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.ID,
                                                                           "kc-login")))
    pytest.driver.find_element(By.ID, 'kc-login').click()
    time.sleep(3)
    error_text = WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.CLASS_NAME,
                                                                                        'rt-input-container__meta'
                                                                                        '--error')))
    value_error_text = error_text.text
    assert value_error_text == 'Введите адрес, указанный при регистрации'

# Позитивная и негативная проверка авторизации по табу логин


def testing_authorization_valid_login(testing):
    WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.ID, "t-btn-tab-login")))
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.ID, "username")))
    pytest.driver.find_element(By.ID, 'username').send_keys(valid_login)
    WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.ID, "password")))
    pytest.driver.find_element(By.ID, 'password').send_keys(valid_password)
    WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.ID, "kc-login")))
    pytest.driver.find_element(By.ID, 'kc-login').click()

    assert WebDriverWait(pytest.driver, 10).until(
        ec.presence_of_element_located((By.CLASS_NAME, 'user-name__last-name')))


def testing_authorization_empty_login(testing, login=''):
    WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.ID, "t-btn-tab-mail")))
    pytest.driver.find_element(By.ID, 't-btn-tab-login').click()
    WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.ID, "username")))
    pytest.driver.find_element(By.ID, 'username').send_keys(login)
    WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.ID, "password")))
    pytest.driver.find_element(By.ID, 'password').send_keys(valid_password)
    WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.ID,
                                                                           "kc-login")))
    pytest.driver.find_element(By.ID, 'kc-login').click()
    time.sleep(3)
    error_text = WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.CLASS_NAME,
                                                                                        'rt-input-container__meta'
                                                                                        '--error')))
    value_error_text = error_text.text
    assert value_error_text == 'Введите логин, указанный при регистрации'

# Негативная проверка по табу лицевой счет


def testing_authorization_empty_bill(testing, bill=''):
    WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.ID, "t-btn-tab-ls")))
    pytest.driver.find_element(By.ID, 't-btn-tab-ls').click()
    WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.ID, "username")))
    pytest.driver.find_element(By.ID, 'username').send_keys(bill)
    WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.ID, "password")))
    pytest.driver.find_element(By.ID, 'password').send_keys(valid_password)
    WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.ID,
                                                                           "kc-login")))
    pytest.driver.find_element(By.ID, 'kc-login').click()
    time.sleep(3)
    error_text = WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.CLASS_NAME,
                                                                                        'rt-input-container__meta'
                                                                                        '--error')))
    value_error_text = error_text.text
    assert value_error_text == 'Введите номер вашего лицевого счета'

# Негативная проверка поля пароль в табе почта с паролем более 360 символов


def testing_password_more_360(testing):
    WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.ID, "t-btn-tab-mail")))
    pytest.driver.find_element(By.ID, 't-btn-tab-mail').click()
    WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.ID, "username")))
    pytest.driver.find_element(By.ID, 'username').send_keys(valid_email)
    WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.ID, "password")))
    pytest.driver.find_element(By.ID, 'password').send_keys(password_more_360)
    WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.ID,
                                                                           "kc-login")))
    pytest.driver.find_element(By.ID, 'kc-login').click()
    time.sleep(3)
    error_text = WebDriverWait(pytest.driver, 10).until(
        ec.presence_of_element_located((By.CLASS_NAME, 'card-container__title')))
    value_error_text = error_text.text
    assert value_error_text == 'Ошибка'

# python -m pytest -v --driver Chrome --driver-path theFinalTask28\Driver\chromedriver.exe tests\authorization_testing.py
