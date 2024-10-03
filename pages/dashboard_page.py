from selenium.webdriver.common.by import By
from .base_page import BasePage

class DashboardPage(BasePage):
    TOP_BAR = (By.CLASS_NAME, 'topBar')
    
    def is_dashboard_page_displayed(self):
        return self.find_element(self.TOP_BAR).is_displayed()