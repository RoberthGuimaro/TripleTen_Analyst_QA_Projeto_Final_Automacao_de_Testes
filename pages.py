import time
from selenium.webdriver.common.by import By
from helpers import retrieve_phone_code
from selenium.webdriver.support.ui import WebDriverWait

# Definição da classe da página, dos localizadores e do metodo na classe
class UrbanRoutesPage:
    # Localizadores como atributos de classe

    # LOCATION
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')

    # OPTION CAR
    PERSONAL_OPTION_LOCATOR = (By.XPATH, '//div[text()="Personal"]')
    CARSHARING_ICON_LOCATOR = (By.XPATH, '//img[@src="/static/media/taxi-active.b0be3054.svg"]')

    BOOK_BUTTON_LOCATOR = (By.XPATH, '//button[@class="button round"]')
    COMFORT_CARD_LOCATOR = (By.XPATH, '//div[contains(@class, "tcard") and .//img[@src="/static/media/kids.075fd8d4.svg"]]')
    COMFORT_LOCATOR = (By.XPATH, '//img[@src="/static/media/kids.075fd8d4.svg"]')

    # PHONE
    PHONE_NUMBER_CLICK = (By.XPATH, '//div[@class="np-text"]')
    PHONE_NUMBER = (By.ID, 'phone')
    HEAD_PHONE_NUMBER = (By.XPATH, '//div[@class="head"]')
    PHONE_BUTTON_NEXT = (By.XPATH, '//button[@class="button full"]')

    # PHONE CODE
    PHONE_CODE = (By.ID, 'code')
    HEAD_PHONE_CODE = (By.XPATH, '//div[@class="head"]')
    PHONE_BUTTON_CODE_CONFIRM = (By.XPATH, '//button[text()="Confirmar"]')

    # PAYMENT
    PAYMENT_METHOD_CLICK = (By.XPATH, '//div[@class="pp-text"]')
    ADD_CARD_CLICK = (By.XPATH, '//div[text()="Adicionar cartão"]')
    CARD_NUMBER = (By.XPATH, "//input[@id='number']")
    CARD_CODE = (By.XPATH, "//input[@id='code' and @name='code']")
    LABEL_CARD = (By.XPATH, "//div[@class='card-number-label']")
    CARD_BUTTON_CONFIRM = (By.XPATH, '//button[@class="button full" and contains(text(),"Adicionar")]')
    CARD_CLOSE_POPUP = (By.XPATH, "//div[@class='head' and text()='Método de pagamento']/preceding-sibling::button[contains(@class,'close-button')]")
    CHECKBOX_CARD_1 = (By.ID, 'card-1')

    # MESSAGE DRIVER
    MESSAGE_DRIVER = (By.ID, 'comment')

    # BEDDING
    BEDDING_SELECTION = (By.XPATH, "//div[text()='Cobertor e lençóis']/following-sibling::div//span[contains(@class, 'slider')]")
    BEDDING_CHECKBOX = (By.XPATH, "//div[text()='Cobertor e lençóis']/following-sibling::div//input")

    # ICECREAM
    ICE_CREAM_SELECTION = (By.XPATH, '//div[@class="counter-plus"]')
    ICE_CREAM_CHECK_QUANTITY = (By.XPATH, "//div[text()='Sorvete']/following-sibling::div//div[@class='counter-value']")

    # REQUEST A RIDE
    REQUEST_RIDE_BUTTON = (By.XPATH, '//button[@class="smart-button"]')
    CHECK_RIDE_REQUEST = (By.XPATH, '//div[@class="order-header-title"]')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 2)

    def set_route(self, from_text, to_text):
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_text)
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_text)

    def get_text_from(self):
        return self.driver.find_element(*self.FROM_LOCATOR).get_attribute('value')

    def get_text_to(self):
        return self.driver.find_element(*self.TO_LOCATOR).get_attribute('value')

    def select_plan(self):
        self.driver.find_element(*self.PERSONAL_OPTION_LOCATOR).click()
        self.driver.find_element(*self.CARSHARING_ICON_LOCATOR).click()
        self.driver.find_element(*self.BOOK_BUTTON_LOCATOR).click()
        if 'active' not in self.driver.find_element(*self.COMFORT_CARD_LOCATOR).get_attribute('class'):
            self.driver.find_element(*self.COMFORT_LOCATOR).click()

    def get_select_plan_comfort(self):
        return self.driver.find_element(*self.COMFORT_CARD_LOCATOR).get_attribute('class')

    def fill_phone_number(self, phone_number):
        self.driver.find_element(*self.PHONE_NUMBER_CLICK).click()
        self.driver.find_element(*self.PHONE_NUMBER).send_keys(phone_number)
        self.driver.find_element(*self.HEAD_PHONE_NUMBER).click()
        self.driver.find_element(*self.PHONE_BUTTON_NEXT).click()

        # chama a função para confirmar o código
        confirmation_code = retrieve_phone_code(self.driver)

        self.driver.find_element(*self.PHONE_CODE).send_keys(confirmation_code)
        self.driver.find_element(*self.PHONE_BUTTON_CODE_CONFIRM).click()

    def get_phone_number(self):
        return self.driver.find_element(*self.PHONE_NUMBER_CLICK).text

    def fill_card(self, card_number, card_code):
        self.driver.find_element(*self.PAYMENT_METHOD_CLICK).click()
        self.driver.find_element(*self.ADD_CARD_CLICK).click()
        self.driver.find_element(*self.CARD_NUMBER).send_keys(card_number)
        self.driver.find_element(*self.CARD_CODE).send_keys(card_code)
        self.driver.find_element(*self.LABEL_CARD).click()
        self.driver.find_element(*self.CARD_BUTTON_CONFIRM).click()
        self.driver.find_element(*self.CARD_CLOSE_POPUP).click()

    def get_fill_card(self):
        self.driver.find_element(*self.PAYMENT_METHOD_CLICK).click()
        return self.driver.find_element(*self.CHECKBOX_CARD_1).is_selected()

    def comment_for_drive(self, message):
        self.driver.find_element(*self.MESSAGE_DRIVER).send_keys(message)

    def get_comment_for_drive(self):
        return self.driver.find_element(*self.MESSAGE_DRIVER).get_attribute('value')

    def order_blanket_and_handkerciefs(self):
        self.driver.find_element(*self.BEDDING_SELECTION).click()

    def get_order_blanket_and_handkerciefs(self):
        return self.driver.find_element(*self.BEDDING_CHECKBOX).is_selected()

    def order_2_ice_creams(self):
        for _ in range(2):
            self.driver.find_element(*self.ICE_CREAM_SELECTION).click()

    def get_order_2_ice_creams(self):
        return self.driver.find_element(*self.ICE_CREAM_CHECK_QUANTITY).text

    def car_search_model_appers(self):
        self.driver.find_element(*self.REQUEST_RIDE_BUTTON).click()
        time.sleep(2)

    def get_car_search_model_appers(self):
        return self.driver.find_element(*self.CHECK_RIDE_REQUEST).text

