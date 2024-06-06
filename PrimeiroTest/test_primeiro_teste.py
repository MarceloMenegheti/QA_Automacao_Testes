from playwrite.sync_api import Playwrigth, Page, expect

#https://automationexercise.com
class TestSuite():
    @pytest.fixture(autouse=True)
    def setup(self, playwrite: Playwrigth):
        self.pw = playwrite
        self.browser = self.playwrite.chromium.launch(headless=False)
        self.context = browser.new_context()
        self.page = contexto.new_page()
        self.base_url = "https://automationexercise.com/login"


    def test_primeiro_teste(self):
        
        self.page.goto(base_url)

        elemento_login = page.locator(".login-form h2")

        expect(elemento_login).to_have_text("Login to your account")