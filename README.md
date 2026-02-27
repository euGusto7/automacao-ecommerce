# 🧪 Automação E2E – SauceDemo

Framework de automação de testes End-to-End desenvolvido em **Python** , utilizando:

- 🐍 Python
- 🌐 Selenium WebDriver
- 🥒 Behave (BDD)
- 📊 Allure Reports
- 🏗 Page Object Model (POM)

---

# 📌 Objetivo

Automatizar os principais fluxos do e-commerce **SauceDemo** , garantindo:

- Validação de login
- Testes funcionais de UI
- Estrutura escalável
- Relatórios profissionais
- Facilidade de manutenção

---

# 🏗 Arquitetura do Projeto

<pre class="overflow-visible! px-0!" data-start="746" data-end="1035"><div class="relative w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>automacao-ecommerce/</span><br/><span>│</span><br/><span>├── features/</span><br/><span>│   ├── login.feature</span><br/><span>│   ├── steps/</span><br/><span>│   │   └── login_steps.py</span><br/><span>│   └── environment.py</span><br/><span>│</span><br/><span>├── pages/</span><br/><span>│   └── login_page.py</span><br/><span>│</span><br/><span>├── reports/</span><br/><span>│   └── allure-results/</span><br/><span>│</span><br/><span>├── config/</span><br/><span>│   └── config.py</span><br/><span>│</span><br/><span>├── behave.ini</span><br/><span>├── requirements.txt</span><br/><span>└── README.md</span></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

# 🧠 Padrões Utilizados

## ✅ Page Object Model (POM)

Separação clara entre:

- Camada de teste (Steps)
- Camada de página (Pages)
- Configuração
- Hooks

Isso melhora:

- Reutilização
- Organização
- Manutenção

---

## ✅ BDD com Behave

Exemplo de cenário:

<pre class="overflow-visible! px-0!" data-start="1303" data-end="1561"><div class="relative w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>Feature: Login no sistema</span><br/><br/><span>  Scenario: Login com sucesso</span><br/><span>    Given que o usuário está na página de login</span><br/><span>    When ele informa usuário e senha válidos</span><br/><span>    And clica no botão de login</span><br/><span>    Then ele deve ser redirecionado para a página de produtos</span></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

# ⚙️ Configuração do Ambiente

## 1️⃣ Criar ambiente virtual

<pre class="overflow-visible! px-0!" data-start="1630" data-end="1661"><div class="relative w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>python </span><span class="ͼu">-m</span><span> venv venv</span></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

## 2️⃣ Ativar o ambiente

### Windows:

<pre class="overflow-visible! px-0!" data-start="1702" data-end="1735"><div class="relative w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>venv\Scripts\activate</span></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

### Linux/Mac:

<pre class="overflow-visible! px-0!" data-start="1752" data-end="1788"><div class="relative w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span class="ͼs">source</span><span> venv/bin/activate</span></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

## 3️⃣ Instalar dependências

<pre class="overflow-visible! px-0!" data-start="1825" data-end="1868"><div class="relative w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>pip install </span><span class="ͼu">-r</span><span> requirements.txt</span></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

# 🔐 Variáveis de Ambiente

O projeto usa variáveis via `.env` ou variáveis do sistema:

<pre class="overflow-visible! px-0!" data-start="1964" data-end="2149"><div class="relative w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span class="ͼt">BASE_URL</span><span></span><span class="ͼn">=</span><span></span><span class="ͼt">os</span><span class="ͼn">.</span><span>getenv(</span><span class="ͼr">"BASE_URL"</span><span>, </span><span class="ͼr">""</span><span>)</span><br/><span class="ͼt">USERNAME</span><span></span><span class="ͼn">=</span><span></span><span class="ͼt">os</span><span class="ͼn">.</span><span>getenv(</span><span class="ͼr">"TEST_USERNAME"</span><span>, </span><span class="ͼr">""</span><span>)</span><br/><span class="ͼt">PASSWORD</span><span></span><span class="ͼn">=</span><span></span><span class="ͼt">os</span><span class="ͼn">.</span><span>getenv(</span><span class="ͼr">"TEST_PASSWORD"</span><span>, </span><span class="ͼr">""</span><span>)</span></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

Você pode definir no sistema:

<pre class="overflow-visible! px-0!" data-start="2182" data-end="2256"><div class="relative w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span class="ͼn">set</span><span></span><span class="ͼt">TEST_USERNAME</span><span class="ͼn">=</span><span></span><br/><span class="ͼn">set</span><span></span><span class="ͼt">TEST_PASSWORD</span><span class="ͼn">=</span><span></span></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

Ou criar um `.env`.

---

# 🚀 Executando os Testes

<pre class="overflow-visible! px-0!" data-start="2311" data-end="2329"><div class="relative w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>behave</span></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

# 📊 Allure Reports

## Gerar resultados

<pre class="overflow-visible! px-0!" data-start="2378" data-end="2465"><div class="relative w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>behave </span><span class="ͼu">-f</span><span> allure_behave.formatter:AllureFormatter </span><span class="ͼu">-o</span><span> reports/allure-results</span></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

ou usando `behave.ini` configurado:

<pre class="overflow-visible! px-0!" data-start="2504" data-end="2522"><div class="relative w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>behave</span></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

## Abrir relatório

<pre class="overflow-visible! px-0!" data-start="2549" data-end="2596"><div class="relative w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>allure serve reports/allure-results</span></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

# 🧾 Exemplo de Configuração do behave.ini

<pre class="overflow-visible! px-0!" data-start="2647" data-end="2839"><div class="relative w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>[behave]</span><br/><span>default_format = pretty</span><br/><span>format = allure_behave.formatter:AllureFormatter</span><br/><span>outfiles = reports/allure-results</span><br/><span>stdout_capture = false</span><br/><span>stderr_capture = false</span><br/><span>log_capture = false</span></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

# 🧪 Boas Práticas Implementadas

- ✔ Estrutura modular
- ✔ Separação de responsabilidades
- ✔ Configuração centralizada
- ✔ Suporte a headless mode
- ✔ Logs informativos
- ✔ Integração com Allure
- ✔ Preparado para CI/CD

---

# 🛠 Possíveis Melhorias Futuras

- 🔥 Screenshot automático em falha
- 🔥 Execução paralela
- 🔥 Integração com GitHub Actions
- 🔥 Pipeline CI
- 🔥 Dockerização
- 🔥 Multi-browser support
- 🔥 Testes negativos
- 🔥 Tags por severidade

---

# 🐞 Troubleshooting

## ❌ Erro: `Context object has no attribute 'driver'`

Verifique se o `environment.py` está inicializando o WebDriver corretamente no `before_scenario`.

---

## ❌ Erro: `allure: command not found`

Instalar Allure CLI e adicionar ao PATH do sistema.

---

# 📦 Requirements Exemplo

<pre class="overflow-visible! px-0!" data-start="3623" data-end="3689"><div class="relative w-full my-4"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>behave==1.2.6</span><br/><span>selenium</span><br/><span>allure-behave==2.13.2</span><br/><span>python-dotenv</span></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

# 👨‍💻 Autor

Guilherme Silva

QA Automation Engineer
