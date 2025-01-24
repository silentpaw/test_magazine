import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption(
        "--language", action="store", default="en", help="Choose language: es, fr, ru, etc."
    )

@pytest.fixture(scope="function")
def browser(request):
    # Получаем язык из аргументов командной строки
    language = request.config.getoption("language")
    
    # Настройка Chrome с указанным языком
    print("\nStarting Chrome browser for test...")
    options = Options()
    options.add_argument(f"--lang={language}")  # Устанавливаем язык для Chrome
    browser = webdriver.Chrome(options=options)

    yield browser  # Возвращаем браузер для использования в тестах
    print("\nQuitting browser...")
    browser.quit()  # Закрываем браузер после завершения теста

  