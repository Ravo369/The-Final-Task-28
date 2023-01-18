import pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('\\C:\\Users\\HP\\PycharmProjects\\theFinalTask28'
                                     '\\Driver\\chromedriver.exe')

    # Переходим на страницу авторизации
    pytest.driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/'
                      'auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/'
                      'account_b2c/login&response_type=code&scope=openid&state=88684b8a-e6fb-'
                      '4a62-9d29-80f64e5d7e3c&theme&auth_type')

    yield

    pytest.driver.quit()
