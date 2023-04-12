import pytest
import logging
import inspect

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class BaseClass:
    def get_logger(self):
        logger = logging.getLogger(inspect.stack()[1][3])
        file_handler = logging.FileHandler("logfile.log", mode='w')
        file_handler.setFormatter(logging.Formatter("%(asctime)s : "
                                                    "%(levelname)s : "
                                                    "%(name)s : "
                                                    "%(message)s"))

        if logger.hasHandlers():
            logger.handlers.clear()
        logger.addHandler(file_handler)
        logger.setLevel(logging.DEBUG)
        return logger

    def verify_element_presence_by_xpath(self, element: str):
        """Must provide XPATH as an argument"""
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, element))).click()

    def verify_element_presence_by_css(self, element: str):
        """Must provide CSS as an argument"""
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, element)))



