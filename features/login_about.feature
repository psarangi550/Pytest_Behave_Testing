Feature: checking the Login and About Page of HRM web page
  Test will check the About page will be displayed in Dashboard or not

  Background:common Task
    Given Open the Brave Browser Driver
    And Open the Orange HRM homepage
    And Enter the Username and Password
    And click the login Button

  Scenario: Access the Login page of Orange HRM homepage
    Then verify dashboard is getting open or not
    And close or quit the Brave browser


  Scenario: Access About Page of Orange HRM homepage
    When click on the Profile Option
    And click on the About option of the Profile
    Then validate the About Page been displayed or not
    And close or quit the browser