# Created by SOL Green at 9/11/2024
Feature: Target Cart


  Scenario: Verify product is added into Cart
    Given Open Target main page
    When Search for tea
    Then Verify that correct search results shown for tea
    Then Add one product into Cart
    Then Check Cart has item

    @smoke
  Scenario: “Your cart is empty” message is shown for empty cart
    Given Open Target main page
    When Click on Cart icon
    Then Verify “Your cart is empty” message is shown