Feature: Delete a book
  In order to keep updated the registers about books read
  As a user
  I want to delete a read book I created

  Background: There are registered users and a book score by one of them
    Given Exists a user "user1" with password "password"
    #And Exists a user "user2" with password "password"
    And Exists book registered by "user1"
     | name            | score       |
     | Harry Potter    | 10          |

  Scenario: Delete a score of a book
    Given I login as user "user1" with password "password"
    When I delete the book score with name "Harry Potter"
    Then I'm viewing the details without book created by "user1"
      | name            | score
    And There are 0 book