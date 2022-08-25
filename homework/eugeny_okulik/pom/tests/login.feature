Feature: Login page

    Scenario: login field exists
    Given Я на главной странице
    When I click login button
    And click login field
    Then I see login field

    Scenario: password field exists
    Given Я на главной странице
    When I click login button
    Then I see password field