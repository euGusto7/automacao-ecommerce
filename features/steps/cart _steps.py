from behave import given, when, then
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from time import sleep
from core.config import Config

import logging
import allure

log = logging.getLogger(__name__)


@given("que o usuário está logado")
def step_user_logged(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open(Config.BASE_URL)
    context.login_page.login(Config.USERNAME, Config.PASSWORD)


@when('eu clico no botão "Adicionar ao Carrinho"')
def step_click_add_to_cart(context):
    log.info('Clicando no botão "Adicionar ao Carrinho"...')

    try:
        context.cart_page = CartPage(context.driver)
        context.cart_page.add_product()
    except Exception as e:
        log.error(f'Erro ao clicar no botão "Adicionar ao Carrinho": {e}')
        raise e


@then("o produto deve ser adicionado ao carrinho")
def step_validate_cart(context):

    try:
        context.cart_page = CartPage(context.driver)
        context.cart_page.open_cart()
        screenshot = context.driver.get_screenshot_as_png()

        allure.attach(
            screenshot, name="Carrinho", attachment_type=allure.attachment_type.PNG
        )
        sleep(5)
    except Exception as e:
        log.error(f"Erro ao abrir o carrinho: {e}")
        raise e
    assert "cart" in context.driver.current_url
