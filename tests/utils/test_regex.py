import pytest

from apps.utils.regex import regex_function

def test_bm_should_should_match():

    pattern = "aaa"
    text = "aabaabaaab"

    assert len(regex_function(pattern, text)) > 0, "Pattern matching should resulted in more than one occurence"

def test_bm_should_not_match():
    pattern = "aaa"
    text = "aabaabaab"

    assert len(regex_function(pattern, text)) == 0, "Pattern matching should resulted in more than one occurence"

