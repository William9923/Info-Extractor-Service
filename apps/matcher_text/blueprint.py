from flask import Blueprint, render_template, abort, request, jsonify

from apps.utils.config import generate_prefix_key

from apps.matcher_text.service import TextService
from apps.utils.model.algorithm import AlgorithmFactory
from apps.utils.model.validation import TextForm

text =  Blueprint('text', __name__, url_prefix= generate_prefix_key() + "/text")

@text.route('/', methods=['POST', 'GET'])
def text_service():
    form = TextForm(request.form)
    if request.method == "POST" :
        if form.validate():
            
            factory = AlgorithmFactory()
            try :
                algo = factory.getAlgo(request.form["algo"])
            except ValueError :
                # log information
                algo = factory.getAlgo("regex")


            # inject the dependencies into the service
            service = TextService(algo)

            # inject data needed
            service.data = {
                'keyword' : request.form.get('keyword'),
                'content' : request.form.get('content'),
            }

            # exec the service
            return service.do()
        else :
            return jsonify({
                "error" : "Prerequiste data not filled correctly"
            })

    return jsonify({
        "message" : "Welcome to Text Matcher Service"
    })

