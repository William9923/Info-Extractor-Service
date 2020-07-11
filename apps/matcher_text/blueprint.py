from flask import Blueprint, render_template, abort, request, jsonify

from apps.utils.config import generate_prefix_key

from apps.matcher_text.util import *

text =  Blueprint('text', __name__, url_prefix= generate_prefix_key() + "/text")

@text.route('/', methods=['POST', 'GET'])
def text_service():
    if request.method == "POST":
        factory = ServiceFactory(request.form)
        service = TextService(KMPAlgorithm(), TextPreprocessor(), TextOutputter())
        service.data = {
            'keyword' : request.form.get('keyword'),
            'content' : request.form.get('content'),
        }
        return service.do()

    return jsonify({
        "message" : "Text Matcher Service"
    })

