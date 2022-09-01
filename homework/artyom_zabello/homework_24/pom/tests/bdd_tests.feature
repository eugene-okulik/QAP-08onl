Feature: Bdd tests
  Scenario: Jobs for QA Auto middle exist
    Given I am at home page
    When I switch to page with jobs
    And Select job as QA Auto
    And Select level as middle
    Then Jobs were selected

    Scenario: Qa auto courses exist
      Given I am at home page
      When I switch to courses page
      And I will find Python courses using the search bar
      Then Qa auto courses is displayed
