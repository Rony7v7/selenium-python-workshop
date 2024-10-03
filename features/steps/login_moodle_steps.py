from behave import given, when, then
from selenium import webdriver
from pages.login_moodle_page import MoodleLoginPage
from pages.dashboard_page import DashboardPage
from selenium.webdriver.common.by import By

@given('the user is on the login page in moodle')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get('https://www.icesi.edu.co/moodle/login/index.php')
    context.login_page = MoodleLoginPage(context.driver)

@when('the user logs in with valid credentials in moodle')
def step_impl(context):
    context.login_page.login("","")
    
@then('the user should be redirected to the dashboard page in moodle')
def step_impl(context):
    dashboard_page = DashboardPage(context.driver)
    assert dashboard_page.is_dashboard_page_displayed()

    
def after_scenario(context, scenario):
    context.driver.quit()
    









































