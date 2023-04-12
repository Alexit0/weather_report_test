from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from page_objects.LoactionDialyPage import LocationDailyPage


class LocationPage:
    def __init__(self, driver):
        self.driver = driver

    def scroll_to_the_top(self):
        return self.driver.execute_script("scrollTo(0, 0)")

    def get_current_weather(self):
        data = {}
        data["Current Time:"] = self.driver.find_element(By.CSS_SELECTOR, "p.cur-con-weather-card__subtitle").text
        data["Current Weather"] = self.driver.find_element(By.CSS_SELECTOR, "div.cur-con-weather-card__panel>div>div>div.temp").text
        data["Weather Details"] = self.driver.find_element(By.CSS_SELECTOR, "span.phrase").text
        return data

    def get_daily_forecast(self):
        self.driver.execute_script("scrollTo(0, 2300)")
        element = self.driver.find_element(By.XPATH, "//h3[.='Daily']")
        ActionChains(self.driver).move_to_element(element).click().perform()
        return LocationDailyPage(self.driver)





