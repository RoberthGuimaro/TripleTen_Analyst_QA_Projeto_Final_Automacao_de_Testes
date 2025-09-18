# Importa módulos
import data, helpers
from pages import UrbanRoutesPage
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

# Classe de testes do aplicativo Urban Routes
class TestUrbanRoutes:
    @classmethod
    # Faz a chamada do servidor e verifica se está online ou offline
    def setup_class(cls):
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes")
        else:
            print('Não foi possível conectar ao Urban Routes. '
                  'Verifique se o servidor está ligado e ainda em execução')

        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}

        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        cls.driver = webdriver.Chrome(options=options)


    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        self.urban_routes_page = UrbanRoutesPage(self.driver)
        # Adicione esperas implícitas para que os elementos da web tenham tempo de carregar
        self.driver.implicitly_wait(3)

        self.urban_routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)

        assert self.urban_routes_page.get_text_from() == data.ADDRESS_FROM and self.urban_routes_page.get_text_to() == data.ADDRESS_TO, f"{self.urban_routes_page.get_text_from()} / {data.ADDRESS_FROM} e {self.urban_routes_page.get_text_to()} / {data.ADDRESS_TO}"

        print(f"O teste passou. Uhul!!!")

    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        self.urban_routes_page = UrbanRoutesPage(self.driver)
        # Adicione esperas implícitas para que os elementos da web tenham tempo de carregar
        self.driver.implicitly_wait(3)
        self.urban_routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.driver.implicitly_wait(2)

        self.urban_routes_page.select_plan()

        assert 'active' in  self.urban_routes_page.get_select_plan_comfort()

        print('O teste passou. Uhul!!!')

    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        self.urban_routes_page = UrbanRoutesPage(self.driver)
        # Adicione esperas implícitas para que os elementos da web tenham tempo de carregar
        self.driver.implicitly_wait(3)
        self.urban_routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.driver.implicitly_wait(2)
        self.urban_routes_page.select_plan()

        self.urban_routes_page.fill_phone_number(data.PHONE_NUMBER)

        assert data.PHONE_NUMBER == self.urban_routes_page.get_phone_number()

        print('Oteste passou. Uhul!!!')

    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        self.urban_routes_page = UrbanRoutesPage(self.driver)
        # Adicione esperas implícitas para que os elementos da web tenham tempo de carregar
        self.driver.implicitly_wait(3)
        self.urban_routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.driver.implicitly_wait(2)
        self.urban_routes_page.select_plan()
        self.urban_routes_page.fill_phone_number(data.PHONE_NUMBER)

        self.urban_routes_page.fill_card(data.CARD_NUMBER, data.CARD_CODE)

        assert self.urban_routes_page.get_fill_card()

        print('O teste passou. Uhul!!!')

    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        self.urban_routes_page = UrbanRoutesPage(self.driver)
        # Adicione esperas implícitas para que os elementos da web tenham tempo de carregar
        self.driver.implicitly_wait(3)
        self.urban_routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.driver.implicitly_wait(2)
        self.urban_routes_page.select_plan()
        self.urban_routes_page.fill_phone_number(data.PHONE_NUMBER)
        self.urban_routes_page.fill_card(data.CARD_NUMBER, data.CARD_CODE)

        self.urban_routes_page.comment_for_drive(data.COMMENT_TO_DRIVER)

        assert data.COMMENT_TO_DRIVER == self.urban_routes_page.get_comment_for_drive()

        print(f'O teste passou. Uhul!!!')

    def test_order_blanket_and_handkerciefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        self.urban_routes_page = UrbanRoutesPage(self.driver)
        # Adicione esperas implícitas para que os elementos da web tenham tempo de carregar
        self.driver.implicitly_wait(3)
        self.urban_routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.driver.implicitly_wait(2)
        self.urban_routes_page.select_plan()
        self.urban_routes_page.fill_phone_number(data.PHONE_NUMBER)
        self.urban_routes_page.fill_card(data.CARD_NUMBER, data.CARD_CODE)
        self.urban_routes_page.comment_for_drive(data.COMMENT_TO_DRIVER)

        self.urban_routes_page.order_blanket_and_handkerciefs()

        assert self.urban_routes_page.get_order_blanket_and_handkerciefs()

        print(f'O teste passou. Uhul!!!')

    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        self.urban_routes_page = UrbanRoutesPage(self.driver)
        # Adicione esperas implícitas para que os elementos da web tenham tempo de carregar
        self.driver.implicitly_wait(3)
        self.urban_routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.driver.implicitly_wait(2)
        self.urban_routes_page.select_plan()
        self.urban_routes_page.fill_phone_number(data.PHONE_NUMBER)
        self.urban_routes_page.fill_card(data.CARD_NUMBER, data.CARD_CODE)
        self.urban_routes_page.comment_for_drive(data.COMMENT_TO_DRIVER)
        self.urban_routes_page.order_blanket_and_handkerciefs()

        self.urban_routes_page.order_2_ice_creams()

        assert self.urban_routes_page.get_order_2_ice_creams() == "2"

        print(f'O teste passou. Uhul!!!')

    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        self.urban_routes_page = UrbanRoutesPage(self.driver)
        # Adicione esperas implícitas para que os elementos da web tenham tempo de carregar
        self.driver.implicitly_wait(3)
        self.urban_routes_page.set_route(data.ADDRESS_FROM, data.ADDRESS_TO)
        self.driver.implicitly_wait(2)
        self.urban_routes_page.select_plan()
        self.urban_routes_page.fill_phone_number(data.PHONE_NUMBER)
        self.urban_routes_page.fill_card(data.CARD_NUMBER, data.CARD_CODE)
        self.urban_routes_page.comment_for_drive(data.COMMENT_TO_DRIVER)
        self.urban_routes_page.order_blanket_and_handkerciefs()
        self.urban_routes_page.order_2_ice_creams()

        self.urban_routes_page.car_search_model_appers()

        assert data.CAR_WAIT in self.urban_routes_page.get_car_search_model_appers()

        print(f'O teste passou. Uhul!!!')

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()