Feature: Adicionar produto ao carrinho

    Scenario: Adicionar um produto ao carrinho
        Given que o usuário está logado
        When eu clico no botão "Adicionar ao Carrinho"
        Then o produto deve ser adicionado ao carrinho
