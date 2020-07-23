import pytest 
from apps.utils.model.error import *

@pytest.mark.parametrize("message, expected_message", [
    ("",""),
    ("text preprocess error", "text preprocess error"),
    ("scrapper preprocess error", "scrapper preprocess error"),
])
def test_PreprocessingException_message(message, expected_message):
    try :
        raise PreprocessingException(message)
    except PreprocessingException as err:
        assert err.message == expected_message

@pytest.mark.parametrize("message, code, expected_status_code", [
    ("",400,400),
    ("", 500,500),
])
def test_PreprocessingException_status_code(message, code, expected_status_code):
    try :
        raise PreprocessingException(message, status_code=code)
    except PreprocessingException as err:
        assert err.status_code == expected_status_code

def test_PreprocessingException_state():
    try :
        raise PreprocessingException("")
    except PreprocessingException as err :
        assert err.state == "Preprocess"

@pytest.mark.parametrize("message, expected_message", [
    ("",""),
    ("text preprocess error", "text preprocess error"),
    ("scrapper preprocess error", "scrapper preprocess error"),
])
def test_OutputException_message(message, expected_message):
    try :
        raise OutputException(message)
    except OutputException as err:
        assert err.message == expected_message

@pytest.mark.parametrize("message, code, expected_status_code", [
    ("",400,400),
    ("", 500,500),
])
def test_OutputException_status_code(message, code, expected_status_code):
    try :
        raise OutputException(message, status_code=code)
    except OutputException as err:
        assert err.status_code == expected_status_code

def test_OutputException_state():
    try :
        raise OutputException("")
    except OutputException as err :
        assert err.state == "Output"

@pytest.mark.parametrize("message, expected_message", [
    ("",""),
    ("text preprocess error", "text preprocess error"),
    ("scrapper preprocess error", "scrapper preprocess error"),
])
def test_ServiceException_message(message, expected_message):
    try :
        raise ServiceException(message)
    except ServiceException as err:
        assert err.message == expected_message

@pytest.mark.parametrize("message, code, expected_status_code", [
    ("",400,400),
    ("", 500,500),
])
def test_ServiceException_status_code(message, code, expected_status_code):
    try :
        raise ServiceException(message, status_code=code)
    except ServiceException as err:
        assert err.status_code == expected_status_code

def test_ServiceException_state():
    try :
        raise ServiceException("")
    except ServiceException as err :
        assert err.state == "Service"

