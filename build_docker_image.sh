#!/bin/bash
SERVICE=dukedoms_mock_card_service_tests
docker build --build-arg service=$SERVICE \
--tag "mhhoban/$SERVICE:latest" .
