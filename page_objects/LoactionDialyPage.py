from selenium.webdriver.common.by import By


class LocationDailyPage:
    def __init__(self, driver):
        self.driver = driver

    def get_weekly_forecast(self):
        return self.driver.find_elements(By.XPATH, "//div[@class='daily-wrapper']")

