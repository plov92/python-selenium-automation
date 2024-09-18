# Created by SOL Green at 9/14/2024
Feature: Target circle benefits

  Scenario: Verify there are 10 benefit cells
    Given Open Target Circle page
    When Identify benefit cells
    Then Verify there are 10 benefit cells