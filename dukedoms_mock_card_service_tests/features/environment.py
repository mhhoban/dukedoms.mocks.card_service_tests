from addict import Dict
from bravado.client import SwaggerClient
from bravado.swagger_model import load_file

def before_scenario(context, step):

    config = {
        'also_return_response': True,
        'validate_responses': True,
        'validate_requests': True,
        'validate_swagger_spec': True,
        'use_models': True,
        'formats': []
    }

    context.clients = Dict()
    context.clients.card_service = SwaggerClient.from_spec(
        load_file(
            'specs/mock_card_service_api.yaml',
        ),
        origin_url='mock-card-service',
        config=config
    )
