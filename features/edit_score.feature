Feature: Edit Score
  In order to keep updated my previous registers about books
  As a user
  I want to edit a score of a book I created

  Background: There are registered users and a book score by one of them
    Given Exists a user "user1" with password "password"
    And Exists a user "user2" with password "password"
    And Exists book registered by "user1"
      | name            | score       |
      | Harry Potter    | 10          |

  Scenario: Edit a score of a book
    Given I login as user "user1" with password "password"
    When I edit the book score with name "Harry Potter"
      | score         |
      | 5            |
    Then I'm viewing the details page for book by "user1"
      | name            | score       |
      | Harry Potter    | 5           |
    And There are 1 book