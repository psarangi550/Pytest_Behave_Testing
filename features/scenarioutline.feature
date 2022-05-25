Feature: Banking Application using Scenario Outline
  Here we are performing deposit and Withdraw for banking application

  Scenario Outline: Testing Banking deposit and withdraw functionality
    Given Bank Starting  Balance amount is <start>
    When A Deposit made with <depo> Amount
    And A withdraw also made with <withdraw> Amount
    Then Total final balance is <final>
    Examples:
      | start | depo | withdraw | final |
      | 1000  | 2000 | 1500     | 1500  |
      | 5000  | 6000 | 9000     | 2000  |