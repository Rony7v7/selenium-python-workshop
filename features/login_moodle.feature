Feature: Login in moodel Feature
  Scenario: Successful login with valid credentials
    Given the user is on the login page in moodle
    When the user logs in with valid credentials in moodle
    Then the user should be redirected to the dashboard page in moodle
