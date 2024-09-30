# Created by SOL Green at 9/30/2024
Feature: Terms and Conditions


  Scenario: User can open and close Terms and Conditions from sign in page
    Given Open Target.com
    And Click on Sign in
    When Click on Sign in again
    And Store original window
    And Click on Target terms and conditions link
    And Switch to the newly opened window
    Then Verify Terms and Conditions page is opened
    And User can close new window and switch back to original
