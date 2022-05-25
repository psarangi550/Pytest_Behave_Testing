Feature: checking the About Page of HRM web page
    Test will check the About page will be displayed in Dashboard or not
  Scenario: Access About Page of Orange HRM homepage
    Given Open the Edge Browser Driver
    When Open the Orange HRM homepage
    And Enter the Username and Password
    And click the login Button
    And click on the Profile Option
    And click on the About option of the Profile
    Then validate the About Page been displayed or not
    And close or quit the browser
    
