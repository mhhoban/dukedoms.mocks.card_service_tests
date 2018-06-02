from behave import given, then, when
from bravado.exception import HTTPNotFound
from hamcrest import assert_that, equal_to, has_item

from dukedoms_mock_card_service_tests.constants import (
    card_catalog as expected_card_catalog,
    expected_list as expected_card_list
)

@when('card service receives request for card catalog')
def request_card_service_catalog(context):
    """
    send request to card service for entire catalog
    """
    catalog, result = context.clients.card_service.cardInfo.get_card_catalog().result()
    assert_that(result.status_code, equal_to(200))
    context.card_catalog = catalog

@then('card service returns the expected card catalog')
def assert_card_catalog(context):
    """
    verify correct card service returned
    """
    for item in expected_card_catalog.keys():
        assert_that(
            context.card_catalog[item],
            equal_to(expected_card_catalog[item])
        )

@when('card service receives request for card list for game id "1337"')
def request_card_list(context):
    """
    verify card list endpoint working
    """
    card_list, result = context.clients.card_service.listOperations.get_card_list(
        gameId=1337
    ).result()
    assert_that(result.status_code, equal_to(200))
    context.card_list = card_list

@then('card service returns expected card list')
def assert_card_catalog(context):
    """
    verify correct card service returned
    """
    for item in expected_card_list.keys():
        assert_that(
            context.card_list[item],
            equal_to(expected_card_list[item])
        )

@when('card service receives request for card info for card ids')
def request_card_info(context):
    """
    query card service for a specific card's info
    """
    card_ids = [row['card id'] for row in context.table]

    card_info, result = context.clients.card_service.cardInfo.get_card_info(
        cardIds=card_ids
    ).result()

    assert_that(result.status_code, equal_to(200))
    context.card_info = card_info

@then('card service returns card info')
def assert_card_info(context):
    """
    assert correct card info retreived
    """
    for row in context.table:
        card = context.clients.card_service.get_model('CardInfo')(
            id=int(row['card id']),
            name=row['name'],
            category=row['category'],
            type=row['type'],
            cost=int(row['cost']),
            actions=row['actions'],
            value=int(row['value']),
            victoryPoints=int(row['victory points'])
        )
        assert_that(
            context.card_info,
            has_item(card)
        )
