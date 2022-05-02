Feature: Register a book
  In order to keep updated the registers about books read
  As a user
  I want to insert a read book

  Background: There is a registered user
    Given Exists a user "user" with password "password"

  Scenario: Register just a book name
    Given I login as user "user" with password "password"
    When I register book
      | name         |
      | Harry Potter |
    Then I'm viewing the details page for book by "user"
      | name         |
      | Harry Potter |
    And There are 1 book