Feature:Set Manipulation Tagging Example Testing
  Manipulating set Operation

  @newscenario
  Scenario: set addition manipulation
    Given i have 3 fruits in the basket
    When we add similar elements which are already present
    Then size of the set remain same
    But when we add a unique new element to set
    Then the size of the set will be 4