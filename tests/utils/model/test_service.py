import pytest
from flask import Flask
import json
from itertools import product

from apps.utils.model.service import *
from apps.utils.model.algorithm import RegexAlgorithm
from apps.utils.model.preprocess import *
from apps.utils.model.output import *

from apps.matcher_text.service import TextService
from apps.matcher_scraper.service import ScrapperService

from tests.resources.fixture import * 
from tests.resources.generate_resource import *

@pytest.mark.parametrize("preprocessor, outputer, input, expected_result", [
    (service[0], service[1], service[2], service[3]) for service in list(
        product(
            [TextPreprocessor(), URLPreprocessor()],
            [JsonOutputter()],
            [data.get('input') for data in generate_service_resource()],
            [data.get('output') for data in generate_service_resource()],
        )
    )
])
def test_Service_job(preprocessor, outputer, input, expected_result, mocker):
    app = Flask(__name__)
    with app.app_context():
        service = Service(RegexAlgorithm(), preprocessor, outputer) # Using Default Algorithm
        mock_api(mocker, input.get('content'))
        service.data = input 
        mock_statistic(mocker, expected_result.get('stats'))
        assert json.loads(service.do().get_data(True), strict=False) == expected_result

# params : input, expected_result
@pytest.mark.parametrize("input, expected_result", [
    (data.get('input'), data.get('output')) for data in generate_service_resource()
])
def test_TextService_job(input, expected_result, mocker):
    app = Flask(__name__)
    with app.app_context():
        service = TextService(RegexAlgorithm())
        service.data = input 
        mock_statistic(mocker, expected_result.get('stats'))
        assert json.loads(service.do().get_data(True), strict=False) == expected_result

@pytest.mark.parametrize("input, expected_result", [
    (data.get('input'), data.get('output')) for data in generate_service_resource()
])
def test_ScrapperService_job(input, expected_result, mocker):
    app = Flask(__name__)
    with app.app_context():
        service = ScrapperService(RegexAlgorithm())
        mock_api(mocker, input.get('content'))
        service.data = input 
        mock_statistic(mocker, expected_result.get('stats'))
        assert json.loads(service.do().get_data(True), strict=False) == expected_result
