
Feature: Target sign in

  Scenario: Verify Target sign in form opens
    Given Open Target.com
    When Click on Sign in
    When Click on Sign in again
    Then Verify Sign in form opened