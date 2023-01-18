import pytest
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def testing_vk_page(testing):
    WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.XPATH, '//a[@id="oidc_vk"]')))

    pytest.driver.find_element(By.XPATH, '//a[@id="oidc_vk"]').click()
    capture_path = 'C:\\Users\\HP\\PycharmProjects\\theFinalTask28\\VK.png'
    pytest.driver.save_screenshot(capture_path)

    assert WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.CLASS_NAME, 'oauth_head')))


def testing_ok_page(testing):
    WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.XPATH, '//a[@id="oidc_ok"]')))

    pytest.driver.find_element(By.XPATH, '//a[@id="oidc_ok"]').click()

    assert WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.CLASS_NAME, 'ext-widget_h_tx')))


def testing_mail_page(testing):
    WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.XPATH, '//a[@id="oidc_mail"]')))

    pytest.driver.find_element(By.XPATH, '//a[@id="oidc_mail"]').click()

    assert WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.CLASS_NAME, 'header__logo')))


def testing_google_page(testing):
    WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.XPATH, '//a[@id="oidc_google"]')))

    pytest.driver.find_element(By.XPATH, '//a[@id="oidc_google"]').click()

    assert WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.CLASS_NAME, 'ZxXxWb')))


def testing_yandex_page(testing):
    WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.XPATH, '//a[@id="oidc_ya"]')))

    pytest.driver.find_element(By.XPATH, '//a[@id="oidc_ya"]').click()

    assert WebDriverWait(pytest.driver, 10).until(ec.presence_of_element_located((By.CLASS_NAME, 'Header')))

# python -m pytest -v --driver Chrome --driver-path theFinalTask28\Driver\chromedriver.exe tests\social_media_testing.py
