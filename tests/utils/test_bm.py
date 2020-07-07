import pytest

from apps.utils.bm import boyer_moore,boyer_moore_first_occurence

def test_bm_should_should_match():

    pattern = "aaa"
    text = "aabaabaaab"

    assert len(boyer_moore(pattern, text)) > 0, "Pattern matching should resulted in more than one occurence"

def test_bm_should_not_match():
    pattern = "aaa"
    text = "aabaabaab"

    assert len(boyer_moore(pattern, text)) == 0, "Pattern matching should resulted in more than one occurence"
