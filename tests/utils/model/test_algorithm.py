import pytest

from apps.utils.model.algorithm import * 

@pytest.mark.parametrize("magic_keyword, expected_result", [
    ("kmp", KMPAlgorithm()),
    ("bm", BMAlgorithm()),
    ("regex", RegexAlgorithm())
])
def test_AlgorithmFactory_should_return_correct_algorithm(magic_keyword, expected_result):
    result = AlgorithmFactory().getAlgo(magic_keyword)
    assert str(result) == str(expected_result), f"{expected_result} expected, but get {result}"



@pytest.mark.parametrize("pattern, text", [
    ("aaa", "aabaabaaab")
])
def test_Algorithm_should_find_pattern(pattern, text):
    algos = [KMPAlgorithm(), BMAlgorithm(), RegexAlgorithm()]
    for algo in algos:
        algo.pattern = pattern 
        algo.text = text 
        result = algo.find()
        assert len(result) > 0, f"{algo} should find the pattern in the text"

@pytest.mark.parametrize("pattern, text", [
    ("aaa","aabaabaab")
])
def test_Algorithm_should_not_find_pattern(pattern, text):
    algos = [KMPAlgorithm(), BMAlgorithm(), RegexAlgorithm()]
    for algo in algos:
        algo.pattern = pattern 
        algo.text = text 
        result = algo.find()
        assert len(result) == 0, f"{algo} should not find the pattern in the text"

