from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def accept_cookies(self):
        return self.driver.find_element(By.CSS_SELECTOR, "fc-primary-button").click()

    def reject_cookies(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".fc-cta-do-not-consent").click()

    def search_location_input(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".search-input")

