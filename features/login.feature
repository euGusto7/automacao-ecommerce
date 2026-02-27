Feature: Login no sistema

    Scenario: Login com sucesso
        Given que o usuário está na página de login
        When ele informa usuário e senha válidos
        And clica no botão de login
        Then ele deve ser redirecionado para a página de produtos
