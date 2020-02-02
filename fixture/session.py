

class SessionHelper:

    def __init__(self, app):
        self.app = app

    def open_page(self):
        driver = self.app.driver
        driver.get("http://creditcalculator.pointschool.ru/credit/")

    def submit(self):
        driver = self.app.driver
        driver.find_element_by_class_name("btn-primary").click()