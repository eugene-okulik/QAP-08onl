Feature: Find job QA Auto
  Scenario: Jobs for QA Auto middle exist
    Given I am at home page
    When I switch to page with jobs
    And Select job as QA Auto
    And Select level as middle
    Then Jobs were selected