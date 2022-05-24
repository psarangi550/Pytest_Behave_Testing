Feature: Performing set manipulation operations
    checking the remove by pop method working or not working
  Scenario: set manipulation operation
    Given initialize the set using text_fixture
    When remove one element from the set
    Then checking the length of the set