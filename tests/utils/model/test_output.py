import pytest
from flask import Flask, jsonify
import json
from apps.utils.model.output import * 

@pytest.mark.parametrize("input, expected_result", [
    ({},{}),
    ({"dummy" : "dummy"}, {"dummy" : "dummy"}),
    ({
        "answer": [],
        "metadata": {
            "seperator": "\f"
        },
        "stats": {
            "keyword": 0,
            "sentences": 0,
            "success": False,
            "time": 1.8824384212493896,
            "total_sentences": 0,
            "word": 0
        }
        }, 
        {
            "answer": [],
            "metadata": {
                "seperator": "\f"
            },
            "stats": {
                "keyword": 0,
                "sentences": 0,
                "success": False,
                "time": 1.8824384212493896,
                "total_sentences": 0,
                "word": 0
            }
        }),
    ])
def test_JsonOutputter_result(input, expected_result):
    app = Flask(__name__)
    with app.app_context():
        outputer = JsonOutputter()
        response = outputer.output(input)
        assert json.loads(response.get_data(True)) == expected_result