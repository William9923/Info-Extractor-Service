from flask import Blueprint, render_template, abort, request, jsonify

from apps.utils.config import generate_prefix_key

from apps.matcher_text.service import *
from apps.utils.model.algorithm import *
from apps.utils.model.preprocess import *
from apps.utils.model.output import *
from apps.utils.model.validation import *

text =  Blueprint('text', __name__, url_prefix= generate_prefix_key() + "/text")

@text.route('/', methods=['POST', 'GET'])
def text_service():
    form = TextForm(request.form)
    if request.method == "POST" :
        if form.validate():
            # inject the dependencies into the service
            service = TextService(KMPAlgorithm(), TextPreprocessor(), JsonOutputter())

            # inject data needed
            service.data = {
                'keyword' : request.form.get('keyword'),
                'content' : request.form.get('content'),
            }

            # exec the service
            return service.do()
        else :
            return jsonify({
                "error" : "Form not filled correctly"
            })

    return jsonify({
        "message" : "Welcome to Text Matcher Service"
    })

