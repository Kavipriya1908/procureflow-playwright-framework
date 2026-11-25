Feature: Login
  As a ProcureFlow user
  I want to sign in with my email and password
  So that I can use the dashboard

  Background:
    Given I am on the login page

  @smoke @ui
  Scenario: Login page is displayed
    Then I should see the "Welcome back" heading

  @smoke @ui @needs_credentials
  Scenario: Valid user can log in
    When I log in with valid credentials
    Then I should be on the dashboard

  @regression @ui @negative
  Scenario: Wrong password shows an error
    When I log in with email "qa.invalid.user@example.com" and password "WrongPass123"
    Then I should see the error "Invalid email or password."

  @regression @ui @negative
  Scenario Outline: Empty fields show a message
    When I log in with email "<email>" and password "<password>"
    Then I should see the error "Please enter your email and password."

    Examples:
      | email                       | password     |
      |                             | WrongPass123 |
      | qa.invalid.user@example.com |              |