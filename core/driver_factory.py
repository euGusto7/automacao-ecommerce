from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def create_driver():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")

    chrome_options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
        },
    )

    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome(options=chrome_options)

    return driver
