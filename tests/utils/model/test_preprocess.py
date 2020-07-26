import pytest

from apps.utils.model.preprocess import * 
from tests.resources.generate_resource import *
from tests.resources.fixture import *

@pytest.mark.parametrize("input, expected_token", [
    (data['input'], data['output']) for data in generate_tokenize_resource()
])
def test_Preprocess_tokenizer(input, expected_token):
    preprocessor = Preprocessor()
    assert preprocessor.tokenizing(input) == expected_token

@pytest.mark.parametrize("input, expected_output", [
    (data['data_text'], data['output_text']) for data in generate_text_resource()
])
def test_TextPreprocessor_preprocess(input, expected_output):
    preprocessor = TextPreprocessor()
    assert preprocessor.preprocess(input) == expected_output


@pytest.mark.parametrize("input, expected_output", [
     (data['data_url'], data['output_url']) for data in generate_url_resource()
])
def test_URLPreprocessor_preprocess(input, expected_output, mocker):
    preprocessor = URLPreprocessor()
    mock_api(mocker, input.get('content'))
    assert preprocessor.preprocess(input) == expected_output


