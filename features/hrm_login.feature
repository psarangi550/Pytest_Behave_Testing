Feature: checking Login Page of HRM web page
  Scenario: Access the Login page
    Given Open Brave Browser
    When Open the Orange HRM
    And Enter the Username as admin and Password as admin123
    And click the login
    Then verify dashboard is getting open or not after login
    And close the Brave browser