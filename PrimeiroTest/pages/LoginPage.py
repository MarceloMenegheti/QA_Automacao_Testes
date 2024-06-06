class Login:
    def __init__(self,page):
        self.campo_email = "input[data-qa='login-email']"
        self.campo_senha = "input[data-qa='login-password']"
        self.botao_login = "button[data-qa='login-button']"
        self.msg_erro = "form[action='/login'] p"

    def realizar_login(self,email, senha):
        self.page.locator(self.campo_email).fill(email)
        self.page.locator(self.campo_senha).fill(senha)

        self.page.locator(self.botao_login).click()

    def return_msg_error(self):

        error = error


