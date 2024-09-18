# Created by SOL Green at 9/11/2024
Feature: Add product into Cart


  Scenario: Verify product is added into Cart
    Given Open Target main page
    When Search for tea
    Then Verify that correct search results shown for tea
    Then Add one product into Cart
    Then Check Cart has item
