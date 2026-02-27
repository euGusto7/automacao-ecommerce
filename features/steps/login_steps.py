from behave import given, when, then
from pages.login_page import LoginPage
from time import sleep
from core.config import Config

import logging, allure

log = logging.getLogger(__name__)


@given("que o usuário está na página de login")
def step_open_login(context):
    log.info("Abrindo a página de login...")

    try:
        context.login_page = LoginPage(context.driver)
    except Exception as e:
        log.error(f"Erro ao criar instância da página de login: {e}")
        raise e
    context.login_page.open(Config.BASE_URL)

    log.info("Página de login aberta com sucesso.")


@when("ele informa usuário e senha válidos")
def step_fill_credentials(context):
    log.info("Preenchendo as credenciais de login...")

    try:
        context.login_page.login(Config.USERNAME, Config.PASSWORD)
    except Exception as e:
        log.error(f"Erro ao preencher credenciais: {e}")
        raise e


@when("clica no botão de login")
def step_click_login(context):
    pass


@then("ele deve ser redirecionado para a página de produtos")
def step_validate_inventory(context):
    sleep(5)

    screenshot = context.driver.get_screenshot_as_png()

    allure.attach(screenshot, name="Login", attachment_type=allure.attachment_type.PNG)

    assert "inventory" in context.driver.current_url
