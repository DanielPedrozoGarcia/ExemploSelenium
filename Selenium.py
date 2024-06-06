from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

def fn_BuscaElemento(Tempo,NomeCampo,Estrategia,ID):
    wait = WebDriverWait(browser, Tempo)
    NomeCampo = wait.until(EC.visibility_of_element_located((Estrategia, ID)))
    return NomeCampo

# URL da página de login
url = "https://app.powerbi.com/groups/me/list?redirectedFromSignup=1&experience=power-bi"

# Lista de emails
emails = [
    "teste@chandlerbing.onmicrosoft.com"
]

# Dicionário para armazenar os resultados
resultados = {}

# Iterar sobre os emails
for email in emails:
    try:
        # Inicializa o navegador
        browser = webdriver.Chrome()

        # Abre a página de login
        browser.get(url)

        # Inserir email
        Email = fn_BuscaElemento(5,"Email",By.ID,"i0116")
        Email.send_keys(email)

        # Clica em avançar
        login_button = browser.find_element(By.ID, "idSIButton9")
        login_button.click()

        # Inserir senha
        Senha = fn_BuscaElemento(5,"Senha",By.ID,"i0118")
        Senha.send_keys("DSH8721@1")

        # Clica em entrar
        login_button = browser.find_element(By.ID, "idSIButton9")
        login_button.click()

        # Clicar em entrar
        login_button = fn_BuscaElemento(2,"Login",By.ID,"idSIButton9")
        login_button.click()

        # Verifica se há algum componente na página antes de recarregar
        try:
            # Procura por algum componente na página
            componente = fn_BuscaElemento(5,"BotaoInserir",By.XPATH, "//button[@aria-label='New report']")
            if componente:
                # Se o componente for encontrado, recarrega a página
                time.sleep(1)
                browser.refresh()
            else:
                # Se o componente não for encontrado, continua aguardando
                while not componente:
                    componente = fn_BuscaElemento(5,"BotaoInserir",By.XPATH, "//button[@aria-label='New report']")
        except TimeoutException:
            # Se ocorrer um TimeoutException, significa que o componente não foi encontrado
            print("O componente não foi encontrado. Continuando aguardando...")

        # Clica em Workspaces
        Workspaces = fn_BuscaElemento(5,"Workspaces",By.XPATH,"/html/body/div[1]/root/mat-sidenav-container/mat-sidenav-content/tri-shell-panel-outlet/tri-item-renderer-panel/tri-extension-panel-outlet/mat-sidenav-container/mat-sidenav-content/div/app-navigation-pane/tri-nav-pane/tri-host-navbar/div/div/tri-workspace-switcher/tri-navbar-label-item/button/div")
        Workspaces.click()

        # Workspace do cliente
        BarraLateral = fn_BuscaElemento(5,"BarraLateral",By.XPATH,"//tri-workspace-button[@class='workspace-list-item tri-flex tri-items-center ng-star-inserted']")
        BotaoWorkspaceCliente = fn_BuscaElemento(5,"BotaoWorkspaceCliente",By.XPATH,".//button[@class='workspace-button-left tri-rounded tri-text-left tri-flex tri-flex-auto tri-items-center']")
        BotaoWorkspaceCliente.click()

        try:
            # Botao Got It
            PoupUp = fn_BuscaElemento(1,"PoupUp",By.XPATH,"/html/body/div[2]/div[4]/div/mat-dialog-container/div/div")
            BotaoGotIt = fn_BuscaElemento(1,"BotaoGotIt",By.XPATH,"/html/body/div[2]/div[4]/div/mat-dialog-container/div/div/simple-dialog/dialog-footer/mat-dialog-actions/div[2]/button[1]")
            if BotaoGotIt:
                BotaoGotIt.click()  
            else:
                browser.quit()
        except TimeoutException:
            browser.quit()
        
        # Armazenar resultado como sucesso
        resultados[email] = "Sucesso"
        
    except Exception as e:
        # Armazenar resultado como falha
        resultados[email] = "\033[91mFalha\033[0m"

    browser.quit()

# Imprimir resultados
for email, resultado in resultados.items():
    print(f"{email}: {resultado}")