Feature: Mock Card Service

Scenario: Fetch Card Catalog
  When card service receives request for card catalog
  Then card service returns the expected card catalog

Scenario: Fetch Card List
  When card service receives request for card list for game id "1337"
  Then card service returns expected card list

Scenario: Card Info Request
  When card service receives request for card info for card ids:
    | card id |
    | 1       |
  Then card service returns card info:
    | card id | name        | category | type     | cost | actions | value | victory points |
    | 1       | Bronze Coin | treasure | treasure | 0    | None    | 1     | 0              |
