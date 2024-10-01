# Created by SOL Green at 10/1/2024
Feature: Target Help dropdown

  Scenario: User can choose different options from dropdown menu and
  verify the correct page opens

    Given Open Target Help page
    When Choose Gift Cards from Browse Help dropdown
    Then Verify Gift Card Page opened