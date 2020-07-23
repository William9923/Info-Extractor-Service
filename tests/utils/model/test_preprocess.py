import pytest
from nltk import sent_tokenize

from apps.utils.model.preprocess import * 

@pytest.mark.parametrize("input, expected_token", [
    ("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam fermentum et nulla quis ullamcorper. Suspendisse fermentum pretium urna dictum lobortis.", 
    [['Lorem', 'ipsum', 'dolor', 'sit', 'amet', ',', 'consectetur', 'adipiscing', 'elit', '.'], 
    ['Aliquam', 'fermentum', 'et', 'nulla', 'quis', 'ullamcorper', '.'], 
    ['Suspendisse', 'fermentum', 'pretium', 'urna', 'dictum', 'lobortis', '.']]),

    ("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sapien. ",
    [['Lorem', 'ipsum', 'dolor', 'sit', 'amet', ',', 'consectetur', 'adipiscing', 'elit', '.'], 
    ['Morbi', 'sapien', '.']]),
])
def test_Preprocess_tokenizer(input, expected_token):
    preprocessor = Preprocessor()
    assert preprocessor.tokenizing(sent_tokenize(input)) == expected_token

# data = {
#     "keyword" : "",
#     "content" : "",
# }

# output = {
#     "keyword" : "",
#     "content" : "",
# }

# @pytest.mark.parametrize("input, expected_output", [
#     (data, output)
# ])
# def test_TextPreprocessor_preprocess(input, expected_output):
#     preprocessor = TextPreprocessor()
#     assert preprocessor.preprocess(input) == expected_output


# data = {
#     "keyword" : "",
#     "url" : "",
# }
# output = {
#     "keyword" : "",
#     "content" : "",
# }
# @pytest.mark.parametrize("input, expected_output", [
#     (data, output)
# ])
# def test_URLPreprocessor_preprocess(input, expected_output):
#     preprocessor = URLPreprocessor()
#     assert preprocessor.preprocess(input) == expected_output


