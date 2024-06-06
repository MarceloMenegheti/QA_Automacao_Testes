import pytest
from playwrite.sync_api import Playwrigth, Page, expect

from HeaderComponent import Header
from LoginPage import Login

#https://automationexercise.com
class TestSuite():
    @pytest.fixture(autouse=True)
    def setup(self, playwrite: Playwrigth):
        self.pw = playwrite
        self.browser = self.playwrite.chromium.launch(headless=False)
        self.context = browser.new_context()
        self.page = contexto.new_page()
        self.base_url = "https://automationexercise.com/login"


    def test_login_funcionando(self):
        self.page.goto(self.base_url)

        header = Header(self.page)
        login = Login(self.page)
        header.clicar_botao_login()

        login.realizar_login("marceloo@gmail.com","12345678")


  def test_login_nao_funcionando(self):
        self.page.goto(self.base_url)

        header = Header(self.page)
        login = Login(self.page)

        header.clicar_botao_login()

        login.realizar_login("marceloo@gmail.com","test")
        msg_error = login.return_msg_error()

        expect(msg_error).to_have_text("Your password is incorrect!")