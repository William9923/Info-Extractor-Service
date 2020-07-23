from flask import Blueprint, render_template, abort, request, jsonify
import logging

from apps.utils.config import generate_prefix_key

from apps.matcher_text.service import TextService
from apps.utils.model.algorithm import AlgorithmFactory
from apps.utils.model.validation import TextForm

LOG = logging.getLogger(__name__)
text =  Blueprint('text', __name__, url_prefix= generate_prefix_key() + "/text")

@text.route('/', methods=['POST', 'GET'])
def text_service():

    LOG.info("Text Service Called")
    form = TextForm(request.form)
    if request.method == "POST" :
        if form.validate():
            factory = AlgorithmFactory()
            try :
                algo = factory.getAlgo(request.form["algo"])
            except Exception :
                LOG.error("Failed to parse algorithm. Using default algorith : regex")
                algo = factory.getAlgo("regex") # default algorithm

            service = TextService(algo)

            LOG.info("Injecting service data")
            service.data = {
                'keyword' : request.form.get('keyword'),
                'content' : request.form.get('content'),
            }

            LOG.info("Executing Text service")
            return service.do()

        else :
            LOG.warning("Data Form not filled correctly. Beware of malicious attemps!!")
            return jsonify({
                "error" : "Prerequiste data not filled correctly"
            })

    return jsonify({
        "message" : "Welcome to Text Matcher Service"
    })

