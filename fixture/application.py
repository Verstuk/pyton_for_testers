from selenium import webdriver
from selenium.webdriver.support.ui import Select
from fixture.session import SessionHelper

class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
        self.session = SessionHelper(self)


    def credit_form_case_1(self, group):
        driver = self.driver
        driver.find_element_by_name("field-desired-loan").clear()
        driver.find_element_by_name("field-desired-loan").send_keys(group.loan)
        driver.find_element_by_name("field-initial-payment").clear()
        driver.find_element_by_name("field-initial-payment").send_keys(group.payment)
        driver.find_element_by_name("field-credit-term").clear()
        driver.find_element_by_name("field-credit-term").send_keys(group.term)

    def credit_form_case_2(self, group):
        driver = self.driver
        driver.find_element_by_name("field-desired-loan").clear()
        driver.find_element_by_name("field-desired-loan").send_keys(group.loan)
        driver.find_element_by_name("field-initial-payment").clear()
        driver.find_element_by_name("field-initial-payment").send_keys(group.payment)
        driver.find_element_by_name("field-credit-term").clear()
        driver.find_element_by_name("field-credit-term").send_keys(group.term)
        driver.find_element_by_class_name("btn-primary").click()
        driver.find_element_by_link_text(u"заполните анкету").click()

        driver.find_element_by_name("second-name").click()
        driver.find_element_by_name("second-name").clear()
        driver.find_element_by_name("second-name").send_keys(u"Иванов")
        driver.find_element_by_name("first-name").click()
        driver.find_element_by_name("first-name").clear()
        driver.find_element_by_name("first-name").send_keys(u"Иван")
        driver.find_element_by_name("middle-name").click()
        driver.find_element_by_name("middle-name").clear()
        driver.find_element_by_name("middle-name").send_keys(u"Иванович")
        driver.find_element_by_name("passport").click()
        driver.find_element_by_name("passport").clear()
        driver.find_element_by_name("passport").send_keys("4099 123456")
        driver.find_element_by_name("issued-by").click()
        driver.find_element_by_name("issued-by").clear()
        driver.find_element_by_name("issued-by").send_keys(u"64 ом")
        driver.find_element_by_name("issued-date").click()
        driver.find_element_by_name("issued-date").clear()
        driver.find_element_by_name("issued-date").send_keys("12.02.1975")
        driver.find_element_by_name("education").click()
        Select(driver.find_element_by_name("education")).select_by_visible_text(u"Высшее")
        driver.find_element_by_name("education").click()
        driver.find_element_by_name("seniority").click()
        Select(driver.find_element_by_name("seniority")).select_by_visible_text(u"5 лет - 10 лет")
        driver.find_element_by_name("seniority").click()
        driver.find_element_by_name("term-work-last-place").click()
        Select(driver.find_element_by_name("term-work-last-place")).select_by_visible_text(u"Более 3 лет")
        driver.find_element_by_name("term-work-last-place").click()
        driver.find_element_by_name("confirmation-income-ndfl").click()
        Select(driver.find_element_by_name("confirmation-income-ndfl")).select_by_visible_text(u"Да")
        driver.find_element_by_name("confirmation-income-ndfl").click()
        driver.find_element_by_name("work-place-bank-area").click()
        Select(driver.find_element_by_name("work-place-bank-area")).select_by_visible_text(u"Да")
        driver.find_element_by_name("work-place-bank-area").click()
        driver.find_element_by_name("net-income").click()
        driver.find_element_by_name("net-income").clear()
        driver.find_element_by_name("net-income").send_keys("30000")
        driver.find_element_by_name("registration-place-bank-area").click()
        Select(driver.find_element_by_name("registration-place-bank-area")).select_by_visible_text(u"Да")
        driver.find_element_by_name("registration-place-bank-area").click()
        driver.find_element_by_name("previous-conviction").click()
        Select(driver.find_element_by_name("previous-conviction")).select_by_visible_text(u"Нет")
        driver.find_element_by_name("previous-conviction").click()
        driver.find_element_by_name("car").click()
        driver.find_element_by_name("car").click()
        driver.find_element_by_name("real-estate").click()
        Select(driver.find_element_by_name("real-estate")).select_by_visible_text(u"Да")
        driver.find_element_by_name("real-estate").click()




    def destroy(self):
        self.driver.quit()