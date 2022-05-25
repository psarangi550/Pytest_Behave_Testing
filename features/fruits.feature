Feature: Checking the Parameterize example by pytest_bdd
    Here we are parameterizing the step definition by using dictionary value
  Scenario: parser to parameterize the pytest_bdd
    Given I have 5 Fruites
    When I eat 3 Fruites
    And I eat 2 Fruites
    Then I have now 0 Fruites in the basket
