
Feature: Target sign in

  Scenario: Verify Target sign in form opens
    Given Open Target.com
    When Click on Sign in
    And Click on Sign in again
    Then Verify Sign in form opened

  Scenario: Verify user is logged in
    Given Open Target.com
    When Click on Sign in
    And Click on Sign in again
    Then Input email Rusmeister.spb@gmail.com
    And Input password ****
    And Click on Sign in with password
    And Verify user is logged in

