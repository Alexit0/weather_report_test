import pytest

from utilities.BaseClass import BaseClass
from page_objects.HomePage import HomePage
from page_objects.LocationPage import LocationPage

from selenium.webdriver.common.by import By
from test_data.HopePageData import HomePageData


class TestClass(BaseClass):
    @pytest.fixture(params=HomePageData.test_data)
    def get_data(self, request):
        return request.param

    def test_e2e_weather(self, get_data):
        log = self.get_logger()
        home_page = HomePage(self.driver)
        home_page.reject_cookies()
        log.info("Rejected cookies")
        home_page.search_location_input().send_keys(get_data["CITY_NAME"])
        self.verify_element_presence_by_xpath(
            "//div[@class='search-results']/div/div[contains(text(), 'Kaunas')]")
        location_page = LocationPage(self.driver)
        location_page.scroll_to_the_top()
        data = location_page.get_current_weather()
        log.info("LOGGING TODAY'S WEATHER >>> ")
        for key in data:
            log.info(key + ':' + data[key])

        weekly_report_page = location_page.get_daily_forecast()
        forecast = weekly_report_page.get_weekly_forecast()
        log.info('LOGGING FORECAST FOR THE UPCOMING WEEK ... ')
        for element in forecast[:7]:
            weekday = element.find_element(By.XPATH, "a/div/h2/span[1]").text
            day = element.find_element(By.XPATH, "a/div/h2/span[2]").text
            temp_high = element.find_element(By.XPATH, "a/div/div/span[1]").text
            temp_low = element.find_element(By.XPATH, "a/div/div/span[2]").text

            log.info(weekday + '(' + day + ') :: Temp: ' + temp_high + temp_low)






