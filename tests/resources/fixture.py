import pytest 

def mock_api(mocker, content):
    mocker.patch('apps.utils.model.preprocess.URLPreprocessor.make_request', return_value= None)
    mocker.patch('apps.utils.model.preprocess.URLPreprocessor.get_content', return_value= content)

def mock_statistic(mocker, stats):
    mocker.patch('apps.utils.model.service.Service.get_stats', return_value=stats)