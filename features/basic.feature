Feature: Testing the Banking Functionality for Withdraw
    Here we will test the functionality of withdraw of banking system
  Scenario: Testing Banking withdraw application
    Given setting the balance to 100 Dollar
    When when withdraw 30 Dollar
    Then Remaining balance is 70 Dollar
