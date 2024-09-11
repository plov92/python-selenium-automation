# Created by SOL Green at 9/11/2024
Feature: Verify "Cart is empty" message


  Scenario: Verify "Cart is empty" message in target.com
    Given Open Target main page
    When Click on Cart icon
    Then Verify "Your cart is empty" message