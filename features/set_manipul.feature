Feature: Set Manipulation of addition of Elements
  Here we are checking the usage of but using the Set Manipulation

  Scenario: set addition manipulation
    Given i have 3 fruits in the set
    When we add elements which are already present
    Then size of the set remain constant
    But when we add a new unique element
    Then the size of the set will be 4
