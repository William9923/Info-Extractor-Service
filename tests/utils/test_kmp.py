import pytest

from apps.utils.kmp import knuth_morris_prath,kmp_first_occurence

def test_kmp_should_should_match():

    pattern = "aaa"
    text = "aabaabaaab"

    assert len(knuth_morris_prath(pattern, text)) > 0, "Pattern matching should resulted in more than one occurence"

def test_kmp_should_not_match():
    pattern = "aaa"
    text = "aabaabaab"

    assert len(knuth_morris_prath(pattern, text)) == 0, "Pattern matching should resulted in more than one occurence"
