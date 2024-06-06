class Header:
    def __init__(self,page):
        self.page = page
        self.botao_login = "a[href ='/login']"

    def clicar_botao_login(self):
        self.page.locator(self.botao_login).click()


        